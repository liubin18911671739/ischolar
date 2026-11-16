# 贡献指南

感谢你关注 iScholar！欢迎通过 Issue 反馈问题、通过 Pull Request 提交改进。

## 提交 Issue

- **Bug 报告**：请说明操作系统、Python/Node 版本、复现步骤、预期结果与实际结果，并附上相关日志（注意删除 API Key、个人路径与隐私信息）。
- **功能建议**：请说明使用场景与目标用户，最好给出可验收的完成标准。
- **内容纠错**：讲义中的事实、引文、链接或软件版本如有错误，请标注文件路径与行号。

## 提交 Pull Request

1. Fork 本仓库并从 `main` 创建分支：`feat/xxx`、`fix/xxx`、`docs/xxx`；
2. 保持改动聚焦，一次 PR 只解决一个问题；
3. 代码风格与现有实现保持一致；
4. 提交前运行本地检查：

```bash
./scripts/check-all.sh          # ischolar pytest + website check/build
# 或分别运行
cd ischolar && python -m pytest tests -q
cd website && npm ci && npm run check && npm run build
```

5. 在 PR 描述中说明改动内容、验证方式与影响范围。

## 内容贡献

- 讲义与文档使用简体中文，结构参考现有课次的属性卡、Callout 与验收清单；
- 引用数据、法规、论文与软件版本时请给出可回溯来源；
- 不提交受版权限制的教材、扫描件或未授权图片；
- 新增案例请先脱敏（人名、校名、地名、项目编号）。

## 安全与隐私

- **切勿提交** `ischolar/data/provider_settings.json`、`.env`、API Key、个人数据库或未脱敏的访谈材料；
- 如发现安全漏洞，请通过仓库 Issues 中的私下联系方式告知维护者，不要公开披露可利用细节。

## 许可

提交贡献即表示你同意：

- 代码贡献按 [MIT](LICENSE) 许可；
- 课程内容贡献按 [CC BY-NC-SA 4.0](LICENSE-CONTENT) 许可。
