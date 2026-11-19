# iScholar 课程项目全局待办清单 (TODO)

本清单基于全项目代码、讲义、模板与工程验证记录整理，涵盖 **关键一致性修复与发布前必办**、**`ischolar` 本地应用**、**`website` 门户网站**、**讲义与技能包** 以及 **打包同步与工程基建** 五大维度。

优先级说明：`P0` 阻断性/事实性错误；`P1` 发布前必须完成；`P2` 功能增强与质量提升；`P3` 工程基建与长期改进。

---

## 一、P0 / P1：关键一致性修复与发布前必办

### 1. 讲义与 Obsidian Vault 技能包对齐

- [x] **[P0] 补齐第 6 个 Hermes Skill（`topic-scout`）**
  - **完成情况**：已新增 `lectures/obsidian-vault-template/skills/topic-scout/SKILL.md`（选题三角、FINER 五维体检、RQ 锤炼四步法、三组提示词模板、输出位置与质量核查清单）与 `00_索引.md`；`skills/README.md` 技能表已更新为 6 个；根目录 `README.md` 口径同步修正；`Obsidian_科研Vault标准模板与Hermes技能包.zip` 已按最新目录（18 个文件，含 `topic-scout`）重新打包。
  - **遗留**：已于 2026-11-15 22:06 重新上传百度网盘（`/iScholar课程/软件与视频工具箱/01_国产与开源软件工具包/`，18 个文件，18,390 字节），远端校验通过。

- [x] **[P1] 清理培训方案讲稿中的历史外部路径引用**
  - **完成情况**：
    - `training-plan/教师科研教学AI培训_原风格保图_校内模型增补版_v3_全文讲稿与版式说明.md` 中 99 处底图 / 模板 / 素材绝对路径已改写为说明性标注（`🖼️ 版式底图 / 🧩 版式模板 / 🎨 版式素材`），并在文首补充“素材未随仓库分发”的路径说明；来源 docx 路径改为仓库内相对路径。全文已无 `~/...`。
    - `lectures/obsidian-vault-template/skills/obsidian-search/SKILL.md`（5 处）与 `zotero-query/SKILL.md`（1 处）的个人 Vault 绝对路径已改为 `~/Obsidian/科研Vault/`；`第01课` 中的模板打开命令改为仓库相对路径。
  - **验收**：`grep -rn "~" lectures/ training-plan/` 无输出。

- [x] **[P1] 修正配套视频 01–04 时长标注并补录制指引**
  - **背景**：`00-课程总纲.md` 中 01–04 号视频原标注「约 2–3 分」，实测仅 5–15 秒（静态翻页步骤卡，非完整录屏），属事实性错误。
  - **完成情况**：
    - 总纲视频索引 01–04 时长改为实测值并加 ⏳步骤卡 标记，表下补「步骤卡说明」。
    - `00_国产与开源软件清单及下载指南.md` 视频章节补类型标注（⏳步骤卡 / ✅实操录屏）。
    - 新增 `software-and-videos/02_软件实操教学视频/README.md`：14 部视频状态总表、01–04 分步录制脚本（含统一录制规范）、录屏剪辑工具建议（OBS/剪映/Kdenlive）、替换与同步命令。
  - **验收**：`grep -rn "约 3 分" lectures/ software-and-videos/` 无输出；README 表与 `ffprobe` 实测时长一致。
  - **遗留**：01–04 完整版录屏待讲师按脚本补录后同名替换并重同步网盘。

- [x] **[P1] 修复 `ischolar` 在系统 Python 3.9 上的启动崩溃（双击即用兜底）**
  - **背景**：无 miniconda / uv 的机器上，`启动iScholar.command`/`.bat` 会用系统 Python（macOS 自带 3.9）建 venv，而后端 pydantic 模型与 FastAPI 路由的 `str | None` 注解在 3.9 求值时报 `TypeError`，后端进程崩溃，违反「双击即可运行」要求。
  - **完成情况**：`app/backend.py`（9 处）、`app/frontend.py`（2 处）、`app/prompts.py`（1 处）、`launcher.py`（2 处）共 14 处联合类型注解统一改为 `Optional[...]` 并补齐 `typing.Optional` 导入；`ischolar/README.md` 与本清单中的过时说明同步更新。
  - **验收**：系统 Python 3.9 下后端导入成功（20 条路由注册）、`launcher.py` 全栈启动 health 200 / 前端 200 无报错；`python3 -m pytest tests -q` 与 `~/miniconda3/bin/python -m pytest tests -q` 均 8 passed。

