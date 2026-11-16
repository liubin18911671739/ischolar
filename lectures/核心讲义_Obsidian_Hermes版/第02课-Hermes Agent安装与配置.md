---
title: 第02课｜Hermes Agent 安装与配置
type: lesson
course: AI4S · 高校教师科研与教学 AI 实训
lesson: "02 / 10"
duration: 90 分钟（理论 25 + 实操 65）
difficulty: 入门 · 需少量命令行
progress: "▰▰▱▱▱▱▱▱▱▱ 20%"
tools:
  - Node.js
  - Hermes Agent
  - OpenCode CLI
  - iScholar 本地工作台
  - DeepSeek API
  - 通义千问 / Kimi
deliverables:
  - Hermes 安装成功并可执行 hermes --version
  - DeepSeek Provider 配置完成
  - 首次对话测试通过
  - iScholar 工作台可双击启动
videos:
  - 01_iScholar本地工作台_双击启动与DeepSeek秘钥配置教程.mp4
  - 02_Obsidian科研Vault与Hermes智能体配置教程.mp4
  - 05_VSCode_Anaconda环境配置与Hermes终端论文项目实战.mp4
tags: [AI4S, Hermes, Agent, 安装配置, 课程教案]
created: 2026-09-17
updated: 2026-11-15
---

# 第02课｜Hermes Agent 安装与配置

> [!abstract] 🎯 本课定位
> 上一课你有了一个**静态的**知识库。这一课给它装上**手脚**：让 AI 能读你的 Vault、写你的文件、按你的流程干活。
>
> **学完你将拥有**：一个能跑起来的 Hermes Agent、一个配置好的国产模型 Provider、一个双击即用的 iScholar 本地工作台，以及一次成功的真实对话。

> [!info] 📌 本课要建立的心智模型
> **Agent = Profile（身份）+ Skills（技能）+ Memory（记忆）+ Tools（工具）。**
> 模型只是“大脑”，Hermes 是把大脑接到你文件系统上的那套“神经系统”。

---

## 🧰 一、本课软件工具箱（下载 · 安装 · 备份）

> [!tip] 全部国产直连或开源免费；API 部分需自行注册获取 Key。

| 软件 / 服务 | 用途 | 官方地址 | 国内加速 / 镜像 | 百度网盘备份 |
| :-- | :-- | :-- | :-- | :-- |
| **Node.js 20+** | Hermes 运行时 | <https://nodejs.org/zh-cn> | 华为云镜像 <https://mirrors.huaweicloud.com/nodejs/>；macOS `brew install node` | `/iScholar课程/软件与视频工具箱/01_国产与开源软件工具包/` |
| **Hermes Agent** | 智能体引擎（开源） | <https://github.com/NousResearch/hermes-agent> | GitHub 国内可访问；`npm i -g hermes-agent` | 同上（含安装脚本说明） |
| **OpenCode CLI** | 终端内的代码/科研任务宿主 | <https://opencode.ai> | 官网直连 | 同上 |
| **iScholar 本地工作台** | 双击即用的图形界面工作台 | 本地 `ischolar/` | — | `iScholar_v6.2_本地双击即用版_Streamlit_FastAPI.zip` |
| **DeepSeek** | 主力大模型（性价比高） | <https://platform.deepseek.com> | 国内直连 | —（需注册获取 Key） |
| **通义千问** | 备选模型（阿里云百炼） | <https://bailian.console.aliyun.com> | 国内直连 | — |
| **Kimi（月之暗面）** | 长文档分析 | <https://platform.moonshot.cn> | 国内直连 | — |
| **智谱 GLM** | 备选模型 | <https://open.bigmodel.cn> | 国内直连 | — |
| **Ollama** | 本地离线模型（第 06 课） | <https://ollama.com> | 国内可直连下载；`brew install ollama` | 视频 `11` |

