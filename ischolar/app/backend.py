"""FastAPI backend for the local standalone iScholar desktop/web application."""

from __future__ import annotations

import json
import os
import sqlite3
import uuid
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.prompts import (
    AGENT_META,
    SYSTEM_PROMPTS,
    TRAINING_TASKS,
    build_user_prompt,
    deterministic_fallback,
    parse_structured_output,
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "ischolar_local.db"
SETTINGS_PATH = DATA_DIR / "provider_settings.json"

DEFAULT_PROVIDERS: dict[str, dict[str, str]] = {
    "deepseek": {
        "label": "DeepSeek 官方 API（推荐·国产直连）",
        "base_url": "https://api.deepseek.com/v1",
        "default_model": "deepseek-chat",
    },
    "qwen": {
        "label": "阿里云百炼 / 通义千问（DashScope）",
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "default_model": "qwen-plus",
    },
    "kimi": {
        "label": "月之暗面 Kimi（Moonshot）",
        "base_url": "https://api.moonshot.cn/v1",
        "default_model": "kimi-k2-0711-preview",
    },
    "zhipu": {
        "label": "智谱清言 GLM（BigModel）",
        "base_url": "https://open.bigmodel.cn/api/paas/v4",
        "default_model": "glm-4-plus",
    },
    "ollama": {
        "label": "Ollama 本地开源模型（离线免Key）",
        "base_url": "http://127.0.0.1:11434/v1",
        "default_model": "qwen2.5:7b",
    },
    "campus_l20": {
        "label": "校内 L20 / vLLM 推理网关（OpenAI兼容）",
        "base_url": "http://127.0.0.1:8000/v1",
        "default_model": "Qwen2.5-14B-Instruct",
    },
    "offline_demo": {
        "label": "本地离线教学演示引擎（无需网络与API Key）",
        "base_url": "local://deterministic",
        "default_model": "ischolar-offline-edu-v1",
    },
}


def _now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S")


def _conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _require_project(conn: sqlite3.Connection, project_id: str) -> sqlite3.Row:
    row = conn.execute("SELECT * FROM projects WHERE id = ?", (project_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"项目不存在：{project_id}")
    return row


def _write_with_backup(path: Path, content: str, backup_existing: bool = True) -> bool:
    """Write content; back up an existing different file. Returns True if a backup was made."""
    backed_up = False
    if path.exists():
        try:
            same = path.read_text(encoding="utf-8") == content
        except Exception:
            same = False
        if same:
            return False
        if backup_existing:
            stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            backup = path.with_name(f"{path.stem}.bak-{stamp}{path.suffix}")
            path.replace(backup)
            backed_up = True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return backed_up


def init_db() -> None:
    with _conn() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS projects (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                discipline TEXT NOT NULL,
                research_question TEXT DEFAULT '',
                description TEXT DEFAULT '',
                vault_path TEXT DEFAULT '',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS runs (
                id TEXT PRIMARY KEY,
                project_id TEXT NOT NULL,
                agent TEXT NOT NULL,
                provider TEXT NOT NULL,
                model TEXT NOT NULL,
                prompt_text TEXT NOT NULL,
                output_markdown TEXT NOT NULL,
                structured_json TEXT DEFAULT '{}',
                approved INTEGER DEFAULT 0,
                reviewer_note TEXT DEFAULT '',
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS evidences (
                id TEXT PRIMARY KEY,
                project_id TEXT NOT NULL,
                claim TEXT NOT NULL,
                source_title TEXT NOT NULL,
                source_locator TEXT DEFAULT '',
                url_or_doi TEXT DEFAULT '',
                permission_status TEXT DEFAULT 'verified',
                review_status TEXT DEFAULT 'needs_review',
                reviewer TEXT DEFAULT '',
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS training_progress (
                task_id TEXT PRIMARY KEY,
                status TEXT NOT NULL DEFAULT 'pending',
                reflection TEXT DEFAULT '',
                updated_at TEXT NOT NULL
            );
            """
        )
        count = conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0]
        if count == 0:
            now = _now_iso()
            demo_id = "proj-demo"
            conn.execute(
                """
                INSERT INTO projects (id, title, discipline, research_question, description, vault_path, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    demo_id,
                    "中阿可持续旅游生态叙事语料库与跨文化传播研究",
                    "区域国别研究 / 旅游管理 / 外语教学",
                    "中阿语境下生态文明与可持续旅游叙事在官方、媒体与景区文本中的主题框架差异及其受众感知机制是什么？",
                    "iScholar 32 课时 AI 科研与教学培训示范项目：串联选题侦察、多语种文献综述、研究设计、语料库清洗与论文投稿全流程。",
                    "",
                    now,
                    now,
                ),
            )
            conn.execute(
                """
                INSERT INTO evidences (id, project_id, claim, source_title, source_locator, url_or_doi, permission_status, review_status, reviewer, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    "ev-001",
                    demo_id,
                    "生成式人工智能服务需落实数据来源合规与生成合成内容标识规范",
                    "《生成式人工智能服务管理暂行办法》与《人工智能生成合成内容标识办法》",
                    "正文条款与施行要求",
                    "https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm",
                    "public_policy",
                    "verified",
                    "课程责任教师",
                    now,
                ),
            )


def load_settings() -> dict[str, Any]:
    default_cfg = {
        "provider": "deepseek",
        "base_url": DEFAULT_PROVIDERS["deepseek"]["base_url"],
        "model": DEFAULT_PROVIDERS["deepseek"]["default_model"],
        "api_key": os.environ.get("DEEPSEEK_API_KEY", ""),
        "temperature": 0.4,
        "fallback_to_offline": True,
    }
    if SETTINGS_PATH.exists():
        try:
            saved = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
            if isinstance(saved, dict):
                default_cfg.update(saved)
        except Exception:
            pass
    return default_cfg


def save_settings(cfg: dict[str, Any]) -> dict[str, Any]:
    current = load_settings()
    current.update(cfg)
    SETTINGS_PATH.write_text(json.dumps(current, ensure_ascii=False, indent=2), encoding="utf-8")
    return current


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="iScholar Local Backend",
    version="6.2.0-local",
    description="iScholar 本地免配置科研智能体与培训工作台后端（FastAPI + SQLite + OpenAI兼容大模型路由）",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ProviderSettingsUpdate(BaseModel):
    provider: str = "deepseek"
    base_url: str = "https://api.deepseek.com/v1"
    model: str = "deepseek-chat"
    api_key: str = ""
    temperature: float = 0.4
    fallback_to_offline: bool = True


class ProjectCreate(BaseModel):
    title: str
    discipline: str = "外语 / 区域国别 / 旅游管理"
    research_question: str = ""
    description: str = ""
    vault_path: str = ""


class AgentRunRequest(BaseModel):
    project_id: str
    agent: str
    payload: dict[str, Any] = Field(default_factory=dict)
    use_upstream_context: bool = True
    # Optional per-request override so user can test keys directly
    provider: Optional[str] = None
    base_url: Optional[str] = None
    model: Optional[str] = None
    api_key: Optional[str] = None
    temperature: Optional[float] = None


class RunApprovalUpdate(BaseModel):
    approved: bool = True
    reviewer_note: str = ""


class EvidenceCreate(BaseModel):
    project_id: str
    claim: str
    source_title: str
    source_locator: str = ""
    url_or_doi: str = ""
    permission_status: str = "public"
    review_status: str = "needs_review"
    reviewer: str = ""


class TrainingUpdate(BaseModel):
    status: str
    reflection: str = ""


class ExportObsidianRequest(BaseModel):
    use_project_vault: bool = True
    custom_vault_path: str = ""
    backup_existing: bool = True


class VaultPathUpdate(BaseModel):
    vault_path: str = ""


class ChatRequest(BaseModel):
    agent: str = "topic"
    message: str
    project_id: Optional[str] = None


@app.get("/v1/health")
def health() -> dict[str, Any]:
    cfg = load_settings()
    return {
        "ok": True,
        "service": "ischolar-local-backend",
        "version": "6.2.0-local",
        "db_path": str(DB_PATH),
        "active_provider": cfg.get("provider"),
        "active_model": cfg.get("model"),
        "has_api_key": bool((cfg.get("api_key") or "").strip()),
    }


@app.get("/v1/providers")
def get_providers() -> dict[str, Any]:
    cfg = load_settings()
    masked = dict(cfg)
    raw_key = (cfg.get("api_key") or "").strip()
    masked["api_key_masked"] = (
        f"{raw_key[:6]}...{raw_key[-4:]}" if len(raw_key) > 10 else ("已配置" if raw_key else "未配置")
    )
    return {
        "presets": DEFAULT_PROVIDERS,
        "current": masked,
        "agents": AGENT_META,
    }


@app.post("/v1/providers")
def update_providers(body: ProviderSettingsUpdate) -> dict[str, Any]:
    current = load_settings()
    update_dict = body.model_dump()
    # If api_key is left blank in UI update and user already had one, only overwrite if explicitly cleared
    if not update_dict["api_key"] and current.get("api_key") and body.provider == current.get("provider"):
        update_dict["api_key"] = current["api_key"]
    saved = save_settings(update_dict)
    return {"ok": True, "current": saved}


@app.post("/v1/providers/test")
async def test_provider_connection(body: Optional[ProviderSettingsUpdate] = None) -> dict[str, Any]:
    cfg = body.model_dump() if body else load_settings()
    provider = cfg.get("provider") or "deepseek"
    base_url = (cfg.get("base_url") or "").rstrip("/")
    model = cfg.get("model") or "deepseek-chat"
    api_key = (cfg.get("api_key") or "").strip()

    if provider == "offline_demo" or base_url.startswith("local://"):
        return {
            "ok": True,
            "mode": "offline_demo",
            "message": "当前使用本地离线教学演示引擎，无需网络连接即可运行全部 7 大科研智能体。",
        }

    if provider != "ollama" and not api_key:
        return {
            "ok": False,
            "mode": provider,
            "message": "未检测到 API 秘钥（API Key）。请在左侧配置栏填入秘钥（如 DeepSeek Key），或切换为 Ollama 本地模型 / 离线教学演示模式。",
        }

    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            resp = await client.post(
                f"{base_url}/chat/completions",
                headers=headers,
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": "请仅回复：连接成功"}],
                    "max_tokens": 16,
                    "temperature": 0.1,
                },
            )
            if resp.status_code == 200:
                data = resp.json()
                reply = (
                    data.get("choices", [{}])[0]
                    .get("message", {})
                    .get("content", "")
                    .strip()
                )
                return {
                    "ok": True,
                    "mode": provider,
                    "message": f"模型连接测试成功！({model}) 响应：{reply}",
                }
            return {
                "ok": False,
                "mode": provider,
                "message": f"接口返回状态码 {resp.status_code}: {resp.text[:240]}",
            }
    except Exception as exc:
        return {
            "ok": False,
            "mode": provider,
            "message": f"连接异常：{exc}（若无网络或未启动本地服务，可开启自动回退离线演示模式）",
        }


@app.get("/v1/projects")
def list_projects() -> dict[str, Any]:
    with _conn() as conn:
        rows = conn.execute("SELECT * FROM projects ORDER BY updated_at DESC").fetchall()
    return {"projects": [dict(r) for r in rows]}


@app.post("/v1/projects")
def create_project(body: ProjectCreate) -> dict[str, Any]:
    pid = f"proj-{uuid.uuid4().hex[:8]}"
    now = _now_iso()
    with _conn() as conn:
        conn.execute(
            """
            INSERT INTO projects (id, title, discipline, research_question, description, vault_path, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                pid,
                body.title.strip(),
                body.discipline.strip(),
                body.research_question.strip(),
                body.description.strip(),
                body.vault_path.strip(),
                now,
                now,
            ),
        )
        row = conn.execute("SELECT * FROM projects WHERE id = ?", (pid,)).fetchone()
    return {"project": dict(row)}


@app.post("/v1/projects/{project_id}/vault")
def update_project_vault(project_id: str, body: VaultPathUpdate) -> dict[str, Any]:
    raw = body.vault_path.strip()
    resolved = ""
    if raw:
        candidate = Path(raw).expanduser()
        if not candidate.exists() or not candidate.is_dir():
            raise HTTPException(status_code=400, detail=f"Vault 路径不存在或不是目录：{candidate}")
        resolved = str(candidate)
    with _conn() as conn:
        _require_project(conn, project_id)
        conn.execute(
            "UPDATE projects SET vault_path = ?, updated_at = ? WHERE id = ?",
            (resolved, _now_iso(), project_id),
        )
        row = conn.execute("SELECT * FROM projects WHERE id = ?", (project_id,)).fetchone()
    return {"ok": True, "project": dict(row)}


@app.get("/v1/projects/{project_id}/runs")
def list_runs(project_id: str, agent: Optional[str] = None) -> dict[str, Any]:
    with _conn() as conn:
        _require_project(conn, project_id)
        if agent:
            rows = conn.execute(
                "SELECT * FROM runs WHERE project_id = ? AND agent = ? ORDER BY created_at DESC",
                (project_id, agent),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM runs WHERE project_id = ? ORDER BY created_at DESC",
                (project_id,),
            ).fetchall()
    result = []
    for r in rows:
        item = dict(r)
        try:
            item["structured"] = json.loads(item.get("structured_json") or "{}")
        except Exception:
            item["structured"] = {}
        result.append(item)
    return {"runs": result}


async def _call_llm(
    system_prompt: str,
    user_prompt: str,
    cfg: dict[str, Any],
    agent: str,
    payload: dict[str, Any],
) -> tuple[str, dict[str, Any], str, str]:
    provider = cfg.get("provider") or "deepseek"
    base_url = (cfg.get("base_url") or "").rstrip("/")
    model = cfg.get("model") or "deepseek-chat"
    api_key = (cfg.get("api_key") or "").strip()
    temperature = float(cfg.get("temperature") or 0.4)
    fallback_ok = bool(cfg.get("fallback_to_offline", True))

    if provider == "offline_demo" or base_url.startswith("local://"):
        text, structured = deterministic_fallback(agent, payload)
        return text, structured, "offline_demo", "ischolar-offline-edu-v1"

    if provider != "ollama" and not api_key:
        if fallback_ok:
            text, structured = deterministic_fallback(agent, payload)
            return text, structured, "offline_demo (未配置API Key自动回退)", "ischolar-offline-edu-v1"
        raise HTTPException(status_code=400, detail="未配置大模型 API 秘钥，请在侧边栏填入 DeepSeek 等模型的 API Key。")

    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    try:
        async with httpx.AsyncClient(timeout=90.0) as client:
            resp = await client.post(
                f"{base_url}/chat/completions",
                headers=headers,
                json={
                    "model": model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    "temperature": temperature,
                },
            )
            if resp.status_code != 200:
                if fallback_ok:
                    text, structured = deterministic_fallback(agent, payload)
                    return (
                        f"> ⚠️ **远端模型返回 {resp.status_code}，已自动回退本地演示引擎**：`{resp.text[:160]}`\n\n" + text,
                        structured,
                        f"{provider}->offline_fallback",
                        model,
                    )
                raise HTTPException(status_code=resp.status_code, detail=resp.text[:400])

            data = resp.json()
            content = (
                data.get("choices", [{}])[0]
                .get("message", {})
                .get("content", "")
                .strip()
            )
            structured = parse_structured_output(content) or {}
            return content, structured, provider, model
    except HTTPException:
        raise
    except Exception as exc:
        if fallback_ok:
            text, structured = deterministic_fallback(agent, payload)
            return (
                f"> ⚠️ **远端模型调用异常（{exc}），已自动切换本地离线演示输出**\n\n" + text,
                structured,
                f"{provider}->offline_fallback",
                model,
            )
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.post("/v1/agent/run")
async def run_agent(body: AgentRunRequest) -> dict[str, Any]:
    if body.agent not in SYSTEM_PROMPTS:
        raise HTTPException(status_code=400, detail=f"未知智能体: {body.agent}")

    cfg = load_settings()
    for field in ("provider", "base_url", "model", "api_key", "temperature"):
        val = getattr(body, field)
        if val is not None and val != "":
            cfg[field] = val

    context_parts: list[str] = []
    with _conn() as conn:
        _require_project(conn, body.project_id)
        if body.use_upstream_context:
            approved_rows = conn.execute(
                """
                SELECT agent, output_markdown FROM runs
                WHERE project_id = ? AND approved = 1
                ORDER BY created_at DESC LIMIT 3
                """,
                (body.project_id,),
            ).fetchall()
            for r in approved_rows:
                context_parts.append(f"[{r['agent']} 已复核成果摘要]:\n{r['output_markdown'][:600]}")

    user_prompt = build_user_prompt(body.agent, body.payload, "\n\n".join(context_parts))
    system_prompt = SYSTEM_PROMPTS[body.agent]

    output_md, structured, used_provider, used_model = await _call_llm(
        system_prompt, user_prompt, cfg, body.agent, body.payload
    )
    if not structured:
        structured = {
            "_parse_warning": "未在模型输出中解析到有效的 JSON 结构化代码块，已保留 Markdown 原文供人工复核。"
        }

    run_id = f"run-{uuid.uuid4().hex[:10]}"
    now = _now_iso()
    with _conn() as conn:
        conn.execute(
            """
            INSERT INTO runs (id, project_id, agent, provider, model, prompt_text, output_markdown, structured_json, approved, reviewer_note, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0, '', ?)
            """,
            (
                run_id,
                body.project_id,
                body.agent,
                used_provider,
                used_model,
                user_prompt,
                output_md,
                json.dumps(structured, ensure_ascii=False),
                now,
            ),
        )
        conn.execute("UPDATE projects SET updated_at = ? WHERE id = ?", (now, body.project_id))

    return {
        "run": {
            "id": run_id,
            "project_id": body.project_id,
            "agent": body.agent,
            "provider": used_provider,
            "model": used_model,
            "prompt_text": user_prompt,
            "output_markdown": output_md,
            "structured": structured,
            "approved": 0,
            "reviewer_note": "",
            "created_at": now,
        }
    }


@app.post("/v1/runs/{run_id}/approve")
def approve_run(run_id: str, body: RunApprovalUpdate) -> dict[str, Any]:
    with _conn() as conn:
        conn.execute(
            "UPDATE runs SET approved = ?, reviewer_note = ? WHERE id = ?",
            (1 if body.approved else 0, body.reviewer_note.strip(), run_id),
        )
        row = conn.execute("SELECT * FROM runs WHERE id = ?", (run_id,)).fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="运行记录不存在")
    return {"ok": True, "run": dict(row)}


@app.get("/v1/projects/{project_id}/evidences")
def list_evidences(project_id: str) -> dict[str, Any]:
    with _conn() as conn:
        _require_project(conn, project_id)
        rows = conn.execute(
            "SELECT * FROM evidences WHERE project_id = ? ORDER BY created_at DESC",
            (project_id,),
        ).fetchall()
    return {"evidences": [dict(r) for r in rows]}


@app.post("/v1/evidences")
def create_evidence(body: EvidenceCreate) -> dict[str, Any]:
    ev_id = f"ev-{uuid.uuid4().hex[:8]}"
    now = _now_iso()
    with _conn() as conn:
        _require_project(conn, body.project_id)
        conn.execute(
            """
            INSERT INTO evidences (id, project_id, claim, source_title, source_locator, url_or_doi, permission_status, review_status, reviewer, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                ev_id,
                body.project_id,
                body.claim.strip(),
                body.source_title.strip(),
                body.source_locator.strip(),
                body.url_or_doi.strip(),
                body.permission_status.strip(),
                body.review_status.strip(),
                body.reviewer.strip(),
                now,
            ),
        )
        row = conn.execute("SELECT * FROM evidences WHERE id = ?", (ev_id,)).fetchone()
    return {"evidence": dict(row)}


@app.get("/v1/training/tasks")
def get_training_tasks() -> dict[str, Any]:
    with _conn() as conn:
        rows = conn.execute("SELECT * FROM training_progress").fetchall()
    prog_map = {r["task_id"]: dict(r) for r in rows}
    tasks = []
    for t in TRAINING_TASKS:
        p = prog_map.get(t["id"], {})
        tasks.append(
            {
                **t,
                "status": p.get("status", "pending"),
                "reflection": p.get("reflection", ""),
                "updated_at": p.get("updated_at", ""),
            }
        )
    return {"tasks": tasks}


@app.post("/v1/training/tasks/{task_id}")
def update_training_task(task_id: str, body: TrainingUpdate) -> dict[str, Any]:
    valid_ids = {t["id"] for t in TRAINING_TASKS}
    if task_id not in valid_ids:
        raise HTTPException(status_code=404, detail=f"实训任务不存在：{task_id}")
    if body.status not in {"pending", "in_progress", "completed"}:
        raise HTTPException(status_code=400, detail="状态必须是 pending / in_progress / completed 之一")
    now = _now_iso()
    with _conn() as conn:
        conn.execute(
            """
            INSERT INTO training_progress (task_id, status, reflection, updated_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(task_id) DO UPDATE SET
                status = excluded.status,
                reflection = excluded.reflection,
                updated_at = excluded.updated_at
            """,
            (task_id, body.status, body.reflection.strip(), now),
        )
    return {"ok": True, "task_id": task_id, "status": body.status, "updated_at": now}


@app.post("/v1/projects/{project_id}/export-obsidian")
def export_to_obsidian(
    project_id: str, body: Optional[ExportObsidianRequest] = None
) -> dict[str, Any]:
    opts = body or ExportObsidianRequest()
    with _conn() as conn:
        proj = _require_project(conn, project_id)
        runs = conn.execute(
            "SELECT * FROM runs WHERE project_id = ? ORDER BY created_at ASC",
            (project_id,),
        ).fetchall()
        evs = conn.execute(
            "SELECT * FROM evidences WHERE project_id = ? ORDER BY created_at ASC",
            (project_id,),
        ).fetchall()

    target = (opts.custom_vault_path or "").strip()
    if not target and opts.use_project_vault:
        target = (proj["vault_path"] or "").strip()

    export_root = DATA_DIR / "obsidian_exports" / project_id
    used_custom = False
    if target:
        candidate = Path(target).expanduser()
        if not candidate.exists() or not candidate.is_dir():
            raise HTTPException(
                status_code=400,
                detail=f"Vault 路径不存在或不是目录：{candidate}。请先在项目设置中填写有效的本地 Obsidian Vault 目录。",
            )
        export_root = candidate
        used_custom = True

    for folder in (
        "00_项目卡",
        "01_原始资料_只读",
        "02_工作区_Agent草稿",
        "03_已复核成果",
        "04_证据与来源台账",
    ):
        (export_root / folder).mkdir(parents=True, exist_ok=True)

    backed_up = 0

    proj_card = (
        f"---\n"
        f"project_id: \"{proj['id']}\"\n"
        f"title: \"{proj['title']}\"\n"
        f"discipline: \"{proj['discipline']}\"\n"
        f"updated: \"{proj['updated_at']}\"\n"
        f"workflow: \"Obsidian + Hermes (OpenCode / DeepSeek Harness)\"\n"
        f"---\n\n"
        f"# {proj['title']}\n\n"
        f"- **学科方向**：{proj['discipline']}\n"
        f"- **核心研究问题**：{proj['research_question']}\n"
        f"- **项目简介**：{proj['description']}\n"
        f"- **智能体运行次数**：{len(runs)} 次\n"
        f"- **登记证据条数**：{len(evs)} 条\n"
    )
    if _write_with_backup(export_root / "00_项目卡" / "研究项目卡.md", proj_card, opts.backup_existing):
        backed_up += 1

    for r in runs:
        sub = "03_已复核成果" if r["approved"] else "02_工作区_Agent草稿"
        fname = f"{r['created_at'][:10]}_{r['agent']}_{r['id']}.md"
        note = (
            f"---\n"
            f"run_id: \"{r['id']}\"\n"
            f"agent: \"{r['agent']}\"\n"
            f"provider: \"{r['provider']}\"\n"
            f"model: \"{r['model']}\"\n"
            f"approved: {bool(r['approved'])}\n"
            f"reviewer_note: \"{r['reviewer_note']}\"\n"
            f"created_at: \"{r['created_at']}\"\n"
            f"---\n\n"
            f"# {AGENT_META.get(r['agent'], {}).get('name', r['agent'])}\n\n"
            f"## 提示词输入\n\n```text\n{r['prompt_text']}\n```\n\n"
            f"## 智能体输出\n\n{r['output_markdown']}\n"
        )
        if _write_with_backup(export_root / sub / fname, note, opts.backup_existing):
            backed_up += 1

    ev_lines = [
        "# 科研证据与来源核验台账\n",
        "| 证据ID | 支持主张 | 来源题名 | 页码/段落定位 | DOI/URL | 许可状态 | 人工复核状态 | 复核人 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for e in evs:
        ev_lines.append(
            f"| {e['id']} | {e['claim']} | {e['source_title']} | {e['source_locator']} | {e['url_or_doi']} | {e['permission_status']} | {e['review_status']} | {e['reviewer']} |"
        )
    if _write_with_backup(
        export_root / "04_证据与来源台账" / "证据台账.md",
        "\n".join(ev_lines) + "\n",
        opts.backup_existing,
    ):
        backed_up += 1

    return {
        "ok": True,
        "export_dir": str(export_root),
        "files_written": 2 + len(runs),
        "used_custom_vault": used_custom,
        "backed_up_files": backed_up,
    }


@app.post("/v1/hermes/chat")
async def hermes_chat(body: ChatRequest) -> dict[str, Any]:
    cfg = load_settings()
    agent_info = AGENT_META.get(body.agent, AGENT_META["topic"])
    system = (
        f"你是 iScholar 内置的 Hermes 科研顾问助手（支持 OpenCode 与 DeepSeek Harness 工作流），"
        f"当前正在协助教师使用【{agent_info['name']}】模块。\n"
        "请用简洁、务实的中文回答用户的科研方法、提示词设计、Obsidian 知识库组织或文献核验问题；"
        "始终强调“证据先于流畅文本、原始资料只读、引用必须回到知网或原文数据库核验”。"
    )
    provider = cfg.get("provider") or "deepseek"
    api_key = (cfg.get("api_key") or "").strip()
    base_url = (cfg.get("base_url") or "").rstrip("/")
    model = cfg.get("model") or "deepseek-chat"

    if provider != "offline_demo" and (provider == "ollama" or api_key):
        headers = {"Content-Type": "application/json"}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        try:
            async with httpx.AsyncClient(timeout=45.0) as client:
                resp = await client.post(
                    f"{base_url}/chat/completions",
                    headers=headers,
                    json={
                        "model": model,
                        "messages": [
                            {"role": "system", "content": system},
                            {"role": "user", "content": body.message},
                        ],
                        "temperature": 0.4,
                    },
                )
                if resp.status_code == 200:
                    reply = resp.json()["choices"][0]["message"]["content"]
                    return {"reply": reply, "provider": provider, "model": model}
        except Exception:
            pass

    fallback_reply = (
        f"**[Hermes 顾问 · {agent_info['name']}]**\n\n"
        f"收到你的问题：「{body.message}」\n\n"
        "建议按以下三步推进：\n"
        "1. **明确输入边界**：在 Obsidian Vault 的 `01_原始资料_只读/` 中准备好经核实的文献题录或脱敏样本。\n"
        "2. **分步调用智能体**：在当前模块填写具体学科、研究问题或检索词，生成候选方案与 JSON 结构化输出。\n"
        "3. **人工复核关口**：对照知网（CNKI）/ OpenAlex 原文核实页码与数据后，点击“标记为已人工复核”，再进入下一阶段或一键导出到 Obsidian Vault。\n\n"
        "*（提示：在左侧边栏填入 DeepSeek API Key 或开启本地 Ollama 后，此处将切换为实时大模型对话。）*"
    )
    return {"reply": fallback_reply, "provider": "offline_demo", "model": "ischolar-offline-edu-v1"}
