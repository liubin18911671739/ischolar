---
title: 第01课｜Obsidian 科研 Vault 搭建
type: lesson
course: AI4S · 高校教师科研与教学 AI 实训
lesson: "01 / 10"
duration: 90 分钟（理论 30 + 实操 60）
difficulty: 入门 · 零代码
progress: "▰▱▱▱▱▱▱▱▱▱ 10%"
tools:
  - Obsidian
  - VS Code
  - Templater
  - Dataview
  - Calendar
  - Zotero Integration
  - Copilot
  - Hermes Console
deliverables:
  - 个人科研 Vault 目录结构（12 个文件夹）
  - 6 个核心插件可正常启用
  - 1 篇标准化文献笔记
videos:
  - 02_Obsidian科研Vault与Hermes智能体配置教程.mp4
  - 05_VSCode_Anaconda环境配置与Hermes终端论文项目实战.mp4
tags: [AI4S, Obsidian, 知识管理, 课程教案]
created: 2026-09-17
updated: 2026-11-15
---

# 第01课｜Obsidian 科研 Vault 搭建

> [!abstract] 🎯 本课定位
> 这是整套课程的**地基课**。本课不写代码、不调模型，只做一件事：把散落在微信、桌面、U 盘里的科研资料，收进一个**本地优先、可检索、可复用**的 Obsidian 科研 Vault。
>
> **学完你将拥有**：一套 12 个文件夹的科研目录、6 个核心插件、1 篇标准化文献笔记，以及后续 9 节课反复使用的“科研中控台”。

> [!info] 📌 一句话原则
> **原始资料只读，工作稿可改，成果留痕。** 目录结构不是审美问题，而是为了防止“改着改着把原始材料覆盖了”。

---

## 🧰 一、本课软件工具箱（下载 · 安装 · 备份）

> [!tip] 所有软件均遵循「国产优先 / 开源免费 / 国内直连」原则，无需科学上网。

| 软件 / 插件 | 用途 | 官方下载 | 国内加速 / 镜像 | 百度网盘备份 |
| :-- | :-- | :-- | :-- | :-- |
| **Obsidian** | 本地 Markdown 知识库（本课核心） | <https://obsidian.md> | 官网国内可直连；macOS 可 `brew install --cask obsidian` | `/iScholar课程/软件与视频工具箱/01_国产与开源软件工具包/` |
| **VS Code** | 批量改 Markdown、看 Git 差异、跑 Hermes 终端 | <https://code.visualstudio.com> | 官网直连；macOS `brew install --cask visual-studio-code` | 同上 |
| **Templater** | 模板引擎（自动填日期、标题） | Obsidian 社区插件市场搜索 `Templater` | 社区市场国内可访问 | 插件配置文件见 Vault 模板包 |
| **Dataview** | 把笔记当数据库查询（文献清单、待办） | 社区插件市场搜索 `Dataview` | 同上 | 同上 |
| **Calendar** | 日历视图，配合每日科研日志 | 社区插件市场搜索 `Calendar` | 同上 | 同上 |
| **Zotero Integration** | 把 Zotero 题录一键拉进笔记 | 社区插件市场搜索 `Zotero Integration` | 同上 | 同上 |
| **Copilot** | Obsidian 内 AI 对话（可选） | 社区插件市场搜索 `Copilot` | 同上 | 同上 |
| **Hermes Console** | Obsidian 内的 Agent 终端（可选） | 社区插件市场搜索 `Hermes` | 同上 | 同上 |
| **课程 Vault 模板** | 目录 + 模板 + 6 个 Hermes Skills | 本地 `lectures/obsidian-vault-template/` | — | `Obsidian_科研Vault标准模板与Hermes技能包.zip` |

> [!example] 🎬 配套实操视频
> - **`02_Obsidian科研Vault与Hermes智能体配置教程.mp4`**（3 分 20 秒）：从零安装 Obsidian → 建 Vault → 装插件 → 接 Hermes。
> - **`05_VSCode_Anaconda环境配置与Hermes终端论文项目实战.mp4`**（2 分 19 秒）：VS Code 安装、插件配置、在终端里用 Hermes 操作论文项目文件夹。
>
> 观看顺序建议：先看 02 建库，再看 05 配编辑器。视频在 `software-and-videos/02_软件实操教学视频/`，网盘同路径。

