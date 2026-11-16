# 大文件与配套资源下载

为保证仓库轻量，以下大文件不进入 Git，统一通过 **GitHub Releases** 与 **百度网盘** 分发。

## 1. GitHub Releases

发布页：<https://github.com/liubin18911671739/ischolar/releases>

| 文件（Releases 资产名） | 说明 | 大小 |
| --- | --- | --- |
| `ischolar-v6.2-local-app.zip` | 本地工作台免配置包（含启动器、后端、前端与测试） | ~43 KB |
| `obsidian-research-vault-template.zip` | 5 份笔记模板 + 6 个 Hermes Skills | ~18 KB |
| `ai4s-core-lectures.zip` | 15 份核心讲义 | ~87 KB |
| `ai4s-topic-lectures.zip` | 13 份专题实战讲义 | ~186 KB |
| `training-plan.docx` | 32 课时培训方案（脱敏版） | ~49 KB |
| `training-plan-slides.pptx` | 汇报课件（脱敏版） | ~35 MB |
| `training-plan-slides.pdf` | 汇报课件 PDF（脱敏版） | ~15 MB |
| `training-calendar.png` | 课程日历大图（脱敏版） | ~1.5 MB |

> Releases 资产使用英文文件名以保证跨平台下载稳定；仓库内 `software-and-videos/01_国产与开源软件工具包/` 下的同名压缩包保留中文名，内容一致。

> 14 部 MP4 实操视频正在做逐帧隐私检查（个人路径、账号、弹窗信息），审核完成后会补充到 Releases；当前请先使用文末「自行录制」或网盘中的原始交付版。

校验方式：下载 `SHA256SUMS.txt` 后执行

```bash
shasum -a 256 -c SHA256SUMS.txt
```

## 2. 百度网盘

已通过 `bypy` 同步至：

```text
/apps/bypy/iScholar课程/软件与视频工具箱/01_国产与开源软件工具包/
/apps/bypy/iScholar课程/软件与视频工具箱/02_软件实操教学视频/
/apps/bypy/iScholar课程/培训方案与讲义_Obsidian_Hermes版/
```

网盘中的文件为原始交付版；开源仓库内的讲义与方案已做院校名称与个人姓名脱敏，内容口径一致。

## 3. 未随仓库分发的第三方资料

- `lectures/原版参考课件_PDF/` 下的 13 份原始 PDF 讲义，因版权归属与授权范围不明确，**不公开分发**；
- 视频中出现的第三方软件界面、图表与论文截图，版权归各自权利人所有，仅用于教学演示。

## 4. 自行打包

```bash
./scripts/package-and-sync.sh          # 生成 4 个 zip + SHA256SUMS.txt
./scripts/package-and-sync.sh --sync   # 可选：同步至百度网盘（需 uvx bypy 授权）
```