### 2. 校方信息确认与 `website/` 线上发布验收

- [ ] **[P1] 完成校方待确认参数填充与线上部署验收**（对应 `website/TODO.md` 中的 P1 项）
  - **代码侧已完成（2026-11-15）**：`npm ci`（373 包）、`npm run check`（ESLint + TypeScript + 内容一致性）与 `npm run build`（28 个静态页面）全部通过；`site.ts` 已将 Obsidian + Hermes 条目标记为 `tested` 并补充 6 Skills / 14 视频证据，L20 保持 `pending`；记录见 `website/docs/VERIFICATION.md`。
  - **仍待外部确认**：
    1. 课程联系邮箱与负责人标签（`siteConfig.contact`）。
    2. 16 次课的具体开课日期（`siteConfig.courseDates`，当前留空仅显示周次）。
    3. 校内共享 L20 算力实测参数（显存、驱动、并发配额、vLLM 接口地址、运维责任人），确认后由 `pending` 改为 `tested` / `confirmed`。
    4. 公开内容、素材许可、发布负责人、域名与部署目标。
  - **剩余验收**：确认上述信息后导入 Vercel 完成预览与正式环境检查，核验关键页面、课时汇总、移动导航、本地记录、打印视图、404 与站外请求，并补记部署地址。

- [x] **[P1] 修正 `website/README.md` 中的历史目录路径**
  - **完成情况**：运行章节已改为 `cd website/`；并清理文末残留的 `# ai-lecture` 标记。

---

## 二、P2：子系统功能增强与质量提升

### 1. `ischolar/` 本地科研智能体工作台（v6.2.0）

- [x] **[P2] 扩展实训任务链至完整 16 次课（32 课时）**
  - **完成情况**：`ischolar/app/prompts.py` 的 `TRAINING_TASKS` 已扩展为 `course-01`～`course-16`，字段含 `lesson` / `module` / `title` / `agent` / `dimension` / `steps`，与 `website/src/content/courses.ts` 的 16 次课标题和模块划分（科研 9 / 教学 6 / 办公 1）一一对应；新增 `TRAINING_MODULES` 供前端展示。
  - **前端**：`frontend.py` 实训页新增「按模块筛选」（全部 / 科研 18h / 教学 12h / 办公 2h）与当前视图完成度统计。
  - **验收**：`pytest` 断言 16 条任务、课次序列 `第01课…第16课`、模块计数 9/6/1 全部通过。

- [x] **[P2] 支持一键导出直接写入用户自定义 Obsidian `vault_path`**
  - **完成情况**：
    - `export-obsidian` 新增可选请求体 `ExportObsidianRequest`（`use_project_vault` / `custom_vault_path` / `backup_existing`）；优先级为自定义路径 > 项目 `vault_path` > 内置导出目录。
    - 新增 `POST /v1/projects/{project_id}/vault` 保存并校验 Vault 目录（不存在或非目录返回 400）。
    - 写入前比较内容：同名且内容不同时自动生成 `xxx.bak-YYYYMMDD-HHMMSS.md` 备份，响应返回 `used_custom_vault` 与 `backed_up_files`。
    - 前端侧边栏新增「📤 导出至 Obsidian Vault」区块：填路径、保存、勾选是否备份、一键导出。
    - 演示项目的初始 `vault_path` 改为空，避免误写课程模板目录。
  - **验收**：`pytest` 覆盖默认导出、自定义 Vault 导出、备份生成与无效路径 400，全部通过。

