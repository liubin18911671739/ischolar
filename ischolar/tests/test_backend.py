"""Backend regression tests for the local iScholar workspace.

Run from the ``ischolar`` directory:

    python -m pytest tests -q
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import backend


@pytest.fixture()
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    db_path = tmp_path / "test_ischolar.db"
    settings_path = tmp_path / "provider_settings.json"
    monkeypatch.setattr(backend, "DB_PATH", db_path)
    monkeypatch.setattr(backend, "SETTINGS_PATH", settings_path)
    monkeypatch.setattr(backend, "DATA_DIR", tmp_path / "data")
    settings_path.write_text(
        json.dumps(
            {
                "provider": "offline_demo",
                "base_url": "local://deterministic",
                "model": "ischolar-offline-edu-v1",
                "api_key": "",
                "temperature": 0.4,
                "fallback_to_offline": True,
            }
        ),
        encoding="utf-8",
    )
    with TestClient(backend.app) as test_client:
        yield test_client


def test_health_and_providers(client: TestClient) -> None:
    health = client.get("/v1/health")
    assert health.status_code == 200
    body = health.json()
    assert body["ok"] is True
    assert body["active_provider"] == "offline_demo"

    providers = client.get("/v1/providers").json()
    assert "deepseek" in providers["presets"]
    assert "topic" in providers["agents"]
    assert providers["current"]["api_key_masked"] in {"未配置", "已配置"} or "..." in providers["current"]["api_key_masked"]


def test_projects_create_and_list(client: TestClient) -> None:
    projects = client.get("/v1/projects").json()["projects"]
    assert any(p["id"] == "proj-demo" for p in projects)

    created = client.post(
        "/v1/projects",
        json={
            "title": "测试项目",
            "discipline": "外语教学",
            "research_question": "AI 反馈如何影响写作修改？",
            "description": "pytest 演示",
        },
    )
    assert created.status_code == 200
    project = created.json()["project"]
    assert project["title"] == "测试项目"

    listed = client.get("/v1/projects").json()["projects"]
    assert any(p["id"] == project["id"] for p in listed)


def test_unknown_project_returns_404(client: TestClient) -> None:
    assert client.get("/v1/projects/not-exist/runs").status_code == 404
    assert client.get("/v1/projects/not-exist/evidences").status_code == 404
    assert (
        client.post(
            "/v1/evidences",
            json={
                "project_id": "not-exist",
                "claim": "主张",
                "source_title": "来源",
            },
        ).status_code
        == 404
    )
    assert (
        client.post(
            "/v1/agent/run",
            json={"project_id": "not-exist", "agent": "topic", "payload": {}},
        ).status_code
        == 404
    )
    assert client.post("/v1/projects/not-exist/export-obsidian").status_code == 404


def test_agent_run_offline_fallback_and_approval(client: TestClient) -> None:
    run_response = client.post(
        "/v1/agent/run",
        json={
            "project_id": "proj-demo",
            "agent": "topic",
            "payload": {"discipline": "区域国别研究", "keywords": "生态叙事, 旅游"},
        },
    )
    assert run_response.status_code == 200
    run = run_response.json()["run"]
    assert run["provider"].startswith("offline_demo")
    assert run["structured"]["topics"]
    assert run["approved"] == 0

    approved = client.post(
        f"/v1/runs/{run['id']}/approve",
        json={"approved": True, "reviewer_note": "已核对文献页码"},
    )
    assert approved.status_code == 200
    assert approved.json()["run"]["approved"] == 1
    assert approved.json()["run"]["reviewer_note"] == "已核对文献页码"

    # Approved output should be injected as upstream context on the next run.
    second = client.post(
        "/v1/agent/run",
        json={
            "project_id": "proj-demo",
            "agent": "litreview",
            "payload": {"query": "生态话语"},
            "use_upstream_context": True,
        },
    )
    assert second.status_code == 200
    assert "[topic 已复核成果摘要]" in second.json()["run"]["prompt_text"]

    runs = client.get("/v1/projects/proj-demo/runs").json()["runs"]
    assert len(runs) >= 2


def test_evidence_create_and_query(client: TestClient) -> None:
    created = client.post(
        "/v1/evidences",
        json={
            "project_id": "proj-demo",
            "claim": "生成式 AI 服务需落实内容标识",
            "source_title": "生成式人工智能服务管理暂行办法",
            "source_locator": "第十二条",
            "url_or_doi": "https://www.cac.gov.cn/",
            "permission_status": "public_policy",
            "review_status": "verified",
            "reviewer": "课程组",
        },
    )
    assert created.status_code == 200
    evidence = created.json()["evidence"]
    assert evidence["claim"].startswith("生成式 AI")

    listed = client.get("/v1/projects/proj-demo/evidences").json()["evidences"]
    assert any(item["id"] == evidence["id"] for item in listed)


def test_training_tasks_cover_16_lessons(client: TestClient) -> None:
    tasks = client.get("/v1/training/tasks").json()["tasks"]
    assert len(tasks) == 16
    assert [t["lesson"] for t in tasks] == [f"第{n:02d}课" for n in range(1, 17)]
    modules = [t["module"] for t in tasks]
    assert modules.count("research") == 9
    assert modules.count("teaching") == 6
    assert modules.count("office") == 1

    updated = client.post(
        "/v1/training/tasks/course-10",
        json={"status": "completed", "reflection": "已完成脚本初稿"},
    )
    assert updated.status_code == 200

    tasks_after = client.get("/v1/training/tasks").json()["tasks"]
    target = next(t for t in tasks_after if t["id"] == "course-10")
    assert target["status"] == "completed"
    assert target["reflection"] == "已完成脚本初稿"

    assert (
        client.post(
            "/v1/training/tasks/not-a-task", json={"status": "completed"}
        ).status_code
        == 404
    )
    assert (
        client.post(
            "/v1/training/tasks/course-01", json={"status": "done"}
        ).status_code
        == 400
    )


def test_export_default_and_custom_vault_with_backup(
    client: TestClient, tmp_path: Path
) -> None:
    default_export = client.post(
        "/v1/projects/proj-demo/export-obsidian",
        json={"use_project_vault": False},
    )
    assert default_export.status_code == 200
    default_body = default_export.json()
    assert default_body["used_custom_vault"] is False
    assert Path(default_body["export_dir"]).exists()

    vault = tmp_path / "obsidian-vault"
    vault.mkdir()

    first = client.post(
        "/v1/projects/proj-demo/export-obsidian",
        json={"use_project_vault": False, "custom_vault_path": str(vault)},
    )
    assert first.status_code == 200
    first_body = first.json()
    assert first_body["used_custom_vault"] is True
    assert (vault / "00_项目卡" / "研究项目卡.md").exists()
    assert (vault / "04_证据与来源台账" / "证据台账.md").exists()

    # 模拟用户手工修改后再导出：应生成时间戳备份而不是直接覆盖
    card = vault / "00_项目卡" / "研究项目卡.md"
    card.write_text(card.read_text(encoding="utf-8") + "\n> 用户手工补充：保留这段话。\n", encoding="utf-8")

    second = client.post(
        "/v1/projects/proj-demo/export-obsidian",
        json={
            "use_project_vault": False,
            "custom_vault_path": str(vault),
            "backup_existing": True,
        },
    )
    assert second.status_code == 200
    assert second.json()["backed_up_files"] >= 1
    backups = list((vault / "00_项目卡").glob("研究项目卡.bak-*.md"))
    assert backups

    missing = client.post(
        "/v1/projects/proj-demo/export-obsidian",
        json={"use_project_vault": False, "custom_vault_path": str(tmp_path / "nope")},
    )
    assert missing.status_code == 400


def test_project_vault_path_update(client: TestClient, tmp_path: Path) -> None:
    vault = tmp_path / "vault"
    vault.mkdir()
    ok = client.post(f"/v1/projects/proj-demo/vault", json={"vault_path": str(vault)})
    assert ok.status_code == 200
    assert ok.json()["project"]["vault_path"] == str(vault)

    export = client.post("/v1/projects/proj-demo/export-obsidian", json={})
    assert export.status_code == 200
    assert export.json()["used_custom_vault"] is True

    bad = client.post(
        "/v1/projects/proj-demo/vault", json={"vault_path": str(tmp_path / "missing")}
    )
    assert bad.status_code == 400