---

## 一、Obsidian 是什么：把知识存成自己的文件

Obsidian 是一款**本地优先、以 Markdown 为底层格式**的知识管理工具。所有笔记都是硬盘上的 `.md` 纯文本文件，不依赖任何云服务；删掉软件，笔记依然在。

> [!info] 为什么文科科研特别适合
> 1. **数据主权**：访谈录音转写稿、未发表数据、学生作文，全部留在本机。
> 2. **双向链接**：`[[作者2024]]` 一写，文献网络自动长出来，写综述时能看见“谁和谁在对话”。
> 3. **纯文本长寿**：20 年后 Word 可能打不开，`.md` 永远能读。
> 4. **可版本管理**：配合 Git，每次修改都有记录，改坏了能回滚。

### 1.1 本地工作流 vs 云端笔记软件

| 维度 | Obsidian + Hermes 本地工作流 | 传统云端笔记软件 |
| :-- | :-- | :-- |
| 数据存储 | 本机 Markdown 文件，可自行备份 | 第三方云数据库 |
| 隐私边界 | 资料不出本机（除非你主动调用 API） | 内容存放在服务商服务器 |
| 断网可用 | 完全可用 | 多数功能依赖网络 |
| 费用 | 软件免费，插件免费 | 个人版免费，协作/高级功能收费 |
| 扩展性 | 1000+ 社区插件 + 本地脚本 | 集成能力受平台限制 |
| AI 集成 | 本地 Agent 读写文件，过程可留痕 | 平台内置 AI，数据边界不透明 |

> [!warning] 别把“本地”当成“自动安全”
> 本地只代表**数据不主动上传**。一旦你把整篇未发表论文粘进云端模型对话框，数据就已经出境了。三级数据边界见第 06 课。

---

## 🛠️ 二、安装与建库

### 2.1 安装 Obsidian

1. 打开 <https://obsidian.md> → **Get Obsidian** → 选择 macOS / Windows / Linux。
2. macOS 也可用 Homebrew：`brew install --cask obsidian`。
3. 安装后首次启动，选择语言为**简体中文**。

### 2.2 创建第一个 Vault

**Vault = 一个普通文件夹**，Obsidian 只是给它加了一层索引和界面。

```text
操作：Obsidian 启动页 → Open folder as vault → 新建文件夹 → 选择 → Trust
```

推荐路径（与课程模板一致）：

```text
~/Obsidian/科研Vault/
```

> [!tip] 路径三条铁律
> 1. **不要放在 iCloud / OneDrive 同步盘**：同步冲突会产生 `xxx (conflicted copy).md`，非常难清理。需要同步请用 Git 或手动备份。
> 2. **路径不要含特殊符号**：空格可用，`#`、`?`、`%` 会出问题。
> 3. **一个课题一个 Vault 或一个大 Vault 分文件夹**：课程推荐后者，方便跨课题复用文献。

### 2.3 直接用课程模板起步（推荐）

不想从零建目录，可解压课程模板包，用 Obsidian 打开其中的 `obsidian-vault-template/`：

```bash
# 仓库内直接打开
open -a Obsidian "lectures/obsidian-vault-template"   # 在仓库根目录执行
```

模板内含：5 份笔记模板（选题评估 / 文献笔记 / 研究设计一页纸 / 论文草稿 / 每日科研日志）+ 6 个 Hermes Skills。

---

## 🏗️ 三、科研 Vault 目录结构

### 3.1 标准结构（12 个文件夹）

```text
📁 科研Vault/
├── 📁 00-收件箱/          # 新想法、临时材料，周末清空
├── 📁 01-选题池/          # 候选选题、选题评估报告
├── 📁 02-文献库/          # 按课题组织的文献笔记
│   ├── 📁 01-课题A/
│   ├── 📁 02-课题B/
│   └── 📁 未分类/
├── 📁 03-研究设计/        # 研究设计一页纸、技术路线图、伦理材料
├── 📁 04-数据与分析/      # 原始数据（只读）、清洗脚本、分析结果
├── 📁 05-写作草稿/        # 论文各版本、章节草稿
├── 📁 06-投稿管理/        # 期刊匹配表、Cover Letter、审稿意见
├── 📁 07-课题档案/        # 国社科/教育部课题申报与结项材料
├── 📁 08-知识卡片/        # 碎片化知识、概念卡（Zettelkasten）
├── 📁 templates/          # 5 份标准模板
├── 📁 skills/             # Hermes 技能库（6 个 SKILL.md）
└── 📁 daily/              # 每日科研日志
```

