---
name: zotero-query
description: "Use when user wants to search their Zotero library, generate literature cards, or manage references. Requires Zotero Integration plugin in Obsidian."
version: 1.0.0
author: AI4S Course
license: MIT
created: 2026-09-08
updated: 2026-09-08
type: 笔记
---

# Zotero Query

Search and manage references from Zotero library, integrated with Obsidian.

## Prerequisites

- Zotero 7 installed
- Better BibTeX plugin installed
- Obsidian Zotero Integration plugin configured

## Workflow

### 1. Search Zotero

```bash
# Search by title/author/keyword in Zotero exports
# Zotero data is synced to Obsidian via Zotero Integration plugin
grep -r "关键词" ~/Obsidian/科研Vault/02-文献库/ --include="*.md"
```

### 2. Generate Literature Card

When user provides a paper title or DOI:

1. Search existing notes in `02-文献库/`
2. If not found, create new note using `文献笔记模板`
3. Fill in basic info from user-provided data
4. Use DeepSeek/Kimi to extract key information from PDF

### 3. Batch Import

```bash
# Import multiple references
# 1. Export from Zotero as CSV/RIS
# 2. Parse and create individual notes
# 3. File into appropriate folder
```

## Citation Key Format

Better BibTeX citation key: `author_year_title`

Example: `smith_2024_ai_feedback`

## Prompt Templates

### Literature Card Generation

```
请阅读以下学术论文，提取关键信息：
[粘贴论文内容或上传PDF]

请按以下结构输出：
1. 研究问题（一句话）
2. 理论框架
3. 研究方法
4. 核心发现（3条）
5. 研究局限
6. 与我研究的关联
```

### Cross-Paper Comparison

```
请对比以下两篇论文的研究方法和发现：
论文A：[粘贴摘要]
论文B：[粘贴摘要]

请用表格对比：
- 研究问题
- 方法
- 样本量
- 核心发现
- 局限性
```
