---
name: paper-writer
description: "Use when user wants to write or revise a paper section. Supports modular writing with IMRaD structure, CARS introduction model, and three-tier polishing pipeline."
version: 1.0.0
author: AI4S Course
license: MIT
created: 2026-09-08
updated: 2026-09-08
type: 笔记
---

# Paper Writer Agent

Modular paper writing with AI assistance and three-tier polishing.

## Writing Order (Easiest to Hardest)

1. **Methods** — 照着研究设计写
2. **Results** — 照着数据写
3. **Literature Review** — 整理读书笔记
4. **Discussion** — 需要深度思考
5. **Introduction** — 提炼全文精华
6. **Conclusion** — 浓缩讨论
7. **Abstract** — 全文缩写
8. **Title** — 最后打磨

## CARS Introduction Model

### Move 1: Establish Territory
引用数据/现象说明话题重要性，综述已有研究的主要发现。

### Move 2: Establish Niche
"然而，已有研究较少关注……" / "目前尚不清楚……"

### Move 3: Occupy the Niche
"本研究旨在……" / "本研究的贡献在于……"

## Three-Tier Polishing Pipeline

### Tier 1: AI Initial Polish
- DeepSeek: 语法检查、逻辑一致性、学术用语
- Prompt: "请检查以下学术文本的语法错误、逻辑漏洞和不规范用语"

### Tier 2: Human Critical Review
- 检查学术判断是否准确
- 核实引用是否正确
- 确保原创贡献清晰

### Tier 3: Tool Final Check
- 秘塔写作猫：格式规范检查
- 火山写作：语言润色
- 知网查重：重复率检测

## Prompt Templates

### Abstract Generation

```
请为以下论文生成中英文摘要：

标题：[论文标题]
研究问题：[RQ]
方法：[方法描述]
核心发现：[3条主要发现]
结论：[一句话结论]

要求：
- 中文摘要200-300字，结构化（目的-方法-结果-结论）
- 英文摘要200-300词，对应翻译
- 关键词3-5个（中英文各一套）
```

### Section Writing

```
请帮我撰写论文的【方法/结果/讨论】部分。

研究信息：
- RQ：[研究问题]
- 方法：[方法描述]
- 数据：[数据情况]
- 发现：[主要发现]

要求：
- 学术文体，中文学术论文风格
- 字数约[X]字
- 按照【期刊名称】的格式要求
```

### Three-Tier Polish

```
Tier 1 Prompt:
请对以下学术论文段落进行语法和逻辑检查：
[粘贴文本]

请标注：
1. 语法错误（红色）
2. 逻辑漏洞（黄色）
3. 不规范用语（蓝色）
4. 修改建议
```

## AI Usage Declaration Template

```
本研究在文献检索和摘要整理阶段使用了DeepSeek AI辅助工具。
所有AI生成内容均经作者逐一核实与修改。
本研究遵循[期刊名]的AI使用政策。
```

## Output Location

Drafts are saved to: `05-写作草稿/` with appropriate version tags
