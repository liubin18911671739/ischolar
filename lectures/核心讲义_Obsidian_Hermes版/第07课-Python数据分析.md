---
title: 第07课｜Python 数据分析与零代码统计
type: lesson
course: AI4S · 高校教师科研与教学 AI 实训
lesson: "07 / 10"
duration: 150 分钟（理论 40 + 实操 110）
difficulty: 进阶 · 可选零代码路线
progress: "▰▰▰▰▰▰▰▱▱▱ 70%"
tools:
  - Anaconda
  - Jupyter Notebook
  - VS Code
  - pandas / matplotlib
  - jamovi
  - JASP
  - GNU PSPP
  - SPSSAU
  - SPSSPRO
  - AntConc
deliverables:
  - 1 份描述统计报告（含三线表）
  - 1 张达到投稿要求的图
  - 1 张统计方法选择速查表
  - 1 份可复现的分析脚本（可选）
videos:
  - 05_VSCode_Anaconda环境配置与Hermes终端论文项目实战.mp4
  - 09_见数_问卷星调研设计与SPSSAU_SPSSPRO零代码统计分析.mp4
  - 10_AntConc语料库下载安装与KWIC_词簇_共现检索实战.mp4
  - 12_jamovi_JASP_PSPP三大开源免费统计软件下载与对比.mp4
  - 04_Ollama本地大模型与jamovi_AntConc数据分析教程.mp4
tags: [AI4S, Python, 数据分析, 可视化, 统计方法]
created: 2026-09-17
updated: 2026-11-15
---

# 第07课｜Python 数据分析与零代码统计

> [!abstract] 🎯 本课定位
> 这一课给你**两条路**：一条零代码（jamovi / JASP / SPSSAU），一条写代码（Python / pandas）。两条路的终点相同：**一张审稿人挑不出毛病的表和一张说得清的图**。
>
> **建议**：先走零代码路线把分析跑通，再用 Python 处理批量与可复现需求。不要一上来就学 Python。

> [!info] 📌 先说结论
> 文科论文里 80% 的分析需求，jamovi / JASP 完全够用；Python 的价值在于**批量处理、可复现、可版本管理**，以及处理语料文本。

---

## 🧰 一、本课软件工具箱（下载 · 安装 · 备份）

| 工具 | 类型 | 官方地址 | 国内加速 / 说明 | 百度网盘备份 |
| :-- | :-- | :-- | :-- | :-- |
| **jamovi** | 零代码统计（开源） | <https://jamovi.org> | 国内可直连；`brew install --cask jamovi` | `/iScholar课程/软件与视频工具箱/01_国产与开源软件工具包/` |
| **JASP** | 零代码统计（开源，贝叶斯友好） | <https://jasp-stats.org> | 国内可直连；`brew install --cask jasp` | 同上 |
| **GNU PSPP** | SPSS 的自由替代（命令行/图形） | <https://www.gnu.org/software/pspp/> | 国内可访问；macOS `brew install pspp` | 同上（含下载说明） |
| **SPSSAU** | 在线零代码统计 | <https://spssau.com> | 国内直连 | —（在线） |
| **SPSSPRO** | 在线零代码统计 | <https://www.spsspro.com> | 国内直连 | —（在线） |
| **Anaconda** | Python + 科学计算全家桶 | <https://www.anaconda.com/download> | 国内可用清华镜像：<https://mirrors.tuna.tsinghua.edu.cn/anaconda/> | 同上（安装引导） |
| **Miniconda** | 轻量版 Anaconda（推荐） | <https://docs.conda.io/en/latest/miniconda.html> | 同上 | 同上 |
| **Jupyter Notebook** | 浏览器内交互式编程 | 随 Anaconda 安装 | `pip install notebook` | 同上 |
| **VS Code** | 代码编辑器（配合 Jupyter 插件） | <https://code.visualstudio.com> | 国内可直连 | 同上 |
| **pandas / matplotlib** | 数据处理与绘图 | <https://pandas.pydata.org> / <https://matplotlib.org> | `pip install pandas matplotlib`（清华源） | 同上 |
| **AntConc 4.4.2** | 语料库检索与词频 | <https://www.laurenceanthony.net/software/antconc/> | 国内可直连 | 同上 |

