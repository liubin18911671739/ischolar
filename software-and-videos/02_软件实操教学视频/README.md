# 软件实操教学视频（14 部）· 状态与录制指引

> 位置：`software-and-videos/02_软件实操教学视频/`
> 网盘：`/apps/bypy/iScholar课程/软件与视频工具箱/02_软件实操教学视频/`

## 一、视频状态总表

| 编号 | 视频 | 类型 | 时长 | 对应课次 |
| :-- | :-- | :-- | :--: | :-- |
| 01 | iScholar本地工作台_双击启动与DeepSeek秘钥配置 | ⏳ 步骤卡（3 页翻页幻灯） | 15 秒 | 02、10 |
| 02 | Obsidian科研Vault与Hermes智能体配置 | ⏳ 步骤卡（2 页翻页幻灯） | 10 秒 | 01、02、03 |
| 03 | Zotero7与Obsidian文献矩阵联动 | ⏳ 步骤卡（翻页幻灯） | 5 秒 | 04 |
| 04 | Ollama本地大模型与jamovi_AntConc数据分析 | ⏳ 步骤卡（翻页幻灯） | 5 秒 | 06、07 |
| 05 | VSCode_Anaconda环境配置与Hermes终端论文项目实战 | ✅ 实操录屏 | 2 分 19 秒 | 01、02、07、08 |
| 06 | Mermaid_Drawio_Excalidraw与OpenCode技术路线图绘制 | ✅ 实操录屏 | 1 分 24 秒 | 03、05 |
| 07 | Unpaywall插件与CORE_PMC开放获取全文免费下载教程 | ✅ 实操录屏 | 1 分 26 秒 | 04 |
| 08 | Taguette开源质性研究访谈文本编码工具实操 | ✅ 实操录屏 | 50 秒 | 05 |
| 09 | 见数_问卷星调研设计与SPSSAU_SPSSPRO零代码统计分析 | ✅ 实操录屏 | 1 分 04 秒 | 05、07 |
| 10 | AntConc语料库下载安装与KWIC_词簇_共现检索实战 | ✅ 实操录屏 | 1 分 39 秒 | 04、07 |
| 11 | Ollama本地部署与魔搭ModelScope_HuggingFace模型数据集下载 | ✅ 实操录屏 | 1 分 12 秒 | 06 |
| 12 | jamovi_JASP_PSPP三大开源免费统计软件下载与对比 | ✅ 实操录屏 | 54 秒 | 07 |
| 13 | Paperpal_QuillBot_Writefull学术润色与PaperPass查重降AIGC | ✅ 实操录屏 | 1 分 20 秒 | 08 |
| 14 | 讯飞智文_豆包与WPS_AI学术汇报PPT生成与美化实战 | ✅ 实操录屏 | 1 分 04 秒 | 09、10 |

> **⏳ 步骤卡说明**：01–04 是静态步骤概览幻灯（5–15 秒自动翻页，含"第 N/M 页"页码），用于课前快速预习操作流程，**不是完整实操录屏**。05–14 为真实屏幕录制。
> 01–04 补录完整版后，**同名替换**本目录文件即可，随后执行同步（见第四节）。

## 一之二、隐私与脱敏说明

本仓库不分发 MP4 视频。现有 14 部视频在开源审核中发现浏览器标签、账号信息、个人路径等隐私元素，正在重录或打码处理；完成前不会上传至 GitHub Releases。开源版请优先使用课程脚本与文档自行录制，或关注后续发布公告。

**录制红线**：

- 使用干净的浏览器用户配置，关闭书签栏与同步；
- 隐藏操作系统用户名、邮箱、手机号与聊天窗口；
- 演示数据使用虚构项目与人名；
- 上传前用 `ffmpeg` 抽帧 + OCR 做一次自检。

## 二、01–04 分步录制脚本（供讲师补录完整版）

统一规范：1920×1080、普通话讲解、每集 2–5 分钟、开头 3 秒显示课程标题卡、结尾显示"iScholar · AI 科研与教学实训课程配套视频"。

### ⏳ 01 · iScholar 本地工作台：双击启动与 DeepSeek 秘钥配置（目标 3 分钟）