### 3.2 设计原则：为什么这样分

| 原则 | 具体做法 | 解决什么问题 |
| :-- | :-- | :-- |
| 数字前缀 | `00`→`08` 按科研流程排序 | 侧边栏永远按流程走，不靠记忆 |
| 收件箱模式 | 一切新东西先扔 `00-收件箱` | 避免“边读边整理”打断阅读 |
| 课题隔离 | 文献库按课题分子文件夹 | 写综述时不会混入别的课题 |
| 只读区隔离 | 原始数据、访谈转写放 `04` 并标注只读 | 防止误覆盖原始材料 |
| 模板独立 | 所有模板放 `templates/` | 换课题也能复用 |
| 日志闭环 | `daily/` 每日一页 | 研究进展可追溯，写结项报告有据可查 |

> [!warning] 最常见的三个翻车现场
> 1. **原始访谈稿直接改**：改完就再也回不到原始表述。→ 原始稿另存 `_原始.md`，分析稿另建文件。
> 2. **文献笔记和 PDF 混在一起**：PDF 二进制文件会拖慢索引。→ PDF 放外部 `附件/`，笔记里用链接。
> 3. **所有东西堆根目录**：两个月后自己都找不到。→ 先建结构，再开始记。

### 3.3 课堂练习：搭出你的 Vault

- [ ] 创建 Vault 并命名（建议 `科研Vault`）
- [ ] 按上表建齐 12 个文件夹
- [ ] 在每个空文件夹放一个 `.gitkeep`（便于将来 Git 跟踪）
- [ ] 截图存档，作为本课交付物

---

## 🔌 四、六大核心插件配置

### 4.1 安装插件的通用步骤

```text
设置（齿轮）→ 第三方插件（社区插件）→ 关闭安全模式 → 浏览 → 搜索插件名 → 安装 → 启用
```

> [!tip] 插件不是越多越好
> 每装一个插件都会拖慢启动、增加冲突概率。本课只装 6 个，够用一学期。后续按需再加。

### 4.2 六个插件逐一配置

#### ① Templater（模板引擎）

- **作用**：插入模板时自动填日期、标题、文件名。
- **配置**：设置 → Templater → Template folder location → `templates`
- **使用**：`Cmd/Ctrl + P` → `Templater: Insert template` → 选模板
- **课堂验证**：用 `选题评估模板.md` 新建一条，确认 `{{date}}` 被替换成当天日期。

#### ② Dataview（把笔记当数据库）

- **作用**：自动生成文献清单、待办列表、投稿进度表。
- **示例**（放进任意笔记的代码块，语言选 `dataview`）：

```dataview
TABLE status, priority, created
FROM "01-选题池"
SORT created DESC
```

- **课堂验证**：在 `01-选题池/` 建 2 条带 `status` 属性的笔记，看表格是否自动出现 2 行。

#### ③ Calendar（日历视图）

- **作用**：右侧日历面板，点日期直接打开 `daily/YYYY-MM-DD.md`。
- **配置**：设置 → Calendar → Daily notes folder → `daily`；日期格式 `YYYY-MM-DD`。
- **课堂验证**：点今天日期，自动创建今日日志。

#### ④ Zotero Integration（文献直连）

- **作用**：在 Obsidian 里搜索 Zotero 条目，一键生成带元数据的文献笔记。
- **前置**：需先安装 Zotero 7 + Better BibTeX（第 04 课详解）。
- **配置**：设置 → Zotero Integration → 填写 Zotero 数据库路径 / Better BibTeX 端口。
- **课堂验证**：插入 1 条 Zotero 文献，检查标题、作者、年份、DOI 是否完整。

#### ⑤ Copilot（Obsidian 内 AI 对话，可选）

- **作用**：在笔记侧边栏直接对话，不用切浏览器。
- **配置**：填入 DeepSeek 或通义千问的 OpenAI 兼容接口地址与 Key。
- **注意**：它会把当前笔记内容作为上下文发给模型。**含敏感数据的笔记不要开 Copilot。**

