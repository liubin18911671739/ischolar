---
title: "第_4_课B__数据分析进阶Python_Obsidian_Hermes版"
workflow: "Obsidian + Hermes (OpenCode / DeepSeek Harness) + iScholar"
software_policy: "国产软件 + 开源软件（零翻墙）"
---

# 第_4_课B__数据分析进阶Python_Obsidian_Hermes版

> **工具栈说明**：本讲义将传统云端知识库工作流全面重构为 **Obsidian Vault + Hermes（OpenCode 或 DeepSeek Harness）+ 本地 iScholar 应用（Streamlit + FastAPI）**，配套软件全部采用国产软件与开源软件。

        🐍
        🐍 第 4 课B — 数据分析进阶·Python
          🐍      课程目标： 搭建 Python 数据分析环境，掌握 Pandas / Matplotlib / Seaborn 核心操作，
                 实现从 SPSS Pro 到 Python 的能力迁移



        🦞 Hermes Agent（OpenCode / DeepSeek Harness） vs ☤ Hermes Agent — 全面对比 + Hermes 部署详解
        🛡️ 零科学上网 · 全免费/开源 AI 文科论文工作流（最优实践）

        📍 模块一：Python 环境搭建（20 分钟）
        🖥️ 三件套安装：Anaconda + Jupyter + VSCode
          💡      零基础老师别怕！ 本课不要求你成为程序员。我们用 AI（DeepSeek / DeepSeek / 通义千问）自动生成
                 代码，你只需要：

                 1. 理解代码在做什么（AI 会解释）
                 2. 修改关键参数（如文件名、列名）
                 3. 运行并查看结果


        Step 1：安装 Anaconda
         步骤                操作                                      说明

                                                                   推荐 Anaconda Distribution（约
                           访问 anaconda.com/download → 选择你的操作
         1. 下载                                                     1GB），自带 Python 3.12 + 300+ 常用
                           系统
                                                                   库

                           双击安装包 → 勾选 "Add to PATH"（Windows）       Mac 用户可用 brew install --cask
         2. 安装
                           或默认设置（Mac）                              anaconda

                           打开终端，运行 conda --version 和 python --
         3. 验证             version
                                                                   应显示 conda 24.x+ 和 Python 3.12+

                            conda create -n research python=3.12
         4. 创建环境           pandas matplotlib seaborn jupyter -y
                                                                   为课题创建独立环境，避免库冲突

         5. 激活环境           conda activate research                 每次开始工作前运行




🐍 第 4 课B — 数据分析进阶·Python                                                                            1


