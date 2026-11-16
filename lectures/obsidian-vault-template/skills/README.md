---
title: Hermes科研技能库
type: skills-index
updated: 2026-11-15
created: 2026-09-17
---

# 🛠️ Hermes科研技能库

为Hermes Agent编写的科研专用Skills。

## 已开发技能

| Skill | 用途 | 文件 |
| :-- |:--| :-- |
| `obsidian-search` | 搜索Obsidian笔记 | `obsidian-search/SKILL.md` |
| `zotero-query` | 查询Zotero文献库 | `zotero-query/SKILL.md` |
| `topic-scout` | 选题发现、空白核验与FINER评估 | `topic-scout/SKILL.md` |
| `literature-review` | 文献综述生成 | `literature-review/SKILL.md` |
| `paper-writer` | 论文模块化写作 | `paper-writer/SKILL.md` |
| `rebuttal-helper` | 审稿意见回复 | `rebuttal-helper/SKILL.md` |

## Skill编写规范

每个Skill包含一个 `SKILL.md` 文件，格式如下：

```yaml
---
name: skill-name
description: "Use when <触发条件>. <一句话行为描述>."
version: 1.0.0
---
# Skill名称
## 使用场景
## 操作步骤
## 提示词模板
## 注意事项
```

## 快速创建新Skill

告诉Hermes Agent：

> "请为我创建一个名为 xxx 的Skill，功能是..."

Agent会自动在 `skills/` 目录下创建SKILL.md文件。

---

*Skills是Hermes的核心能力扩展机制，每次使用后可迭代优化*
