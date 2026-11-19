# 工程验证记录

日期：2026-10-19。范围为本地工程、Playwright 多引擎自动化与自动无障碍扫描，不代表校方验收、线上部署验收或完整 WCAG 认证。

## 环境与构建

- Node.js 22.20.0，npm 11.7.0。
- Next.js 16.4.2、React 19.3.0，已提供 npm 锁文件。
- `npm run lint`：通过。
- `npm run typecheck`：通过。
- `npm run test:content`：通过，16 次课、32 小时、18 份模板、5 个专题，课程及资源关联均完整。
- `npm run build`：通过，课程与专题均静态预渲染；没有模型代理、上传接口或用户数据接收 API。
- 最新复核：`npm run check` 与 `npm run build` 均通过。
- 内容检查已纳入 `prebuild`，后续构建会先检查课程、课时、日期、资源关联和状态依据。

## 浏览器场景

Playwright 共 26 项检查通过（Chromium 桌面/手机工作台、Chromium/Firefox/WebKit/移动 WebKit 无障碍扫描及 Firefox/WebKit/移动 WebKit 核心流程），使用生产构建服务：

1. 首页、日历、五专题、资源、安全说明、搜索及首末课程详情可访问，无页面错误或控制台错误。
2. 1440px、390px 和关键页面 768px / 1024px 下无横向溢出。
3. 日历模块筛选、课程搜索、详情展开和周/列表视图正常。
4. 进度和笔记刷新恢复，导出 JSON 的实际内容正确，清除需要确认且只删除本站数据键。
5. 模板按课次筛选、搜索、复制和下载正常，CSV 文件实际包含中文编码 BOM 和所需列。
6. 来源与许可表单检查授权依据，记录本地保存、刷新恢复、导出和删除正常。
7. 全站搜索支持课程、模块及模板标签；无结果有清空入口。
8. 打印媒体下展开课次详细内容并隐藏导航；另生成了 16 页 A4 日历打印预览。
9. 损坏 JSON 不被覆盖，导出包含原始备份。
10. 浏览器存储被禁用时说明降级状态，笔记仍可在当前会话编辑并直接导出。
11. 未知课程返回 404，键盘可访问跳过导航入口，移动导航正常。
12. 页面加载没有请求站外资源；笔记输入未进入请求正文。人工检查源码未发现远程字体、模型调用、上传函数或密钥。
13. Firefox、WebKit 桌面与移动模拟下，核心页面可加载且关键筛选、导航/功能流程可用；关键页面没有横向溢出。
14. `@axe-core/playwright` 对 WCAG 2.2 A/AA 规则执行自动扫描，并启用目标尺寸规则；Chromium 桌面/手机、Firefox、WebKit 桌面/手机模拟均通过。扫描发现并修复了可访问名称、标题层级、地标命名和文字对比度问题。

## 视觉检查

已查看桌面与手机首页，以及日历、课程详情、资源页和平板科研专题截图。采用浅色学术风格、海军蓝与青绿，保留信息层级和留白；未使用学校徽标、虚构照片或未经验证的成效数据。截图及 PDF 位于被 Git 忽略的 `test-results/`。

## 依赖及限制

- `npm audit --omit=dev`：0 项已知漏洞。
- 完整开发依赖审计报告 5 项 high 问题，来自 ESLint 工具链中的 `braces@3.0.3` / micromatch / fast-glob 依赖链。GitHub Advisory GHSA-vfj7-8cjw-p6xm 目前没有修复版本；npm 的强制修复提议会造成 Next ESLint 工具链主版本不兼容，因此未使用。详情和复核期限见 [安全例外登记](SECURITY_EXCEPTIONS.md)。`npm audit --omit=dev --audit-level=high` 通过，生产依赖无 high 或更高告警。
- `napi-postinstall@0.3.5` 的官方 registry 下载地址返回 404，已固定为可下载的 `0.3.4` 并通过构建和浏览器检查。
- Playwright WebKit 使用 WebKit 引擎，并非原生 Safari 应用；Firefox/WebKit 的 Playwright 运行也不等同各操作系统的原生浏览器验收。此次未完成原生 Safari/Firefox 与 VoiceOver/NVDA 等辅助技术的人工测试。axe 自动扫描不能证明完整 WCAG 2.2 AA 符合性，发布前仍建议人工键盘与屏幕阅读器验收。
- Vercel 尚未实际部署；校内模型、L20 参数、具体日期、授权流程和联系方式仍需确认。

## 本地审阅