> [!example] 🎬 配套实操视频
> - **`12_jamovi_JASP_PSPP三大开源免费统计软件下载与对比.mp4`**（54 秒）：`jamovi.org` → `jasp-stats.org` → `gnu.org/software/pspp/` 三者下载与界面差异。
> - **`09_见数_问卷星调研设计与SPSSAU_SPSSPRO零代码统计分析.mp4`**：SPSSAU 上传 Excel → 选方法 → 出三线表；SPSSPRO 在线分析。
> - **`05_VSCode_Anaconda环境配置与Hermes终端论文项目实战.mp4`**：Anaconda / Jupyter / matplotlib / VS Code 安装 + 在终端里让 Hermes 写分析脚本。
> - **`10_AntConc语料库下载安装与KWIC_词簇_共现检索实战.mp4`**：语料词频、KWIC、词簇、搭配。
> - **`04_Ollama本地大模型与jamovi_AntConc数据分析教程.mp4`**：三件套协同工作流。

---

## 🧭 二、先选工具：三条路线对比

| 维度 | jamovi / JASP | SPSSAU / SPSSPRO | Python（pandas） |
| :-- | :-- | :-- | :-- |
| 上手难度 | ★☆☆ | ★☆☆ | ★★★ |
| 费用 | 完全免费 | 基础免费/高级付费 | 完全免费 |
| 数据是否上传 | **本地** | **上传到服务器** | 本地 |
| 适合 | 问卷、实验、量表 | 快速出结果、教学演示 | 批量、文本、可复现 |
| 可复现性 | 中（可导出分析文件） | 低 | **高**（脚本即方法） |
| 图表质量 | 好，可导出 | 好 | 需调参，但最灵活 |
| 推荐场景 | 论文正文分析 | 快速摸底 | 语料清洗、批量统计 |

> [!warning] 数据合规提醒
> SPSSAU / SPSSPRO 是**在线服务**，数据会上传。含学生个人信息或未公开数据的，请用 jamovi / JASP / Python 本地处理（见第 06 课三级数据边界）。

---

## 📊 三、零代码路线：jamovi 实操

### 3.1 安装与界面

```bash
# macOS
brew install --cask jamovi
# 或官网下载 .dmg / .exe
```

界面分三块：左侧**分析菜单**、中间**数据表**、右侧**结果区**。

### 3.2 导入数据

```text
菜单 → 数据 → 导入 → Excel / CSV / SPSS (.sav)
```

> [!tip] 数据准备三条
> 1. 第一行必须是变量名，不含合并单元格。
> 2. 一列一个变量，一行一个被试。
> 3. 分类变量设为「名义/有序」，连续变量设为「连续」，否则分析菜单会灰掉。

### 3.3 常用分析路径

| 需求 | jamovi 路径 |
| :-- | :-- |
| 频数、均值、标准差 | 分析 → 探索 → 描述统计 |
| 信度 | 分析 → 因子 → 可靠性分析（Cronbach's α） |
| 两组比较 | 分析 → t 检验 → 独立样本 / 配对样本 |
| 多组比较 | 分析 → 方差分析 → ANOVA |
| 相关 | 分析 → 回归 → 相关矩阵 |
| 线性回归 | 分析 → 回归 → 线性回归 |
| 卡方 | 分析 → 频率 → 独立样本卡方 |

### 3.4 导出投稿级三线表

```text
结果区右键 → 复制 → 粘贴到 Word
或：结果区 → 导出 → HTML / PDF
```

三线表规范：**顶线、栏目线、底线**，无竖线；表中保留 M、SD、t/F、p、效应量（Cohen's d / η²）。

### 3.5 JASP 的差异

- 界面与 jamovi 类似，**贝叶斯分析**更完整（Bayes Factor）。
- 适合需要“支持零假设”论证的研究（如“两组无差异”）。
- 同样支持导出 APA 格式表。

### 3.6 GNU PSPP（SPSS 替代）

```bash
brew install pspp
pspp   # 图形界面
```

适合已经习惯 SPSS 语法的人；兼容 `.sav` 文件，可跑 `DESCRIPTIVES`、`T-TEST`、`REGRESSION` 等语法。界面较朴素，图表能力弱于 jamovi。

---

## 🐍 四、Python 路线：从环境到出图

### 4.1 安装 Anaconda / Miniconda

```bash
# 推荐 Miniconda（体积小）
# 官网下载对应系统安装包后：
bash Miniconda3-latest-MacOSX-arm64.sh

# 验证
conda --version
python --version
```