- [x] **[P2] 升级 FastAPI 生命周期写法并补充自动化测试**
  - **完成情况**：改用 `@asynccontextmanager lifespan` 初始化数据库，已移除 `@app.on_event("startup")`；新增 `ischolar/tests/test_backend.py`（8 个用例，使用隔离临时数据库与设置文件），覆盖健康检查、Provider、项目 CRUD、未知项目 404、离线回退运行、人工复核与上游上下文注入、证据台账、16 课任务、导出与备份、Vault 路径校验；`pyproject.toml` 增加 `test` extra 与 `pythonpath`/`testpaths` 配置。
  - **运行方式**：`cd ischolar && python -m pytest tests -q`（2026-11-16 已将 `str | None` 注解统一改为 `Optional[...]`，系统 Python 3.9 亦可运行；macOS 亦可用 `~/miniconda3/bin/python`）。
  - **验收**：8 passed；启动无 `on_event` 弃用警告。

- [x] **[P2] 完善错误处理与输入校验**
  - **完成情况**：新增 `_require_project()`，`/v1/projects/{id}/runs`、`/evidences`、`/v1/agent/run`、`/v1/evidences`、`/v1/projects/{id}/export-obsidian` 均校验项目存在性并返回 404；实训任务校验 `task_id`（404）与状态枚举（400）；模型输出未解析到 JSON 时写入 `_parse_warning`，前端以警告条展示。

### 2. `website/` 课程门户网站

- [x] **[P2] 支持浏览器本地学习记录 JSON 导入与恢复**（对应 `website/TODO.md` 建议改进项）
  - **完成情况**：`learning-store.ts` 新增 `previewImportLearning()`（JSON 解析、version 1、课程 ID、notes 键、sources 结构逐项校验，失败返回中文原因，绝不改动现有数据）与 `importLearning()`（写入前把原记录备份到 `ischolar-workbench:v1:backup`，再覆盖并同步全局状态）；`LocalRecords` 新增「导入本地 JSON」按钮、隐藏文件输入、导入前预览框（课次/笔记/来源数量与导出时间）和确认/取消。
  - **验收**：`tests/workbench.spec.ts` 新增用例「导出 → 清除 → 非法文件拒绝 → 合法文件确认恢复」在 desktop / mobile 均通过。

- [ ] **[P2] 跟进开发依赖安全审计项**（受阻于上游，非本地可解）
  - **现状（2026-11-16 复核）**：生产依赖 0 漏洞；开发依赖 ESLint 工具链中 `braces@3.0.3` 仍无修复版本；`napi-postinstall` 官方 tarball 仍 404，继续固定 `0.3.4`。
  - **行动**：上游发布修复版本后升级依赖、移除 override，并重跑 `npm run check`、`npm run build` 与 `npm run test:e2e`。

- [ ] **[P2] 补充原生浏览器与辅助技术人工验收**（需人工执行）
  - **现状**：自动化侧 Chromium 桌面/移动、WebKit 桌面/移动与 axe 扫描通过；本机 Playwright Firefox 二进制启动失败（`Could not find profile folder`，环境问题，已记录于工程验证记录）。
  - **行动**：发布前完成原生 Safari、Firefox 与 VoiceOver/NVDA 的键盘与朗读抽查，补跑 Firefox 自动化或人工回归，并记录到 `website/docs/VERIFICATION.md`。

---

## 三、P2 / P3：打包同步与仓库工程基建

- [x] **[P2] 初始化根仓库版本控制与 `.gitignore` 防护**
  - **完成情况**：根目录已 `git init` 并提交初始版本（`eb26e97`）；新增 `.gitignore` 排除 `__pycache__`、`*.pyc`、`.venv`、`provider_settings.json`、`ischolar_local.db`、`obsidian_exports/`、`node_modules`、`.next`、Playwright 报告与测试产物、`.DS_Store`、`.env*` 与本地记录导出。
  - **校验**：`git ls-files` 中无密钥、缓存、依赖、构建产物与数据库。
  - **说明**：`website/` 自带独立 `.git`（嵌套仓库），根仓库以 gitlink 方式引用，未合并其历史；如需统一管理，可后续 `git submodule` 化或移除内层仓库。

