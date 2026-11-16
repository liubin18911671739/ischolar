# 开发依赖安全例外

复核日期：2026-10-19  
复核期限：2027-01-19，或上游发布修复版本时（以先到者为准）

## 当前例外

完整 `npm audit` 报告 5 项 high 告警，均来自仅在开发/检查阶段使用的依赖链：

`eslint-config-next@16.4.2 → @next/eslint-plugin-next@16.4.2 → fast-glob@3.3.1 → micromatch@4.0.8 → braces@3.0.3`

GitHub Advisory GHSA-vfj7-8cjw-p6xm 将 `braces` 3.0.3 及更早版本列为受影响版本，当前没有修复版本。npm 提议的强制自动修复会将 Next ESLint 配置降至不兼容的主版本，因此不采用。`npm audit --omit=dev --audit-level=high` 通过，生产依赖目前无 high 或更高等级告警。

## 处理要求

- 保持依赖锁文件，不使用 `npm audit fix --force` 或手工覆盖版本来掩盖告警。
- 每季度及 Next/ESLint 工具链升级时复查上游 Advisory 与 `npm audit`。
- 上游修复发布后，升级兼容工具链并运行 `npm run check`、`npm run build` 和 `npm run test:e2e`，再关闭本例外。
- 若告警范围或生产依赖路径改变，立即更新本记录并重新评估发布风险。
