# iScholar 本地科研智能体工作台 — 开发说明

`iScholar` 是本地双击即用的科研智能体工作台：**Streamlit 前端（默认 8501 端口）+ FastAPI 后端（默认 8765 端口）+ SQLite 存储**，支持用户自填 DeepSeek / 通义千问 / Kimi / 智谱密钥，也可切换 Ollama 本地模型或离线教学演示引擎。

---

## 一、目录结构

```text
ischolar/
├── 启动iScholar.command            # macOS 双击启动器（自动检测环境 → 拉起前后端 → 打开浏览器）
├── 启动iScholar.bat                # Windows 双击启动器
├── launcher.py                     # 一键守护进程启动器
├── pyproject.toml                  # 依赖与 pytest 配置（testpaths / pythonpath）
├── requirements.txt                # pip 依赖
├── app/
│   ├── backend.py                  # FastAPI 后端（SQLite + OpenAI 兼容路由 + Obsidian 导出）
│   ├── frontend.py                 # Streamlit 前端（秘钥配置 + 7 大智能体 + 证据台账 + 16 课实训）
│   └── prompts.py                  # 7 大智能体提示词 / 结构化 JSON 解析 / 离线演示引擎 / 16 课任务链
├── tests/
│   └── test_backend.py             # 后端接口回归测试（8 个用例，隔离临时数据库）
└── data/                           # 本地运行数据（不入 Git，见下文）
```

---

## 二、本地数据目录（`ischolar/data/`）

> 该目录属于运行数据，`.gitignore` 已排除；删除后重新启动会自动重建（并注入演示项目 `proj-demo`）。

| 文件 / 目录 | 说明 |
| :-- | :-- |
| `ischolar_local.db` | SQLite 数据库。四张表：`projects`（项目）、`runs`（智能体运行记录与复核状态）、`evidences`（证据与来源台账）、`training_progress`（16 课实训进度）。首启自动建表并写入演示项目。 |
| `provider_settings.json` | **本地密钥存储**。保存当前模型服务商 / base_url / model / temperature / fallback 与 API Key。文件名出现在 `.gitignore`，**严禁提交或随包分发**；前端界面仅显示掩码（如 `sk-abc…wxyz`）。 |
| `obsidian_exports/` | 默认导出目录。结构：`00_项目卡`、`01_原始资料_只读`、`02_工作区_Agent草稿`、`03_已复核成果`、`04_证据与来源台账`。若配置了自定义 Obsidian Vault（见下文），导出会直接写入目标 Vault，同名旧文件自动生成 `*.bak-YYYYMMDD-HHMMSS.md` 备份。 |

---

## 三、端口与环境变量

| 变量 | 默认值 | 说明 |
| :-- | :-- | :-- |
| `ISCHOLAR_BACKEND_PORT` | `8765` | FastAPI 后端端口（接口文档：`http://127.0.0.1:<port>/docs`） |
| `ISCHOLAR_FRONTEND_PORT` | `8501` | Streamlit 前端端口 |
| `ISCHOLAR_BACKEND_URL` | `http://127.0.0.1:8765` | 前端访问后端地址（launcher 自动注入） |
| `ISCHOLAR_NO_BROWSER` | 未设置 | 设为 `1` 时启动后不自动打开浏览器 |
| `DEEPSEEK_API_KEY` | 未设置 | 后备默认密钥来源（读取自环境，UI 填入的 Key 优先） |

端口被占用时改用环境变量即可，例如：

```bash
ISCHOLAR_BACKEND_PORT=8766 ISCHOLAR_FRONTEND_PORT=8502 ./启动iScholar.command
```

---

## 四、开发、测试与数据重置

### 运行测试（推荐 Python ≥ 3.10）

```bash
cd ischolar
python -m pytest tests -q           # macOS 可用 ~/miniconda3/bin/python
```

- 测试使用临时目录（不写真实 `data/`），覆盖：健康检查、Provider 配置、项目 CRUD、未知项目 404、离线回退运行、人工复核与上游上下文注入、证据台账、16 课任务、默认/自定义 Vault 导出与备份、Vault 路径校验。
- 注解已统一改为 `Optional[...]` 写法，兼容系统 Python 3.9（2026-11-16 实测 3.9 全栈启动与 3.13 测试均通过）；推荐仍使用 Python ≥ 3.10。

### 启动开发服务（非双击方式）

```bash
cd ischolar
python launcher.py                       # 同时拉起 8765 与 8501
# 或分别调试：
python -m uvicorn app.backend:app --host 127.0.0.1 --port 8765 --reload
python -m streamlit run app/frontend.py --server.port 8501
```

### 重置本地数据

```bash
# 停止服务后执行
rm ischolar/data/ischolar_local.db                     # 重置项目/运行/证据/实训进度
rm ischolar/data/provider_settings.json                # 清除已保存的密钥与模型配置
rm -rf ischolar/data/obsidian_exports                  # 清空导出缓存
./启动iScholar.command                                  # 重启后自动重建演示项目
```

### 打包分发

```bash
./scripts/package-and-sync.sh          # 清理 + 重新打包 4 个 zip + SHA256SUMS.txt
./scripts/package-and-sync.sh --sync   # 同上并增量同步百度网盘
```

打包会自动排除 `provider_settings.json`、`__pycache__`、`.venv`、`.pytest_cache` 与 `.DS_Store`。

---

## 五、常见问题

| 问题 | 处理 |
| :-- | :-- |
| 双击启动报 `command not found` | 用 `./启动iScholar.command`（含 `cd` 到自身目录）；Windows 确认在 `ischolar/` 目录下运行 `.bat` |
| 8501/8765 端口被占用 | 见上表改用环境变量换端口 |
| 界面提示“无法连接本地 FastAPI 后端” | 先启动后端（或用 launcher 一键启动），确认 `/v1/health` 返回 ok |
| 测试报 `unsupported operand type(s) for |` | Python 版本低于 3.10，换用 3.10+ 解释器 |
| 导出失败提示“Vault 路径不存在” | 先创建目录或在界面填写已存在的本地 Vault 路径 |