1. 展示解压后的 `iScholar_v6.2_本地双击即用版` 目录，指认 `启动iScholar.command`（macOS）/ `启动iScholar.bat`（Windows）。
2. 双击启动，展示首次运行自动创建环境（终端滚动安装提示），强调"无需手动配依赖"。
3. 浏览器自动打开 `http://127.0.0.1:8501`，介绍左侧边栏三大区：大模型秘钥设置、项目列表、导出。
4. 展开【大模型与 API 秘钥设置】→ 选择 DeepSeek 官方 API → 粘贴个人 Key → 点【保存配置】【测试连接】→ 展示成功提示（Key 掩码显示）。
5. 演示无 Key / 断网时的【离线教学演示引擎】兜底，跑一次 TopicScout 选题侦察。
6. 收尾：展示一键导出到 Obsidian Vault 的入口（详细见视频 02）。

### ⏳ 02 · Obsidian 科研 Vault 与 Hermes 智能体配置（目标 3 分钟）

1. 打开 Obsidian →【Open folder as vault】加载课程标准 Vault 模板（`lectures/obsidian-vault-template/`）。
2. 介绍三分区结构：`01-原始资料_只读`、`02-工作区_Agent草稿`、`03-已复核成果`（+ `04_证据与来源台账`）。
3. 启用插件：Templater、Dataview、Zotero Integration 与 Hermes Console。
4. 打开终端，演示 Hermes Agent 三种形态：Hermes CLI、OpenCode、DeepSeek Harness（DSH Desktop）。
5. 加载 6 大科研技能（`obsidian-search` / `zotero-query` / `literature-review` / `topic-scout` / `paper-writer` / `rebuttal-helper`），展示 `skills/README.md`。
6. 在 Obsidian 中选中文本作为上下文发送给 Hermes 分析；强调"只读原始文献、覆盖写入需教师确认"。
7. 回到 iScholar 点【一键导出当前项目至 Obsidian Vault】，展示生成的标准 Markdown 台账与自动备份。

### ⏳ 03 · Zotero 7 与 Obsidian 文献矩阵联动（目标 4 分钟）

1. 知网（CNKI）高级检索 → 导出 Refworks 格式题录 → 导入 Zotero 7。
2. 安装并配置 Better BibTeX，生成唯一 Citation Key。
3. Obsidian 安装 Zotero Integration 插件，配置数据库路径与输出模板，一键导入结构化文献笔记。
4. 演示文献矩阵笔记的字段（作者/年份/方法/结论/证据页码）与 Dataview 汇总表。
5. 结合 CiteSpace 生成关键词共现图谱，回填到综述笔记。
6. 收尾：在 iScholar 中演示 LitReview 智能体如何消费该矩阵生成漏斗式综述。

### ⏳ 04 · Ollama 本地大模型与 jamovi / AntConc 数据分析（目标 4 分钟）

1. 下载安装 Ollama，`ollama pull qwen2.5` 拉取国产开源模型，`ollama run` 验证。
2. 在 iScholar 秘钥设置中选择"本地 Ollama"端点，测试连接成功。
3. jamovi 打开示例数据：描述统计、T 检验、回归，导出 APA 格式表格。
4. AntConc 导入课程语料：KWIC 检索、词簇（N-gram）、共现分析、关键词表。
5. 讲解三者分工：本地模型（私密草稿）+ jamovi（统计）+ AntConc（语料证据），全程数据不出本机。

## 三、录屏工具建议（国产 / 开源）

- 录屏：OBS Studio（开源免费，跨平台）或 Windows 自带 Xbox Game Bar、macOS `Cmd+Shift+5`。
- 剪辑：剪映（国产）或 Kdenlive / Shotcut（开源）。
- 字幕：剪映自动字幕识别后人工校对专有名词（iScholar、Obsidian、Zotero 等）。

## 四、替换与同步

```bash
# 1) 同名替换本目录中的 mp4（保持编号与文件名不变）
# 2) 更新根 README / 总纲 / 软件清单中的时长标注（如实测时长变化）
# 3) 重新打包并同步网盘（4 个 zip + 软件清单 + 校验清单）
cd <仓库根目录>
./scripts/package-and-sync.sh --sync

# 4) 单独补传视频（视频体积大，不走脚本，逐个上传）
cd software-and-videos
python3 -m bypy upload "02_软件实操教学视频/<新视频>.mp4" "iScholar课程/软件与视频工具箱/02_软件实操教学视频/"
```
