---
name: literature-review
description: "Use when user wants to generate a literature review section, synthesize multiple papers, or identify research gaps. Outputs structured review paragraphs."
version: 1.0.0
author: AI4S Course
license: MIT
created: 2026-09-17
updated: 2026-09-17
type: 笔记
---

# Literature Review Agent

Generate structured literature reviews using OCAR model and funnel structure.

## Models

### OCAR Model (English Papers)

| Step | Meaning | Function |
| :-- |:--| :-- |
| O - Overview | 概述研究领域现状 | 为读者建立背景认知 |
| C - Contributions | 指出关键文献贡献 | 综合多篇文献的核心发现 |
| A - Arguments | 讨论学术争议点 | 呈现不同观点与矛盾 |
| R - Research Gap | 指出现有研究空白 | 为你的研究提供合理性 |

### Funnel Structure (Chinese Papers)

```
🌍 宏观背景（领域整体研究现状）
    ↓
📚 主题梳理（按2-3个子主题分类述评）
    ↓
⚡ 争议与空白（学界分歧与未解决问题）
    ↓
🎯 本研究定位（如何填补空白）
```

## Prompt Templates

### Framework Generation

```
我正在写一篇关于【研究主题】的文献综述，已经阅读了以下文献：
[粘贴文献卡片摘要]

请帮我：
1. 将这些文献按主题分为2-3个子主题，每个子主题拟一个小标题
2. 在每个子主题下，指出学界的共识和分歧
3. 在最后一段指出当前研究的空白/不足
4. 说明本研究如何填补这个空白

请使用学术文体，引用格式为"作者（年份）"。
```

### Paragraph Generation

```
You are a senior researcher in [field]. Based on the following literature
summaries, write a literature review paragraph (about 200 words) on [sub-topic].

Requirements:
1. Start with a topic sentence that states the main argument
2. Synthesize (not list) findings from multiple studies
3. Highlight agreements and disagreements
4. End with a clear research gap statement
5. Use APA 7th citation format

[Paste literature summaries]
```

### Gap Analysis

```
基于以下文献，分析当前研究的空白：
[粘贴文献列表]

请从以下角度分析：
1. 方法论空白（哪些方法未被使用？）
2. 语境空白（哪些情境未被研究？）
3. 理论空白（哪些理论关系未被验证？）
4. 时间空白（哪些最新发展未被关注？）
```

## Output Location

Review drafts are saved to: `05-写作草稿/` with tag `#文献综述`

## Quality Checklist

- [ ] 每条引用都有实际阅读过的文献支撑
- [ ] 综述逻辑是"综合"而非"罗列"
- [ ] 明确指出了研究空白
- [ ] 本研究的定位清晰
- [ ] 引用格式统一
