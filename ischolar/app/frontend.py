"""Streamlit frontend for the local standalone iScholar application."""

from __future__ import annotations

import os
from typing import Any, Optional

import httpx
import streamlit as st

API_BASE = os.environ.get("ISCHOLAR_BACKEND_URL", "http://127.0.0.1:8765")

st.set_page_config(
    page_title="iScholar 本地科研智能体工作台 (Obsidian + Hermes)",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
    .stMetric { background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.25); padding: 0.75rem; border-radius: 0.5rem; }
    </style>
    """,
    unsafe_allow_html=True,
)


def api_get(path: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any]:
    with httpx.Client(timeout=30.0) as client:
        resp = client.get(f"{API_BASE}{path}", params=params)
        resp.raise_for_status()
        return resp.json()


def api_post(path: str, payload: Optional[dict[str, Any]] = None) -> dict[str, Any]:
    with httpx.Client(timeout=120.0) as client:
        resp = client.post(f"{API_BASE}{path}", json=payload or {})
        resp.raise_for_status()
        return resp.json()


# Verify backend health
try:
    health = api_get("/v1/health")
    prov_info = api_get("/v1/providers")
except Exception as exc:
    st.error(
        f"无法连接本地 FastAPI 后端 ({API_BASE})：{exc}\n\n"
        "请使用项目根目录下的双击启动器 `启动iScholar.command`（macOS）或 `启动iScholar.bat`（Windows）同时拉起前后端。"
    )
    st.stop()

presets = prov_info.get("presets", {})
current_cfg = prov_info.get("current", {})
agents_meta = prov_info.get("agents", {})

# ─── Sidebar: Model & API Key Configuration + Project Selection ───
with st.sidebar:
    st.title("🎓 iScholar 科研工作台")
    st.caption("本地免配置版 · Streamlit + FastAPI · Obsidian + Hermes 协同")

    with st.expander("🔑 大模型与 API 秘钥设置", expanded=not health.get("has_api_key")):
        prov_keys = list(presets.keys())
        cur_prov = current_cfg.get("provider", "deepseek")
        prov_idx = prov_keys.index(cur_prov) if cur_prov in prov_keys else 0

        selected_prov = st.selectbox(
            "选择模型服务商",
            options=prov_keys,
            index=prov_idx,
            format_func=lambda k: presets[k]["label"],
        )

        preset_url = presets[selected_prov]["base_url"]
        preset_model = presets[selected_prov]["default_model"]

        base_url_input = st.text_input(
            "API 接口地址 (Base URL)",
            value=current_cfg.get("base_url") if selected_prov == cur_prov else preset_url,
        )
        model_input = st.text_input(
            "模型名称 (Model)",
            value=current_cfg.get("model") if selected_prov == cur_prov else preset_model,
        )
        api_key_input = st.text_input(
            "API 秘钥 (如 DeepSeek Key，本地保存在本机)",
            value="",
            type="password",
            placeholder=f"当前状态：{current_cfg.get('api_key_masked', '未配置')}",
        )
        temp_input = st.slider(
            "生成温度 (Temperature)",
            min_value=0.0,
            max_value=1.0,
            value=float(current_cfg.get("temperature", 0.4)),
            step=0.1,
        )
        fallback_input = st.checkbox(
            "无秘钥或断网时自动使用本地教学演示引擎",
            value=bool(current_cfg.get("fallback_to_offline", True)),
        )

        col_s1, col_s2 = st.columns(2)
        with col_s1:
            if st.button("💾 保存配置", use_container_width=True):
                api_post(
                    "/v1/providers",
                    {
                        "provider": selected_prov,
                        "base_url": base_url_input,
                        "model": model_input,
                        "api_key": api_key_input,
                        "temperature": temp_input,
                        "fallback_to_offline": fallback_input,
                    },
                )
                st.success("已保存至本地！")
                st.rerun()
        with col_s2:
            if st.button("🔌 测试连接", use_container_width=True):
                res = api_post(
                    "/v1/providers/test",
                    {
                        "provider": selected_prov,
                        "base_url": base_url_input,
                        "model": model_input,
                        "api_key": api_key_input or current_cfg.get("api_key", ""),
                        "temperature": temp_input,
                        "fallback_to_offline": fallback_input,
                    },
                )
                if res.get("ok"):
                    st.success(res.get("message"))
                else:
                    st.warning(res.get("message"))

    st.divider()
    st.subheader("📁 当前科研项目")
    projects = api_get("/v1/projects").get("projects", [])
    proj_map = {p["id"]: p for p in projects}
    selected_proj_id = st.selectbox(
        "切换项目",
        options=list(proj_map.keys()),
        format_func=lambda pid: proj_map[pid]["title"],
    )
    active_project = proj_map[selected_proj_id]

    with st.expander("➕ 新建科研/课程项目"):
        new_title = st.text_input("项目名称", placeholder="例如：生成式AI辅助大学英语写作实证研究")
        new_disc = st.text_input("所属学科", value="外语教学 / 区域国别 / 旅游管理")
        new_rq = st.text_area("初步研究问题", placeholder="输入拟探索的核心问题...")
        if st.button("创建项目", use_container_width=True) and new_title.strip():
            api_post(
                "/v1/projects",
                {
                    "title": new_title,
                    "discipline": new_disc,
                    "research_question": new_rq,
                    "description": "用户自建科研智能体项目",
                },
            )
            st.success("创建成功！")
            st.rerun()

    st.divider()
    with st.expander("📤 导出至 Obsidian Vault", expanded=False):
        vault_input = st.text_input(
            "目标 Vault 目录（留空则导出到应用内置目录）",
            value=active_project.get("vault_path", ""),
            placeholder="例如：~/Obsidian/科研Vault",
            help="目录必须已存在。导出会写入 00_项目卡、01_原始资料_只读、02_工作区_Agent草稿、03_已复核成果、04_证据与来源台账。",
        )
        c_v1, c_v2 = st.columns(2)
        with c_v1:
            if st.button("💾 保存 Vault 路径", use_container_width=True):
                try:
                    saved = api_post(f"/v1/projects/{selected_proj_id}/vault", {"vault_path": vault_input})
                    st.success(f"已保存：{saved['project']['vault_path'] or '未设置'}")
                    st.rerun()
                except Exception as exc:
                    st.error(f"保存失败：{exc}")
        with c_v2:
            backup_existing = st.checkbox("同名文件先备份", value=True)
        if st.button("📤 一键导出当前项目", use_container_width=True):
            try:
                exp_res = api_post(
                    f"/v1/projects/{selected_proj_id}/export-obsidian",
                    {
                        "use_project_vault": True,
                        "custom_vault_path": vault_input.strip(),
                        "backup_existing": backup_existing,
                    },
                )
                msg = (
                    f"已导出 {exp_res['files_written']} 份 Markdown 文件至：\n`{exp_res['export_dir']}`"
                )
                if exp_res.get("used_custom_vault"):
                    msg += "\n\n✅ 已写入自定义 Obsidian Vault。"
                if exp_res.get("backed_up_files"):
                    msg += f"\n\n🗂️ 已为 {exp_res['backed_up_files']} 个同名文件生成时间戳备份。"
                st.success(msg)
            except Exception as exc:
                st.error(f"导出失败：{exc}")

# ─── Main Header & Status Metrics ───
st.markdown(f"## 🏛️ {active_project['title']}")
st.caption(
    f"**学科方向**：{active_project['discipline']} ｜ **核心研究问题**：{active_project['research_question'] or '待定'} ｜ "
    f"**当前模型**：`{current_cfg.get('provider')} / {current_cfg.get('model')}`（秘钥状态：{current_cfg.get('api_key_masked')}）"
)

runs_all = api_get(f"/v1/projects/{selected_proj_id}/runs").get("runs", [])
evs_all = api_get(f"/v1/projects/{selected_proj_id}/evidences").get("evidences", [])
tasks_all = api_get("/v1/training/tasks").get("tasks", [])
approved_count = sum(1 for r in runs_all if r.get("approved"))
completed_tasks = sum(1 for t in tasks_all if t.get("status") == "completed")

m1, m2, m3, m4 = st.columns(4)
m1.metric("🤖 智能体执行次数", f"{len(runs_all)} 次")
m2.metric("✅ 已人工复核成果", f"{approved_count} 份")
m3.metric("📚 已登记核验来源", f"{len(evs_all)} 条")
m4.metric("🎯 课程实训完成度", f"{completed_tasks} / {len(tasks_all)}")

tab_agents, tab_evidence, tab_training, tab_hermes = st.tabs(
    [
        "🚀 七大科研智能体工作流",
        "🔍 证据卡与来源核验台账",
        "📋 32课时实训任务与复盘",
        "💬 Hermes 科研顾问 (OpenCode / DSH)",
    ]
)

# ─── Tab 1: 7 Research Agents ───
with tab_agents:
    col_left, col_right = st.columns([1, 1.4], gap="large")

    with col_left:
        agent_keys = list(agents_meta.keys())
        selected_agent = st.selectbox(
            "选择当前研究阶段智能体",
            options=agent_keys,
            format_func=lambda k: f"{agents_meta[k]['name']} — {agents_meta[k]['short']}",
        )
        st.info(agents_meta[selected_agent]["description"])

        use_ctx = st.checkbox("自动注入上游阶段已人工复核的成果作为上下文", value=True)
        payload: dict[str, Any] = {}

        if selected_agent == "topic":
            payload["discipline"] = st.text_input("学科领域", value=active_project["discipline"])
            payload["keywords"] = st.text_input("核心关键词（逗号分隔）", value="生成式AI, 生态语料库, 中阿跨文化叙事")
            payload["targetJournal"] = st.text_input("目标期刊或课题类别", value="国家社科基金一般项目 / CSSCI核心期刊")
            payload["analysisMode"] = st.selectbox(
                "分析重心",
                options=["gap", "literature", "trends"],
                format_func=lambda x: {"gap": "研究空白发现 (Gap)", "literature": "文献脉络梳理", "trends": "前沿热点扫描"}[x],
            )
        elif selected_agent == "litreview":
            payload["query"] = st.text_input("检索与综述主题", value=active_project["research_question"] or active_project["title"])
            c1, c2 = st.columns(2)
            payload["yearFrom"] = c1.text_input("起始年份", value="2020")
            payload["yearTo"] = c2.text_input("截止年份", value="2026")
        elif selected_agent == "design":
            payload["researchQuestion"] = st.text_area("核心研究问题 (RQ)", value=active_project["research_question"] or active_project["title"])
            payload["methodology"] = st.selectbox(
                "拟采用研究方法",
                options=[
                    "混合方法（语料库量化统计 + 话语框架质性编码）",
                    "准实验设计（前后测问卷 + jamovi/JASP 配对检验）",
                    "定性研究（半结构化深度访谈 + 主题分析法）",
                    "文献计量与知识图谱分析（CiteSpace / VOSviewer）",
                ],
            )
        elif selected_agent == "data":
            payload["dataSource"] = st.text_input("数据或语料来源", value="中阿可持续旅游公开报道语料（200篇）与课堂调查问卷")
            payload["collectionMethod"] = st.text_input("采集与处理工具", value="Python清洗脚本 + AntConc语料检索 + jamovi统计")
        elif selected_agent == "write":
            payload["section"] = st.selectbox(
                "撰写模块",
                options=["introduction", "literature", "methods", "results", "discussion", "abstract"],
                format_func=lambda s: {
                    "introduction": "引言 (CARS三步模型)",
                    "literature": "文献综述与研究假设",
                    "methods": "研究设计与数据来源",
                    "results": "数据分析与实证结果",
                    "discussion": "讨论、理论贡献与研究局限",
                    "abstract": "中英双语摘要与关键词",
                }[s],
            )
            payload["citationStyle"] = st.selectbox("引用体例", options=["GB/T 7714-2015（中文核心期刊）", "APA 7th（国际SSCI期刊）"])
        elif selected_agent == "submit":
            payload["abstract"] = st.text_area("论文摘要草稿", value=active_project["description"], height=100)
            payload["keywords"] = st.text_input("论文关键词", value="生成式人工智能; 科研智能体; 语料库; 跨文化传播")
        elif selected_agent == "rebuttal":
            payload["reviewerComments"] = st.text_area(
                "审稿专家意见（每条意见一行）",
                value=(
                    "审稿意见1：研究方法部分对语料抽样标准与跨语言对齐清洗规则交代不够清晰。\n"
                    "审稿意见2：结论部分外推范围过大，建议补充案例边界与局限性讨论。"
                ),
                height=120,
            )

        payload["customPrompt"] = st.text_area("补充说明或特定约束（可选）", placeholder="可输入具体材料片段、字数要求或目标期刊特殊体例...")

        if st.button("▶️ 运行当前阶段智能体", type="primary", use_container_width=True):
            with st.spinner("智能体正在分析并生成结构化报告..."):
                run_res = api_post(
                    "/v1/agent/run",
                    {
                        "project_id": selected_proj_id,
                        "agent": selected_agent,
                        "payload": payload,
                        "use_upstream_context": use_ctx,
                    },
                )
                st.session_state["latest_run_id"] = run_res["run"]["id"]
                st.rerun()

    with col_right:
        st.subheader("📄 阶段产出与人工关口复核")
        agent_runs = [r for r in runs_all if r["agent"] == selected_agent]
        if not agent_runs:
            st.info("当前阶段尚无运行记录。请在左侧配置参数并点击「运行当前阶段智能体」。")
        else:
            selected_run_idx = st.selectbox(
                "历史运行记录",
                options=range(len(agent_runs)),
                format_func=lambda i: (
                    f"{agent_runs[i]['created_at']} ｜ {agent_runs[i]['provider']} ({agent_runs[i]['model']}) "
                    f"｜ {'✅已复核' if agent_runs[i]['approved'] else '⏳待复核'}"
                ),
            )
            current_run = agent_runs[selected_run_idx]
            st.markdown(current_run["output_markdown"])

            if current_run.get("structured"):
                if current_run["structured"].get("_parse_warning"):
                    st.warning(current_run["structured"]["_parse_warning"])
                with st.expander("🧩 查看解析后的结构化 JSON 数据"):
                    st.json(current_run["structured"])

            st.divider()
            st.markdown("#### 🛡️ 教师人工复核关口（证据先于流畅文本）")
            rev_note = st.text_input(
                "人工复核意见 / 原文核对记录",
                value=current_run.get("reviewer_note", ""),
                key=f"note_{current_run['id']}",
                placeholder="例如：已核对知网文献DOI与页码，保留候选选题1作为主攻方向。",
            )
            c_app1, c_app2 = st.columns(2)
            with c_app1:
                if st.button("✅ 标记为【已人工复核】（可进入下一阶段上下文）", key=f"app_{current_run['id']}", use_container_width=True):
                    api_post(
                        f"/v1/runs/{current_run['id']}/approve",
                        {"approved": True, "reviewer_note": rev_note},
                    )
                    st.success("已通过人工复核关口！")
                    st.rerun()
            with c_app2:
                if st.button("↩️ 标记为【待重新核查】", key=f"unapp_{current_run['id']}", use_container_width=True):
                    api_post(
                        f"/v1/runs/{current_run['id']}/approve",
                        {"approved": False, "reviewer_note": rev_note},
                    )
                    st.warning("已退回待核查状态。")
                    st.rerun()

# ─── Tab 2: Evidence Ledger ───
with tab_evidence:
    st.subheader("🔍 科研证据卡与来源许可登记台账")
    st.caption("遵循课程原则：AI 生成的题名、作者、DOI、法规与统计数字必须回到数据库或原文逐项核实。")

    with st.expander("➕ 新增一条经核实的科研证据卡", expanded=False):
        ec1, ec2 = st.columns(2)
        ev_claim = ec1.text_input("支持或质疑的核心主张")
        ev_source = ec2.text_input("原始来源题名 / 作者 / 年份")
        ev_loc = ec1.text_input("页码、段落或时间戳定位", placeholder="例如：第 12 页第 3 段")
        ev_url = ec2.text_input("DOI 或原始 URL 链接")
        ev_perm = ec1.selectbox("许可与使用边界", ["public_open (公开可用)", "campus_db (校内数据库授权)", "unknown (待核实授权)"])
        ev_status = ec2.selectbox("人工复核状态", ["verified (已核对原文)", "needs_review (待复核)"])
        ev_reviewer = st.text_input("复核人姓名", value="课程参训教师")

        if st.button("保存证据卡", type="primary") and ev_claim.strip() and ev_source.strip():
            api_post(
                "/v1/evidences",
                {
                    "project_id": selected_proj_id,
                    "claim": ev_claim,
                    "source_title": ev_source,
                    "source_locator": ev_loc,
                    "url_or_doi": ev_url,
                    "permission_status": ev_perm,
                    "review_status": ev_status,
                    "reviewer": ev_reviewer,
                },
            )
            st.success("证据卡已入库！")
            st.rerun()

    if evs_all:
        st.dataframe(evs_all, use_container_width=True)
    else:
        st.info("暂无证据记录。")

# ─── Tab 3: Training Tasks ───
with tab_training:
    st.subheader("📋 iScholar 32 课时 AI 科研与教学实训任务链")
    module_labels = {
        "all": "全部模块（32 课时）",
        "research": "科研模块（第 01–09 课 · 18 课时）",
        "teaching": "教学模块（第 10–15 课 · 12 课时）",
        "office": "办公综合（第 16 课 · 2 课时）",
    }
    selected_module = st.radio(
        "按模块筛选",
        options=list(module_labels.keys()),
        format_func=lambda k: module_labels[k],
        horizontal=True,
    )
    filtered_tasks = [
        t for t in tasks_all if selected_module == "all" or t.get("module") == selected_module
    ]
    done_in_view = sum(1 for t in filtered_tasks if t.get("status") == "completed")
    st.caption(f"当前视图：{done_in_view} / {len(filtered_tasks)} 项已完成")
    for t in filtered_tasks:
        with st.container(border=True):
            tc1, tc2 = st.columns([3, 1])
            with tc1:
                st.markdown(f"#### [{t['lesson']}] {t['title']}")
                st.caption(
                    f"模块：{module_labels.get(t.get('module', ''), '—')} ｜ "
                    f"能力维度：{t['dimension']} ｜ 对应智能体：`{agents_meta.get(t['agent'], {}).get('name', t['agent'])}`"
                )
                for idx, s in enumerate(t["steps"], 1):
                    st.markdown(f"{idx}. {s}")
            with tc2:
                cur_st = t.get("status", "pending")
                st_options = ["pending", "in_progress", "completed"]
                new_st = st.selectbox(
                    "完成状态",
                    options=st_options,
                    index=st_options.index(cur_st) if cur_st in st_options else 0,
                    format_func=lambda x: {"pending": "⏳ 未开始", "in_progress": "🔄 进行中", "completed": "✅ 已完成"}[x],
                    key=f"st_{t['id']}",
                )
            refl = st.text_input(
                "实操产出路径或课后反思记录",
                value=t.get("reflection", ""),
                key=f"refl_{t['id']}",
                placeholder="填写在 Obsidian Vault 中的文件路径或本课核验心得...",
            )
            if st.button("更新任务进度", key=f"btn_{t['id']}"):
                api_post(f"/v1/training/tasks/{t['id']}", {"status": new_st, "reflection": refl})
                st.success("已保存进度！")
                st.rerun()

# ─── Tab 4: Hermes Assistant ───
with tab_hermes:
    st.subheader("💬 Hermes 科研工作流顾问（Obsidian + OpenCode / DeepSeek Harness）")
    st.caption("围绕当前课题模块提问，获取 Obsidian 目录规范、Hermes Skill 编写或文献核验建议。")

    chat_agent = st.selectbox(
        "当前咨询模块上下文",
        options=list(agents_meta.keys()),
        format_func=lambda k: agents_meta[k]["name"],
        key="hermes_agent_sel",
    )

    if "hermes_messages" not in st.session_state:
        st.session_state["hermes_messages"] = [
            {
                "role": "assistant",
                "content": "你好！我是内置的 **Hermes 科研工作流顾问**。你可以向我咨询如何将当前课题沉淀到 **Obsidian Vault**、如何通过 **Hermes（OpenCode 或 DeepSeek Harness）** 调用阶段技能，或如何设计当前章节的提示词。",
            }
        ]

    for msg in st.session_state["hermes_messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_q = st.chat_input("输入你的科研方法、提示词或 Obsidian + Hermes 配置问题...")
    if user_q:
        st.session_state["hermes_messages"].append({"role": "user", "content": user_q})
        with st.chat_message("user"):
            st.markdown(user_q)
        with st.chat_message("assistant"):
            with st.spinner("Hermes 正在思考..."):
                res = api_post(
                    "/v1/hermes/chat",
                    {"agent": chat_agent, "message": user_q, "project_id": selected_proj_id},
                )
                reply_text = res.get("reply", "")
                st.markdown(reply_text)
                st.session_state["hermes_messages"].append({"role": "assistant", "content": reply_text})
