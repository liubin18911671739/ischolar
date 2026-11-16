---
name: obsidian-search
description: "Use when user wants to search, create, or update notes in the Obsidian vault. Searches by content, tags, or filename."
version: 1.0.0
author: AI4S Course
license: MIT
created: 2026-09-08
updated: 2026-09-08
type: 笔记
---

# Obsidian Search

Search, create, and update notes in the Obsidian Vault.

## Vault Location

Default vault: `~/Obsidian/科研Vault/`

## Operations

### Search Notes

```bash
# Search by content
grep -r "关键词" ~/Obsidian/科研Vault/ --include="*.md"

# Search by filename
find ~/Obsidian/科研Vault/ -name "*.md" | grep "关键词"

# Search by tag
grep -r "tags:.*文献笔记" ~/Obsidian/科研Vault/ --include="*.md"
```

### Create Note

Use `write_file` tool to create a new note with YAML frontmatter.

### Update Note

Use `patch` tool to update specific sections of an existing note.

## File Structure

```
科研Vault/
├── 00-收件箱/          # Quick capture
├── 01-选题池/          # Topic evaluation
├── 02-文献库/          # Literature notes
├── 03-研究设计/        # Research design
├── 04-数据与分析/      # Data & analysis
├── 05-写作草稿/        # Paper drafts
├── 06-投稿管理/        # Submission management
├── 07-课题档案/        # Project archives
├── 08-知识卡片/        # Knowledge cards (Zettelkasten)
├── templates/          # Note templates
├── skills/             # Hermes skills
└── daily/              # Daily logs
```

## Templates Available

- `templates/文献笔记模板.md` - Literature note
- `templates/选题评估模板.md` - Topic evaluation
- `templates/研究设计一页纸模板.md` - Research design one-pager
- `templates/论文草稿模板.md` - Paper draft
- `templates/每日科研日志模板.md` - Daily research log

## Usage Examples

```
User: 帮我搜索Obsidian中关于"翻译学习"的文献笔记
Agent: grep -r "翻译学习" ~/Obsidian/科研Vault/02-文献库/ --include="*.md" -l

User: 创建一条新的文献笔记
Agent: 使用 write_file 创建到 02-文献库/未分类/ 目录，套用文献笔记模板

User: 查看今天写了什么
Agent: 读取 daily/ 目录下今天的日志文件
```
