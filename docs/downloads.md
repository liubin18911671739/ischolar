# 大文件与配套资源下载

为保证仓库轻量，以下大文件不进入 Git，统一通过 **GitHub Releases** 与 **百度网盘** 分发。

## 1. GitHub Releases

发布页：<https://github.com/liubin18911671739/ischolar/releases>

| 文件 | 说明 | 大小 |
| --- | --- | --- |
| `iScholar_v6.2_本地双击即用版_Streamlit_FastAPI.zip` | 本地工作台免配置包（含启动器、后端、前端与测试） | ~43 KB |
| `Obsidian_科研Vault标准模板与Hermes技能包.zip` | 5 份笔记模板 + 6 个 Hermes Skills | ~18 KB |
| `AI4S课程_核心讲义_Obsidian_Hermes版.zip` | 15 份核心讲义 | ~87 KB |
| `AI4S课程_专题实战讲义_Obsidian_Hermes重构版.zip` | 13 份专题实战讲义 | ~186 KB |
| `AI培训计划方案.docx` | 32 课时培训方案（脱敏版） | ~49 KB |
| `AI培训方案_示例高校版_v3.pptx` | 汇报课件（脱敏版） | ~35 MB |
| `AI培训方案_示例高校版_v3.pdf` | 汇报课件 PDF（脱敏版） | ~15 MB |
| `AI培训课程日历.png` | 课程日历大图（脱敏版） | ~1.5 MB |
| `软件实操教学视频.zip` | 14 部 MP4（01–04 为步骤卡，05–14 为实操录屏） | ~35 MB |

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
