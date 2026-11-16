# Vercel 部署说明

本工程已按 Next.js 默认构建方式准备；本次交付不包含实际线上部署，也未创建或推送远程仓库。

## 部署前

1. 确认公开内容、案例和联系方式可以发布，网站的非官方授权说明继续保留。
2. 本地运行 `npm ci`、`npm run check`、`npm run build` 和浏览器测试。
3. 按需将项目提交到自己的 Git 仓库。不要提交 `.env*`、密钥、浏览器 JSON 备份或校内受限材料。

## 导入 Vercel

在 Vercel 选择 **Add New → Project → Import Git Repository**，导入项目仓库：

| 配置 | 值 |
| --- | --- |
| Framework Preset | Next.js（自动识别） |
| Root Directory | 独立仓库为仓库根；如放入大仓库，选择本工程所在目录 |
| Node.js | 22.x 推荐；工程亦允许兼容的 24.x |
| Install Command | 默认 npm 安装；锁文件已提供 |
| Build Command | `npm run build` |
| Output Directory | 保留 Next.js 默认值，不改成 `out` |
| Environment Variables | 无需配置 |

点击 Deploy 后检查构建日志，再打开预览网址。无需 `vercel.json`、数据库、模型服务、服务器密钥或 Serverless API。默认 Next.js 服务静态预渲染页面即可。

官方入口：[Next.js on Vercel](https://vercel.com/docs/frameworks/full-stack/nextjs)。

## 预览检查与发布

- 打开首页、日历、16 个课程详情、资源中心和关于页，检查移动端导航。
- 确认课时为 32h，科研 18h / 教学 12h / 办公综合 2h，且不展示未确认的具体日期或模型性能。
- 操作筛选、模板下载、复制、笔记保存、导出与清除。
- 检查打印和 404，确认没有被加入追踪脚本或远程字体。
- 联系方式若尚未配置，应继续显示占位说明。

Vercel 与自定义域名、不同浏览器的 localStorage 相互隔离；预览网址里的笔记不会自动迁移到正式域名。切换域名前请导出备份。托管平台可能保留普通访问日志，本站不提供用户输入的接收或上传接口。

## 待校方确认

校内模型平台、模型版本、API 与条款；L20 实际规格、驱动、共享配额和运维；课程日期、账号与教室；素材、肖像/声音授权和发布流程。确认前不应将相应状态改为已批准或已实测。