---

          📦     Anaconda vs pip： Anaconda = Python + 包管理器(conda) + 300+预装科学计算库 +
                Jupyter。对文科老师来说，一次安装全部搞定，不需要手动 pip install 各种依赖。

        Step 2：Jupyter Notebook 基本使用
           graph
              A["  🚀启动<br>jupyter notebook"] --> B["       📝 新建 Notebook<br>New → P
          ython 3"]
               B --> C["⌨️写代码<br>Cell 中输入代码"]
               C --> D["▶️运行<br>Shift+Enter"]
               D --> E["   📊 查看结果<br>表格/图表即时显示"]
               E --> C
               style A fill:#E3F2FD,stroke:#1565C0
               style D fill:#E8F5E9,stroke:#2E7D32


                                            🚀 启动
                                        jupyter notebook




                                       📝 新建 Notebook
                                        New → Python 3




                                           ⌨️ 写代码
                                          Cell 中输入代码




                                       ▶️ 运行
                                      Shift+Enter




                                             📊 查看结果
                                          表格/图表即时显示




        核心操作速查：

         快捷键               功能               使用场景
          Shift + Enter    运行当前单元格并跳到下一个    最常用，执行代码看结果
          Ctrl + Enter     运行当前单元格（不跳转）     反复调试同一段代码




🐍 第 4 课B — 数据分析进阶·Python                                                              2


---

         快捷键               功能                          使用场景

          Esc → A          在上方插入新单元格                   添加说明文字

          Esc → B          在下方插入新单元格                   继续写代码

          Esc → M          切换为 Markdown 模式             写文字说明和标题

          Esc → DD         删除当前单元格                     清理无用代码
          Tab              代码自动补全                      忘记函数名时使用



          💡      Jupyter 的核心优势： 代码和结果（表格、图表）在同一界面中即时呈现，非常适合数据
                 探索和可视化。你可以一边写代码一边看结果，就像一个交互式笔记本。


        Step 3：VSCode 安装与 Python 配置
         步骤                操作                                                  说明

         1. 下载             访问 code.visualstudio.com                            免费、跨平台的代码编辑器

                                                                               提供语法高亮、智能提示、
         2. 安装扩展           搜索并安装：Python • Jupyter • Pylance
                                                                               Notebook 支持
                           Ctrl+Shift+P → "Python: Select Interpreter" → 选
         3. 选择解释器                                                              确保使用 Anaconda 创建的环境
                            research 环境

         4. 打开
                           新建 .ipynb 文件或打开已有 Notebook                          VSCode 内置 Jupyter 支持
         Notebook

        Jupyter vs VSCode：何时用哪个？

          📓 ✅    Jupyter Notebook
                       数据探索和可视化
                                                                 💻 ✅   VSCode
                                                                               编写完整 .py 脚本

                     ✅ 教学演示（步步可见）                                            ✅ 大型项目（多文件）
                     ✅ 快速实验和原型                                               ✅ Git 版本控制集成
                     ❌ 大型项目管理                                                ✅ 同时也能运行 .ipynb

        📍 模块二：SPSS Pro → Python 能力迁移（20 分钟）
         🔄       核心思路： 你在 SPSS Pro 中已经会用的功能，在 Python 中都有对应实现，而且更灵
                 活、更可复现、更适合自动化。


        常用统计功能对照表




🐍 第 4 课B — 数据分析进阶·Python                                                                              3


---

         分析任务              SPSS Pro 操作   Python 实现                       核心函数

         读取数据
                           文件 → 打开 →     import pandas as pd             pd.read_csv()   /
                           数据            df = pd.read_csv("data.csv")    pd.read_excel()

                           分析 → 描述统      df.describe()
         描述统计                                                            .describe()    .mean()    .std()
                           计 → 频率/描述     df["col"].value_counts()

                           分析 → 描述统
         交叉表                             pd.crosstab(df["A"], df["B"])   pd.crosstab()
                           计 → 交叉表

                           分析 → 比较均      from scipy import stats
         独立样本 t 检验                                                       scipy.stats.ttest_ind()
                           值 → 独立样本 T    stats.ttest_ind(g1, g2)

                           分析 → 比较均
         单因素方差分析           值 → 单因素       stats.f_oneway(g1, g2, g3)      scipy.stats.f_oneway()
                           ANOVA
                           分析 → 相关 →     df.corr()                       .corr()    pearsonr()
         相关分析
                           双变量           stats.pearsonr(x, y)            spearmanr()

                           分析 → 回归 →     import statsmodels.api as sm
         线性回归                                                            statsmodels.OLS()
                           线性            sm.OLS(y, X).fit()

                           分析 → 量表 →
         信度分析                            pg.cronbach_alpha(df[items])    pingouin.cronbach_alpha()
                           可靠性分析

                           分析 → 描述统
         卡方检验              计 → 交叉表 →     stats.chi2_contingency(table)   scipy.stats.chi2_contingency()
                           卡方

                           数据 → 选择个      df[df["age"] > 30]
         数据筛选                                                            布尔索引 / .query()
                           案             df.query("age > 30")

                           转换 → 替换缺
         缺失值处理                           df.fillna(0)    / df.dropna()   .fillna()    .dropna()    .isna()
                           失值

                           转换 → 重编码
         重编码                             df["col"].map({"A":1, "B":2})   .map()    .replace()    .cut()
                           为不同变量


        Python 的三大优势（相比 SPSS Pro）

          🔄     可复现
                代码 = 完整分析记录。分享 .ipynb 文件，任何人都能重现你的分析过程。SPSS 点菜单不
                留痕迹。




          ⚡     可自动化
                同一分析逻辑可用 for 循环批量处理 100 个文件。SPSS 每个文件都要重新点一遍。




          🧩     可扩展
                Python 生态无限——NLP、机器学习、知识图谱、大模型 API 全部打通。SPSS 只能做统
                计。




🐍 第 4 课B — 数据分析进阶·Python                                                                                     4


---

        课题案例：问卷数据分析（SPSS → Python）


          💬     提示词模板 — 让 AI 帮你把 SPSS 操作翻译成 Python
                我在 SPSS Pro 中完成了以下分析，请帮我用 Python（pandas + scipy + statsmodels）
                实现同样的功能：

                1. 读取 survey_data.csv（入境游客满意度问卷，包含国籍、年龄、语言能力、满意度 5
                   级量表）

                2. 描述性统计：均值、标准差、频率分布
                3. 信度分析：计算满意度量表的 Cronbach's α
                4. 按国籍分组的满意度对比：单因素方差分析（ANOVA）
                5. 语言障碍与满意度的 Pearson 相关分析
                6. 多元线性回归：自变量=年龄+语言能力+文化距离，因变量=满意度
                请使用 pandas + scipy + statsmodels，输出中文注释，打印带 emoji 的结果。


        示例代码片段：

          import pandas as pd
          from scipy import stats
          import statsmodels.api as sm

          # 1. 读取数据（对应 SPSS：文件→打开→数据）
          df = pd.read_csv("survey_data.csv")


          # 2. 描述性统计（对应 SPSS：分析→描述统计→描述）
          print("  📊描述性统计")
          print(df.describe())

          # 3. 按国籍分组的满意度对比（对应 SPSS：分析→比较均值→单因素ANOVA）
          groups = [g["satisfaction"] for _, g in df.groupby("nationality")]
          f_stat, p_value = stats.f_oneway(*groups)
          print(f"\n   🔬
                       单因素方差分析: F={f_stat:.3f}, p={p_value:.4f}")

          # 4. 相关分析（对应 SPSS：分析→相关→双变量）
          r, p = stats.pearsonr(df["language_barrier"], df["satisfaction"])
          print(f"\n   🔗
                       Pearson相关: r={r:.3f}, p={p:.4f}")


          # 5. 多元线性回归（对应 SPSS：分析→回归→线性）
          X = sm.add_constant(df[["age", "language_ability", "cultural_distanc
          e"]])
          model = sm.OLS(df["satisfaction"], X).fit()
          print(f"\n   📈
                       回归分析:\n{model.summary()}")




🐍 第 4 课B — 数据分析进阶·Python                                                         5


---

        📍 模块三：Matplotlib + Seaborn 数据可视化（15 分钟）
         🎨      Matplotlib 是 Python 最基础的绑图库（高度可定制），Seaborn 在它之上提供更美观的
                统计图表（一行代码出图）。两者搭配使用效果最佳。


        核心图表类型与选择指南
         数据关系              推荐图表         Seaborn 函数                             课题应用场景

         分布                直方图 / 核密度图   sns.histplot()    / sns.kdeplot()      游客满意度分数分布

         比较                柱状图 / 箱线图    sns.barplot()    / sns.boxplot()       不同国籍游客满意度对比

         相关                散点图 / 热力图    sns.scatterplot()    / sns.heatmap()   语言障碍与满意度相关性

         趋势                折线图          sns.lineplot()                         入境游客数量年度变化趋势

         占比                饼图 / 环形图     plt.pie() （Matplotlib）                 游客来源国占比

         多变量               组合图 / 分面图    sns.FacetGrid()    / sns.pairplot()    多维度满意度交叉分析


        可视化实战：课题数据四张核心图
        图 1：不同国籍游客满意度对比（柱状图 + 误差棒）

          import matplotlib.pyplot as plt
          import seaborn as sns

          # 设置中文字体（解决乱码）
          plt.rcParams["font.sans-serif"] = ["SimHei"] # Windows
          # plt.rcParams["font.sans-serif"] = ["PingFang SC"] # Mac
          plt.rcParams["axes.unicode_minus"] = False


          # 柱状图：按国籍分组的满意度对比
          fig, ax = plt.subplots(figsize=(10, 6))
          sns.barplot(data=df, x="nationality", y="satisfaction",
                      palette="Set2", ci=95, ax=ax)
          ax.set_title("不同国籍入境游客满意度对比", fontsize=16, fontweight="bold")
          ax.set_xlabel("国籍", fontsize=12)
          ax.set_ylabel("满意度均值（5级量表）", fontsize=12)
          plt.tight_layout()
          plt.savefig("fig1_satisfaction_by_nationality.png", dpi=300)
          plt.show()


        图 2：满意度各维度相关性热力图

          # 热力图：变量间相关性矩阵
          corr_cols = ["overall_satisfaction", "language_service",
                       "cultural_experience", "transportation", "food"]
          corr_matrix = df[corr_cols].corr()



🐍 第 4 课B — 数据分析进阶·Python                                                                      6


---

          fig, ax = plt.subplots(figsize=(8, 6))
          sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="RdYlBu_r",
                      center=0, square=True, ax=ax)
          ax.set_title("满意度各维度相关性矩阵", fontsize=14, fontweight="bold")
          plt.tight_layout()
          plt.savefig("fig2_correlation_heatmap.png", dpi=300)
          plt.show()


        图 3：语言障碍与满意度散点图（回归线）

          # 散点图 + 回归线
          fig, ax = plt.subplots(figsize=(8, 6))
          sns.regplot(data=df, x="language_barrier", y="satisfaction",
                      scatter_kws={"alpha": 0.5}, line_kws={"color": "red"}, ax=
          ax)
          ax.set_title("语言障碍与游客满意度关系", fontsize=14, fontweight="bold")
          ax.set_xlabel("语言障碍程度（1-5）", fontsize=12)
          ax.set_ylabel("总体满意度（1-5）", fontsize=12)
          plt.tight_layout()
          plt.savefig("fig3_language_satisfaction.png", dpi=300)
          plt.show()


        图 4：游客来源国分布（饼图）

          # 饼图：游客来源国占比
          counts = df["nationality"].value_counts()
          fig, ax = plt.subplots(figsize=(8, 8))
          colors = sns.color_palette("Set3", len(counts))
          ax.pie(counts, labels=counts.index, autopct="%1.1f%%",
                 colors=colors, startangle=140)
          ax.set_title("入境游客来源国分布", fontsize=14, fontweight="bold")
          plt.tight_layout()
          plt.savefig("fig4_nationality_distribution.png", dpi=300)
          plt.show()


        Seaborn 美化技巧速查




🐍 第 4 课B — 数据分析进阶·Python                                                           7


---

          🎨       一行代码提升颜值：

                    sns.set_theme(style="whitegrid")   — 白色网格背景（学术论文推荐）
                    sns.set_palette("Set2")    — 使用柔和配色方案
                    plt.savefig("fig.png", dpi=300, bbox_inches="tight")   — 高分辨率导出（期刊投稿要求）
                    sns.set_context("paper")   — 适合论文的字体大小



        📍 模块四：AI 辅助 Python 编程（5 分钟）
         🤖        核心理念： 你不需要记住任何函数名——用自然语言告诉 AI 你想做什么，AI 帮你写代
                  码。


        AI 编程提示词模板
         分析需求                                                提示词模板

                                                             "请帮我写 Python 代码，读取 data.csv，处理缺失值
         数据清洗                                                （用均值填充数值列，删除缺失超过 50% 的行）       ，并输
                                                             出清洗后的数据概况"

                                                             "请对 survey.csv 做全面描述统计，包括均值、标准
         描述统计                                                差、分位数、频率分布，并生成汇总表格，使用
                                                             pandas"
                                                             "请用 scipy 对 A 组和 B 组的满意度数据做独立样本 t
         假设检验
                                                             检验，并解读 t 值和 p 值的含义"

                                                             "请用 seaborn 画一组 2×2 子图，包含柱状图、箱线
         可视化                                                 图、散点图、热力图，数据来自 data.csv，中文标签，
                                                             学术风格"


        推荐 AI 编程工具
         工具                    特点                                          适用场景

         DeepSeek / 通义千问 Code           终端中自然语言→自动写码+运行+调试                          完整脚本开发，自动修 bug

         Cursor                AI 加持的 VSCode 分支，Cmd+K 生成代码                 日常编码，边写边补全

         DeepSeek / DeepSeek    网页对话生成代码 → 复制到 Jupyter 运行                   快速实验，零安装

         GitHub Copilot        VSCode 插件，实时代码补全                            熟练用户加速编码



        📝 课后作业
            A. 完成 Anaconda + Jupyter + VSCode 安装，截图验证 conda --version 和 python --version
            B. 在 Jupyter Notebook 中用 pandas 读取一份 CSV 数据（课题问卷/公开数据集），完成描述
         性统计




🐍 第 4 课B — 数据分析进阶·Python                                                                          8


---

            C. 用 Seaborn 制作两张课题相关的可视化图表（柱状图 + 热力图），导出 300dpi PNG
            D. 将 SPSS Pro 中的一项分析（如 t 检验或回归）用 Python 重新实现，对比两者输出结果

        📐 练习试题
        选择题
        Q1. 以下哪个不是 Anaconda 自带的组件？
            A. Python 解释器
            B. Jupyter Notebook
            C. conda 包管理器
            D. VSCode 编辑器
           答案：D — VSCode 需要单独安装。Anaconda 自带 Python + conda + Jupyter + 300+ 科学计
           算库。

        Q2. 在 Python 中，与 SPSS 的"分析 → 比较均值 → 独立样本 T"功能对应的是？
            A. pd.crosstab()
            B. stats.ttest_ind()
            C. df.describe()
            D. sm.OLS()
           答案：B — scipy.stats.ttest_ind() 用于两组独立样本的 t 检验。

        Q3. Seaborn 中绘制相关性矩阵热力图应使用哪个函数？
            A. sns.barplot()
            B. sns.scatterplot()
            C. sns.heatmap()
            D. sns.lineplot()
           答案：C — sns.heatmap() 配合 df.corr() 生成相关性热力图。

        Q4. 以下哪种做法最能保证数据分析的可复现性？
            A. 在 SPSS 中截图记录每步操作
            B. 用 Jupyter Notebook 编写完整代码并保存 .ipynb 文件
            C. 在 Word 中手动记录分析步骤
            D. 口头描述分析过程
           答案：B — Jupyter Notebook 中代码+结果一体保存，任何人打开即可重现全部分析。

        Q5. 在 Matplotlib 中设置中文字体以避免乱码，正确的方法是？



🐍 第 4 课B — 数据分析进阶·Python                                                          9


---

            A. plt.rcParams["font.sans-serif"] = ["SimHei"]
            B. plt.set_language("chinese")
            C. sns.set_font("chinese")
            D. import chinese_font
           答案：A — 需要手动设置 rcParams 指定支持中文的字体。



        🔮 下节预告
         ☁️     第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战

                    校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 平台注册与 GPU Pod 管理
                    Axolotl + Hugging Face 模型微调（LoRA）
                    vLLM Serverless 大模型部署
                    Jupyter 云端训练大模型
                    ComfyUI 多模态内容生成




🐍 第 4 课B — 数据分析进阶·Python                                      10


---