> [!example] 🎬 配套实操视频
> - **`01_iScholar本地工作台_双击启动与DeepSeek秘钥配置教程.mp4`**：双击启动、填 Key、跑第一个智能体。
> - **`02_Obsidian科研Vault与Hermes智能体配置教程.mp4`**：Obsidian 与 Hermes 打通。
> - **`05_VSCode_Anaconda环境配置与Hermes终端论文项目实战.mp4`**：在 VS Code 终端里用 Hermes 操作真实论文项目（`Poseidon` 界面、`deepseek-flash` 模型、Skills 加载过程）。

---

## 🤖 二、Hermes 是什么

Hermes Agent 是 Nous Research 开源的 AI Agent 框架，可在终端、桌面、消息平台（Telegram / Discord）运行。与普通聊天工具的区别在于：它**能调用工具、能读写文件、能记住上下文**。

### 2.1 Harness 架构

```text
┌─────────────────────────────────────────┐
│            Hermes Agent Harness          │
├─────────────┬─────────────┬─────────────┤
│   Tools     │   Skills    │   Memory    │
│  工具调用    │  技能模块    │  持久记忆    │
│  terminal   │  SKILL.md   │  对话历史    │
│  web_search │  模板/脚本   │  用户偏好    │
│  read/write │  参考文件    │  项目状态    │
├─────────────┴─────────────┴─────────────┤
│         Gateway（终端 / 桌面 / IM）        │
└─────────────────────────────────────────┘
```

### 2.2 四个核心概念

| 概念 | 是什么 | 在本课程中的用途 |
| :-- | :-- | :-- |
| **Tools** | Agent 可调用的外部能力 | 读写 Vault、检索网页、执行 Python |
| **Skills** | 可复用的知识与工作流（`SKILL.md`） | 6 个科研技能：检索、选题、综述、写作、返修 |
| **Memory** | 持久化上下文 | 记住你的学科、在研课题、写作偏好 |
| **Gateway** | 多平台入口 | 终端 CLI、桌面 GUI、Obsidian 内 Console |

> [!info] 为什么科研场景需要 Agent 而不是聊天框
> 聊天框里你得反复粘贴背景、手动复制结果；Agent 直接在你的 Vault 上工作，**读的是同一份文件，写回的是同一个目录**，过程留痕、可复核。

---

## 🔄 三、安装步骤

### 3.1 系统要求

| 项目 | 最低 | 推荐 |
| :-- | :-- | :-- |
| 操作系统 | macOS 12 / Windows 10（WSL2）/ Ubuntu 20.04 | macOS 14+ / Windows 11 |
| Node.js | v18 | **v20 或 v22 LTS** |
| 内存 | 4 GB | 8 GB+（跑本地模型需 16 GB+） |
| 磁盘 | 2 GB 空闲 | 10 GB+（含模型缓存） |

### 3.2 安装 Node.js

**macOS**

```bash
# 方式一：Homebrew
brew install node

# 方式二：官网安装包
# https://nodejs.org/zh-cn 下载 LTS 版本 .pkg
```

**Windows**

```powershell
# 官网下载 LTS .msi 安装包，勾选 "Add to PATH"
# 或使用 winget
winget install OpenJS.NodeJS.LTS
```

**验证**

```bash
node --version   # 期望 v20.x 或 v22.x
npm --version    # 期望 10.x 以上
```

> [!warning] 国内 npm 安装慢
> 设置国内镜像后再装：
> ```bash
> npm config set registry https://registry.npmmirror.com
> ```

### 3.3 安装 Hermes Agent

```bash
# 方式一：官方一键脚本（推荐）
curl -fsSL https://hermes.nousresearch.com/install.sh | bash

# 方式二：npm 全局安装
npm install -g hermes-agent

# 验证
hermes --version
```

### 3.4 运行安装向导

```bash
hermes setup
```

向导会依次询问：

1. 选择或新建 Profile（建议先建 `research`）
2. 选择模型 Provider（本课选 **DeepSeek**）
3. 填入 API Key
4. 选择默认模型（`deepseek-chat`）
5. 确认工具权限（先只开 `read_file`、`write_file`、`web_search`，暂不开 `terminal`）

### 3.5 获取 DeepSeek API Key