工程交付时已使用 `npm run start -- --hostname 127.0.0.1 --port 3000` 启动生产预览，地址为 http://127.0.0.1:3000 。进程停止后可重新运行该命令；修改代码需要重新构建或切换到 `npm run dev`。

---

## 2026-11-15 预发布复核

范围：本地依赖重装、代码检查与生产构建；**不含 Vercel 线上部署与校方验收**。

### 变更内容

- `src/content/site.ts`：将「Obsidian + Hermes」平台状态由 `proposal` 更新为 `tested`（依据：6 个 Hermes Skills 与 14 部实操视频随包交付、10 课核心讲义完成口径重构，日期 2026-11-15，责任人 iScholar 课程组）；软件工具箱条目补充 Unpaywall、CORE、PSPP、Taguette、Paperpal、PaperPass、讯飞智文等工具与 14 部视频说明。
- `README.md`：运行章节目录改为本仓库 `website/` 路径，移除文末旧项目名残留。
- 校内 L20 条目保持 `pending`；`siteConfig.contact` 与 `courseDates` 未填写，仍显示占位。

### 环境与结果

| 项目 | 结果 |
| --- | --- |
| Node.js / npm | v22.20.0 / 11.7.0 |
| `npm ci` | 通过，373 个包；因本机 npm 缓存损坏，使用 `--prefer-offline` 重装（耗时约 34 分钟） |
| `npm run lint` | 通过 |
| `npm run typecheck` | 通过 |
| `npm run test:content` | 通过（16 次课、32 小时、18 份模板、5 个专题） |
| `npm run build` | 通过，静态生成 28 个页面（首页、日历、16 课详情、5 专题、资源、搜索、关于、404） |

### 仍未完成（阻塞发布验收）

- 未创建远程仓库，未执行 Vercel 预览/正式部署，因此**没有可记录的线上地址**。
- 校方联系邮箱、开课日期、L20 实际规格与配额、素材授权与发布负责人仍待确认。
- 本轮未重跑 Playwright 浏览器测试（依赖与构建已验证；如发布前需要，可执行 `npx playwright install chromium && npm run test:e2e`）。

---

## 2026-11-16 本地记录导入与子系统增强

范围：门户网站「本地记录导入/恢复」功能、`ischolar` 后端 16 课任务链与导出增强、自动化测试回归。

### 变更

- `src/lib/learning-store.ts`：新增 `previewImportLearning()`（JSON 解析、`version === 1`、课程 ID、`notes` 键、`sources` 结构逐项校验）与 `importLearning()`（覆盖前把原记录写入 `ischolar-workbench:v1:backup`）。
- `src/components/learning-tools.tsx`：资源中心新增「导入本地 JSON」按钮、隐藏文件输入、导入前预览确认框（课次/笔记/来源数量与导出时间）及错误提示。
- `tests/workbench.spec.ts`：新增导入往返用例，覆盖损坏文件不覆盖、合法文件确认恢复。
- `ischolar/`：`TRAINING_TASKS` 扩展为 16 次课（与门户课程一致），后端改用 `lifespan`，新增项目存在性校验、结构化解析 `_parse_warning`、自定义 Vault 导出与同名文件时间戳备份、`POST /v1/projects/{id}/vault`；新增 8 个 pytest 用例。

### 结果

| 项目 | 结果 |
| --- | --- |
| `ischolar`：`python -m pytest tests -q` | 8 passed（隔离临时数据库；系统 Python 3.9 不支持 `str \| None` 注解求值，需用 Python 3.10+，本机使用 3.13） |
| `npm run lint` / `typecheck` / `test:content` | 全部通过 |
| `npm run build` | 通过，28 个静态页面 |
| `npm run test:e2e` | 26 passed，2 failed |
| 新增导入用例（desktop / mobile） | 通过 |

### 失败项说明（环境问题，非代码回归）

- `[firefox]` 的 `accessibility.spec.ts` 与 `cross-browser.spec.ts` 均在浏览器启动阶段失败：`browserType.launch: Failed to launch the browser process ... Could not find profile folder.`
- 直接以 `firefox -no-remote -headless -profile /tmp/ffprof-test -silent` 启动同样报错，确认是本机 Playwright Firefox 1555 可执行文件无法创建/读取 profile，与应用代码无关；重新执行 `npx playwright install firefox` 后现象不变。
- Chromium 桌面/移动与 WebKit 桌面/移动（含 axe WCAG 2.2 A/AA 扫描）均通过。Firefox 回归待浏览器环境修复后补跑，或改用原生 Firefox 人工验收。