#### ⑥ Hermes Console（Obsidian 内 Agent 终端，可选）

- **作用**：在 Obsidian 里唤起 Hermes Agent，让它直接读写 Vault 文件（搜笔记、批量改 frontmatter、按模板生成综述草稿）。
- **配置**：确认本机已安装 Hermes（第 02 课），在插件设置里指向 `hermes` 可执行文件路径。
- **课堂验证**：输入“列出 02-文献库 下最近 5 篇笔记的标题”，确认能返回真实文件列表。

> [!warning] 插件权限提醒
> Copilot、Hermes Console 这类插件拥有**读写你 Vault 的权限**。只从官方社区市场安装，不要手动拖入来源不明的插件包。

---

## 📝 五、第一篇标准化文献笔记

### 5.1 文献笔记的最小结构

一篇合格的文献笔记，至少回答四个问题：**它研究什么、怎么做的、发现了什么、对我有什么用**。

```markdown
---
title: "{{title}}"
authors: []
year:
venue:
doi:
type: literature-note
status: 待精读
tags: [文献笔记]
created: {{date}}
---

# {{title}}

## 1. 研究问题
>

## 2. 方法与数据
- 方法：
- 样本 / 语料：
- 分析工具：

## 3. 核心发现
1.
2.

## 4. 局限与争议
>

## 5. 与我的研究的关系
- 可引用到哪一章：
- 可借鉴的方法：
- 需要回源核验的点：
```

### 5.2 课堂练习

- [ ] 用 `templates/文献笔记模板.md` 新建 1 篇
- [ ] 选一篇你正在读的中文核心期刊论文填写
- [ ] 在 `## 5` 里写清“准备引用到引言还是讨论”
- [ ] 用 `[[ ]]` 链接到 `01-选题池` 里的某个选题

> [!success] ✅ 本课验收标准
> 1. Vault 目录 12 个文件夹齐全，截图可见；
> 2. 6 个插件状态为“已启用”，其中 Templater / Dataview / Calendar 完成一次实际验证；
> 3. 1 篇文献笔记字段完整，且与选题池建立了双向链接；
> 4. 能在 `daily/` 里写下今天的第一条科研日志。

---

## ❓ 六、常见问题

> [!question] Q1：Obsidian 免费吗？商用要付费吗？
> 个人使用免费。公司/机构内部商用需购买 Commercial 授权。高校教师个人科研与教学使用属个人使用范畴。

> [!question] Q2：能不能用 iCloud 同步？
> 技术上可以，但不推荐：iCloud 的按需下载会导致文件“本地不存在”，Obsidian 索引出错。推荐 Git（第 10 课）或手动定期备份。

> [!question] Q3：插件装完 Obsidian 变卡怎么办？
> 设置 → 第三方插件，逐个关闭排查；也可用“受限模式”启动。常见元凶是 Dataview 在大 Vault 上的全库查询。

> [!question] Q4：Vault 建错了能改路径吗？
> 可以。直接把整个文件夹移动到新位置，再用 Obsidian 重新 “Open folder as vault”。内部 `[[链接]]` 是相对路径，不受影响。

> [!question] Q5：我需要一开始就装 AI 插件吗？
> 不需要。先把目录和笔记规范跑顺，第 02 课配好 Hermes 后再接 AI，否则容易变成“用 AI 生成一堆找不到的笔记”。

---

## 📎 七、本课交付物与衔接

| 交付物 | 存放位置 | 验收方式 |
| :-- | :-- | :-- |
| Vault 目录结构 | `~/Obsidian/科研Vault/` | 截图 12 个文件夹 |
| 插件配置 | `.obsidian/plugins/` | 6 个插件处于启用状态 |
| 文献笔记 1 篇 | `02-文献库/未分类/` | frontmatter 完整、有双向链接 |
| 今日科研日志 | `daily/` | 至少 3 条记录 |

**下一课预告**：第 02 课安装 Hermes Agent，让这个 Vault 长出“会自己读文件、写文件”的手。

---

> [!quote] 本课一句话
> **先把资料收进一个自己能找回来的地方，再谈让 AI 帮你思考。**