```bash
# 国内加速
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 4.2 建一个专用环境

```bash
conda create -n research python=3.11 -y
conda activate research
pip install pandas matplotlib openpyxl scipy statsmodels jupyter
```

> [!tip] 为什么建独立环境
> 不同项目的包版本会冲突。一个环境一个项目，写方法部分时可以准确报告版本号。

### 4.3 Jupyter 基础

```bash
jupyter notebook
```

| 操作 | 快捷键 |
| :-- | :-- |
| 运行当前格 | `Shift + Enter` |
| 上方插入 | `Esc` 然后 `A` |
| 下方插入 | `Esc` 然后 `B` |
| 删除 | `Esc` 然后 `D D` |
| 切换 Markdown | `Esc` 然后 `M` |

### 4.4 读取与清洗

```python
import pandas as pd

df = pd.read_excel("问卷数据.xlsx")
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())

# 缺失值
print(df.isnull().sum())
df_clean = df.dropna(subset=["核心量表1", "核心量表2"])

# 去重
df_clean = df_clean.drop_duplicates(subset=["编号"])

# 类型转换
df_clean["教龄"] = pd.to_numeric(df_clean["教龄"], errors="coerce")
```

### 4.5 描述统计与分组

```python
# 描述统计
desc = df_clean[["AI使用频率", "反馈质量"]].agg(["mean", "std", "min", "max"])
print(desc)

# 分组均值
group = df_clean.groupby("教龄段")[["AI使用频率"]].agg(["mean", "std", "count"])
print(group)
```

### 4.6 t 检验与回归

```python
from scipy import stats
import statsmodels.formula.api as smf

# 独立样本 t 检验
g1 = df_clean.loc[df_clean["组别"] == "实验组", "写作成绩"]
g2 = df_clean.loc[df_clean["组别"] == "对照组", "写作成绩"]
t, p = stats.ttest_ind(g1, g2, equal_var=False)
print(f"t={t:.3f}, p={p:.4f}")

