---
name: rebuttal-helper
description: "Use when user needs to respond to peer review comments. Categorizes review comments, generates Rebuttal Letter drafts, and applies three-color annotation method."
version: 1.0.0
author: AI4S Course
license: MIT
created: 2026-09-17
updated: 2026-09-17
type: 笔记
---

# Rebuttal Helper Agent

Systematic review response with three-color annotation and point-by-point templates.

## Six Types of Review Comments

| Type | Typical Phrasing | Severity | Strategy |
| :-- |:--| :-- |:--|
| ① Method | "样本量不足""缺少效度检验" | 🔴 High | Supplement data/analysis; acknowledge limitations |
| ② Theory | "理论框架薄弱""核心概念未界定" | 🔴 High | Strengthen literature review; clarify operationalization |
| ③ Literature | "缺少最新研究""遗漏关键文献" | 🟡 Medium | Add references; explain search strategy |
| ④ Writing | "The writing needs improvement" | 🟡 Medium | Rewrite + language polish |
| ⑤ Data | "数据不足以支持结论" | 🔴 High | Additional analysis; acknowledge limitations |
| ⑥ Novelty | "Incremental contribution" | 🔴 High | Clarify theoretical/practical novelty |

## Three-Color Annotation Method

- 🔴 **Red (Must Change)**: Method flaws, missing data, ethical issues
- 🟡 **Yellow (Negotiable)**: Theory depth, literature breadth, writing style
- 🟢 **Green (Just Explain)**: Minor clarifications, terminology, formatting

## Rebuttal Letter Template

```
Dear Editor and Reviewers,

We sincerely thank the editor and reviewers for their constructive comments,
which have significantly improved the quality of our manuscript. Below, we
respond to each comment point-by-point. Reviewer comments are shown in
**bold**, and our responses are in regular text. Changes in the manuscript
are highlighted in [color] in the revised manuscript.

---

**[Reviewer Comment 1]**
[Original comment]

**Response:**
We appreciate this insightful comment. [Your detailed response]

[Describe specific changes made, with page/line numbers in revised manuscript]

---

**[Reviewer Comment 2]**
...

---

We believe these revisions have substantially strengthened the manuscript.
We are happy to make further adjustments if needed.

Sincerely,
[Author Names]
```

## Point-by-Point Response Format

For each comment:
1. **Acknowledge** — Thank the reviewer
2. **Summarize** — Restate the concern briefly
3. **Respond** — Address the point directly
4. **Evidence** — Point to specific changes (page/line numbers)
5. **Closing** — Confirm the change is made

## AI Prompt for Rebuttal

```
请帮我回复以下审稿意见：

审稿意见：[粘贴审稿意见]

我的论文信息：
- 标题：[标题]
- 方法：[方法]
- 主要发现：[发现]

请按照以下格式回复：
1. 感谢审稿人的建议
2. 简要复述问题
3. 详细回复（解释/修改/补充）
4. 指出修改稿中的具体位置

语气要求：专业、谦逊、有理有据
```

## Quality Checklist

- [ ] 每条审稿意见都有回复
- [ ] 回复语气专业且谦逊
- [ ] 修改内容有具体页码/行号引用
- [ ] 方法论问题有实质性回应（不仅是文字修改）
- [ ] Rebuttal Letter格式规范
- [ ] 修改稿中有清晰的修改标记

## Output Location

Rebuttal drafts are saved to: `06-投稿管理/` with the journal name