- [x] **[P3] 编写一键打包与百度网盘同步脚本（`scripts/package-and-sync.sh`）**
  - **完成情况**：脚本支持默认打包与 `--sync` 两种模式；自动清理 `__pycache__` / `.pytest_cache` / `.venv` / `__MACOSX` / `*.pyc` / `.DS_Store` / `*.bak-*`，打包时排除 `provider_settings.json`；重新生成 4 个 zip 并输出 `SHA256SUMS.txt`；`--sync` 模式经 `uvx bypy` 上传 4 个 zip + 软件清单 + 校验清单，并列出远端做尺寸核对。
  - **验收（2026-11-16 已执行）**：重复执行产物一致（文件数 21/18/15/13）；本地 `shasum -a 256 -c` 全部 OK；远端 7 个文件与本地尺寸一致（如 `iScholar_v6.2_…zip` 79,107 B）。
  - **注意**：14 部教学视频体积较大且上传易超时，不纳入本脚本；更新视频时仍需按单文件 `bypy upload`。

- [x] **[P3] 配置持续集成检查**
  - **完成情况**：新增 `.github/workflows/ci.yml`（push/PR 触发）：
    - `ischolar-backend`（Python 3.12）：安装依赖 → `py_compile` 字节码检查 → `pytest tests -q`；
    - `website-portal`（Node 22 + npm 缓存）：`npm ci` → `npm run check` → `npm run build` → 安装 Chromium → `npx playwright test tests/workbench.spec.ts --project=desktop --project=mobile`。
  - 本地等效入口：`scripts/check-all.sh`（ischolar pytest + website check/build），已于 2026-11-16 实际运行全部通过。
  - **说明**：完整 `test:e2e` 中的 Firefox 项目在本机环境启动失败（见工程验证记录），CI 仅跑 Chromium 桌面/移动两项目；推送到 GitHub 后即可启用。

- [x] **[P3] 补充 `ischolar/` 与根目录的开发说明文档**
  - **完成情况**：新增 `ischolar/README.md`，覆盖：目录结构与各文件职责；`data/` 三类本地数据（`ischolar_local.db` 四张表、`provider_settings.json` 密钥存储与掩码、`obsidian_exports/` 导出结构与备份规则）；端口与环境变量表（`ISCHOLAR_BACKEND_PORT` / `ISCHOLAR_FRONTEND_PORT` / `ISCHOLAR_BACKEND_URL` / `ISCHOLAR_NO_BROWSER` / `DEEPSEEK_API_KEY`，含换端口示例）；开发调试、测试（含 3.9 注意事项）、数据重置与打包命令；常见问题表。
  - 根目录 `README.md` 增加「本地一键检查与打包同步」小节与相关入口链接。

---

## 四、已完成基线（供对照）

- [x] 门户网站 16 次课 / 32 课时 / 18 份模板 / 5 个专题内容一致性校验通过。
- [x] Playwright 26 项检查通过，含多浏览器与 axe WCAG 2.2 A/AA 自动扫描。
- [x] 生产依赖审计 0 项已知漏洞。
- [x] iScholar v6.2 本地 7 大科研智能体、人工复核关口与 Obsidian 导出全链路验证通过。
- [x] 百度网盘 `/apps/bypy/iScholar课程/` 目录同步核验通过。
- [x] 核心讲义（15 份）与专题实战讲义（13 份）完成 Obsidian + Hermes 体系重构，Notion 相关表述已全部替换。
- [x] **核心讲义 10 课完成 Notion 风格重构**：统一课程属性卡（进度/时长/难度/工具/交付物/视频）、Callout 区块（目标/工具箱/视频跟练/概念/避坑/验收/FAQ），并新增“软件下载位置与使用方法”专节。
- [x] **实操视频扩充至 14 部**：`~/Downloads/AI-Video` 的 10 部录屏已按内容规范重命名为 `05`–`14`，归入 `software-and-videos/02_软件实操教学视频/`，并在对应课次与总纲视频索引中建立映射。
- [x] **软件清单升级为全课程工具总表**：覆盖知识库、智能体、模型、检索全文、文献管理、质性编码、问卷统计、语料库、编程、写作润色、查重、期刊查询、绘图、PPT、版本管理，并标注官方地址与国内镜像。