# 线性回归
model = smf.ols("写作成绩 ~ AI使用频率 + 教龄 + C(学科)", data=df_clean).fit()
print(model.summary())
```

### 4.7 出图（投稿要求）

```python
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["PingFang SC", "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
means = df_clean.groupby("组别")["写作成绩"].mean()
errors = df_clean.groupby("组别")["写作成绩"].std()
ax.bar(means.index, means.values, yerr=errors.values, capsize=4,
       color=["#2E5C8A", "#8AA9C6"], edgecolor="black", linewidth=0.6)
ax.set_ylabel("写作成绩（M ± SD）")
ax.set_title("实验组与对照组写作成绩比较")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("fig1_writing_score.png", dpi=300, bbox_inches="tight")
plt.show()
```

> [!warning] 图的四条硬规矩
> 1. **300 dpi** 以上，导出 PNG 或 PDF（矢量优先）。
> 2. 中文必须设字体，否则出现方块。
> 3. 误差线要说明是 SD 还是 SE。
> 4. 图注要能独立读懂（不看正文也知道画的是什么）。

---

## 🔤 五、语料分析：AntConc 与 Python 的分工

| 任务 | 用 AntConc | 用 Python |
| :-- | :-- | :-- |
| 快速看词频、KWIC | ✅ 最快 | 需写代码 |
| 词簇、搭配 | ✅ 内置 | 需 nltk/spacy |
| 批量清洗 10 万条文本 | ❌ | ✅ |
| 情感分析、主题模型 | ❌ | ✅ |
| 出可交互图 | ❌ | ✅ |

### 5.1 AntConc 核心操作

```text
1. File → Open File(s) → 选择语料（.txt）
2. 左侧 Target Corpus 显示 Files / Tokens
3. KWIC：输入检索词 → Start → 看索引行
4. Cluster：Cluster Size = 2~4，Min. Freq = 5
5. Collocate：看搭配词与强度
6. Word List → 生成词频表 → 导出 CSV
```

### 5.2 Python 批量清洗示例

```python
import re
from pathlib import Path

def clean(text: str) -> str:
    text = re.sub(r"http\S+", "", text)          # 去 URL
    text = re.sub(r"\s+", " ", text)             # 压空白
    text = re.sub(r"[^\u4e00-\u9fa5A-Za-z0-9，。！？；：]", "", text)
    return text.strip()

out = Path("cleaned"); out.mkdir(exist_ok=True)
for p in Path("raw").glob("*.txt"):
    t = p.read_text(encoding="utf-8", errors="ignore")
    (out / p.name).write_text(clean(t), encoding="utf-8")
print("done")
```

---

## 📋 六、统计方法选择速查表

| 研究问题 | 自变量 | 因变量 | 方法 |
| :-- | :-- | :-- | :-- |
| 两组均值是否有差异 | 二分类 | 连续 | 独立样本 t 检验 |
| 同一组前后是否变化 | 时间（前/后） | 连续 | 配对样本 t 检验 |
| 三组以上均值差异 | 多分类 | 连续 | 单因素 ANOVA + 事后检验 |
| 两个连续变量关系 | 连续 | 连续 | Pearson / Spearman 相关 |
| 控制变量后的影响 | 多个 | 连续 | 多元线性回归 |
| 二分类结果的影响因素 | 多个 | 二分类 | Logistic 回归 |
| 分类变量关联 | 分类 | 分类 | 卡方检验 |
| 量表内部一致性 | — | 多题项 | Cronbach's α |
| 量表结构效度 | — | 多题项 | 探索性/验证性因子分析 |

> [!warning] 三个最常见的方法误用
> 1. **不检验前提就用 t 检验**：方差不齐、严重偏态时应用 Welch t 或非参数检验。
> 2. **把相关当因果**：横断面问卷只能谈关联。
> 3. **多重比较不校正**：做 10 次检验必有一个 p<0.05，需 Bonferroni 或 FDR。

---

## 🧪 七、课堂实操与验收

### 7.1 任务卡（零代码路线）

- [ ] 安装 jamovi 或 JASP
- [ ] 导入一份问卷数据（可用课程示例）
- [ ] 完成描述统计 + 信度分析
- [ ] 完成一次组间比较（t 或 ANOVA）
- [ ] 导出一张三线表到 Word

### 7.2 任务卡（Python 路线，可选）

- [ ] 建 `research` conda 环境
- [ ] 用 pandas 读取并清洗数据
- [ ] 输出描述统计表
- [ ] 用 matplotlib 出一张 300 dpi 图
- [ ] 把脚本存进 `04-数据与分析/scripts/`

> [!success] ✅ 本课验收标准
> | 项目 | 合格线 |
> | :-- | :-- |
> | 描述统计 | 含 n、M、SD、缺失值说明 |
> | 推断统计 | 前提检验 + 效应量 + p 值 |
> | 表格 | 三线表，无竖线 |
> | 图 | 300 dpi，中文正常，图注完整 |
> | 可复现 | 脚本或 jamovi 分析文件可重跑 |

---

## ❓ 八、常见问题

> [!question] Q1：jamovi 和 JASP 选哪个？
> 常规频数派检验选 jamovi（更轻快）；需要贝叶斯因子或更规范的表输出选 JASP。两者都免费，可都装。

> [!question] Q2：一定要学 Python 吗？
> 不强制。但如果要做语料清洗、批量文本处理、或者想让分析可复现，Python 值得投入 2–3 周。

> [!question] Q3：Anaconda 太大，有替代吗？
> Miniconda 或 `uv`（更现代、更快）。课程给的是最稳的路径，进阶可用 uv。

> [!question] Q4：matplotlib 中文变方块？
> 设置 `plt.rcParams["font.sans-serif"]` 为系统已安装的中文字体（macOS: PingFang SC；Windows: Microsoft YaHei），并设 `axes.unicode_minus = False`。

> [!question] Q5：SPSSAU 结果能直接写进论文吗？
> 可以，但要自己核对：样本量、前提假设、效应量、p 值精度。工具只负责算，解释权在你。

> [!question] Q6：图被审稿人说"太丑"怎么办？
> 三件事立刻改善：①去边框（top/right spines）；②统一配色（2–3 个低饱和色）；③字号 ≥ 8pt，导出 300 dpi。

---

## 📎 九、本课交付物与衔接

| 交付物 | 位置 |
| :-- | :-- |
| 描述统计报告 | `04-数据与分析/结果/描述统计.md` |
| 三线表 | 同上（Word 版） |
| 图 | `04-数据与分析/figures/fig1_*.png` |
| 分析脚本 | `04-数据与分析/scripts/analysis.py` |
| 方法速查表 | `04-数据与分析/统计方法速查.md` |

**下一课预告**：第 08 课把结果写成论文——IMRaD 模块化写作、CARS 引言、三级润色与查重。

---

> [!quote] 本课一句话
> **统计工具只负责算得对；说得对，仍然是你的事。**