```text
1. 打开 https://platform.deepseek.com → 注册 / 登录（手机号即可）
2. 左侧「API keys」→「创建 API key」→ 命名（如 ischolar-course）
3. 复制形如 sk-xxxxxxxx 的字符串（只显示一次，务必立刻保存）
4. 「充值」页面按需充值（课程实操约 5–20 元足够）
```

> [!warning] Key 安全三条
> 1. **不要**把 Key 贴进微信群、论文、PPT、Git 仓库。
> 2. 本课程所有本地配置保存在 `ischolar/data/provider_settings.json`，该文件**不要提交、不要打包**。
> 3. 一旦怀疑泄露，立刻在平台「删除该 Key」并重建。

### 3.6 首次对话测试

```bash
hermes chat -q "用三句话说明你能帮文科老师做什么"
```

预期：返回一段中文说明，且**不是**“我无法访问文件系统”之类的拒答。

> [!tip] 如果报错
> - `command not found: hermes` → PATH 未生效，重开终端或 `source ~/.zshrc`
> - `401 Unauthorized` → Key 错误或未充值
> - `ECONNREFUSED` → 网络代理问题，检查是否设置了系统代理但终端未继承

---

## 🖥️ 四、iScholar 本地工作台（零命令行替代方案）

如果命令行让你紧张，课程提供了**双击即用**的图形工作台，功能覆盖 7 大科研智能体。

### 4.1 启动方式

| 系统 | 操作 |
| :-- | :-- |
| macOS | Finder 双击 `ischolar/启动iScholar.command` |
| Windows | 双击 `ischolar/启动iScholar.bat` |

启动器会自动：检测依赖 → 缺依赖则从清华镜像安装 → 拉起 FastAPI（`127.0.0.1:8765`）→ 拉起 Streamlit（`127.0.0.1:8501`）→ 自动打开浏览器。

### 4.2 填入秘钥

```text
左侧边栏 → 🔑 大模型与 API 秘钥设置
├── 选择模型服务商：DeepSeek / 通义千问 / Kimi / 智谱 / Ollama / 校内 L20 / 离线演示
├── 填入 API Key
├── 点击「🔌 测试连接」→ 看到「模型连接测试成功」即通
└── 点击「💾 保存配置」
```

> [!success] 没有 Key 也能上课
> 选择「**本地离线教学演示引擎**」，7 个智能体全部可跑，输出的是结构化教学示例（会明确标注“示例条目·请回源核验”）。适合课堂演示与首次体验。

### 4.3 与 Hermes 的分工

| 场景 | 用哪个 | 原因 |
| :-- | :-- | :-- |
| 第一次体验 7 大智能体 | iScholar | 图形界面，零配置 |
| 批量处理 Vault 里的 50 篇笔记 | Hermes | 能循环调用工具、写脚本 |
| 需要严格的过程留痕与人工关口 | iScholar | 内置复核状态与证据台账 |
| 复杂多步任务（检索→清洗→成稿） | Hermes + Skills | 可编排、可复用 |
| 课堂演示、无网络环境 | iScholar 离线引擎 | 不依赖外网 |

---

## ⚙️ 五、Profile 与配置文件

### 5.1 目录结构

```text
~/.hermes/
├── config.yaml              # 全局配置
├── skills/                  # 全局技能（跨 Profile 共享）
└── profiles/
    ├── default/
    │   ├── config.yaml
    │   ├── skills/
    │   ├── memories/
    │   └── cron/
    └── research/            # 本课新建
        ├── config.yaml
        └── skills/
```

### 5.2 一个可用的 `config.yaml` 示例

```yaml
name: "科研助手"
description: "面向外语、区域国别、旅游管理方向文科教师的科研 Agent"
model: "deepseek-chat"
temperature: 0.4

system_prompt: |
  你是高校文科教师的科研助手。你必须：
  1. 区分「已核实事实」与「模型推测」，后者必须显式标注；
  2. 不生成看起来真实但无法核验的文献条目；
  3. 所有引用提示用户回到知网（CNKI）、万方或原文数据库核实；
  4. 优先使用中文回答，术语保留英文原文。

skills:
  - obsidian-search
  - zotero-query
  - topic-scout
  - literature-review
  - paper-writer
  - rebuttal-helper

tools:
  - read_file
  - write_file
  - search_files
  - web_search
  - web_extract

providers:
  - name: deepseek
    type: openai-compatible
    base_url: "https://api.deepseek.com/v1"
    api_key: "${DEEPSEEK_API_KEY}"
    model: "deepseek-chat"
```

### 5.3 把 Key 放进环境变量（比写进配置更安全）

```bash
# macOS / Linux：写入 ~/.zshrc 或 ~/.bashrc
export DEEPSEEK_API_KEY="sk-你的key"

# 生效
source ~/.zshrc
```

Windows（PowerShell）：

```powershell
setx DEEPSEEK_API_KEY "sk-你的key"
```

### 5.4 常用命令速查

```bash
hermes profile list          # 查看所有 Profile
hermes profile create research
hermes profile use research
hermes chat                  # 进入交互对话
hermes chat -q "问题"        # 单次提问
hermes skills list           # 查看已加载技能
```

---

## 🧪 六、课堂实操与验收

### 6.1 任务卡

- [ ] 安装 Node.js，`node --version` 显示 v20+
- [ ] 安装 Hermes，`hermes --version` 有输出
- [ ] `hermes setup` 完成 DeepSeek Provider 配置
- [ ] 单次提问成功返回中文结果
- [ ] 启动 iScholar，测试连接成功（或选择离线引擎跑通 1 个智能体）
- [ ] 截图保存：终端返回结果 + iScholar 连接成功提示

> [!success] ✅ 本课验收标准
> 1. `hermes chat -q "你好"` 有正常中文回复；
> 2. iScholar 侧边栏显示「已配置」秘钥状态；
> 3. 能说清 Profile / Skills / Memory / Tools 四者的区别；
> 4. 知道自己的 Key 存在哪里、如何删除。

---

## ❓ 七、常见问题

> [!question] Q1：一定要用 DeepSeek 吗？
> 不必。通义千问（`qwen-plus`）、Kimi（长文档）、智谱 GLM 都可以，接口都是 OpenAI 兼容格式。选 DeepSeek 是因为便宜且中文科研场景表现稳定。

> [!question] Q2：Hermes 和 OpenCode 是什么关系？
> 两者都是 Agent 宿主（Harness）：Hermes 偏终端/多平台，OpenCode 偏代码与工程任务。课程中两者可并存，Skills 目录可共享（`~/.hermes/skills/` 与 `~/.dsh/skills/`）。

> [!question] Q3：安装报 `EACCES` 权限错误？
> 不要用 `sudo npm install -g`。改用 nvm 管理 Node，或 `npm config set prefix ~/.npm-global` 后把该目录加入 PATH。

> [!question] Q4：公司/学校网络装不上怎么办？
> 优先用国内镜像：`npm config set registry https://registry.npmmirror.com`；Hermes 也可用 `npm i -g hermes-agent --registry=...`。

> [!question] Q5：API 调用贵吗？
> `deepseek-chat` 价格约为每百万输入 token 一两元量级，一次课程实操通常几分钱到几毛钱。建议先充 20 元，够用很久。

> [!question] Q6：能不能完全离线？
> 可以，用 Ollama + Qwen2.5-7B（第 06 课），但推理质量低于云端大模型，适合处理敏感材料。

---

## 📎 八、本课交付物与衔接

| 交付物 | 位置 | 验收 |
| :-- | :-- | :-- |
| Hermes 可执行 | `which hermes` | 有路径输出 |
| DeepSeek Provider | `~/.hermes/profiles/research/config.yaml` | Key 通过环境变量注入 |
| iScholar 配置 | `ischolar/data/provider_settings.json` | 测试连接成功（该文件不入库） |
| 对话截图 | 个人课程档案 | 含时间与模型名 |

**下一课预告**：第 03 课把 Hermes 从“通用助手”改造成 6 个**科研专用 Agent**，并写你自己的第一个 Skill。

---

> [!quote] 本课一句话
> **模型决定上限，工具决定能不能落地；Hermes 的价值是让模型真正碰到你的文件。**
