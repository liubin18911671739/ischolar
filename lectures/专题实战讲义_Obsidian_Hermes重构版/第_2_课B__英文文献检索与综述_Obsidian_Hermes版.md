---
title: "第_2_课B__英文文献检索与综述_Obsidian_Hermes版"
workflow: "Obsidian + Hermes (OpenCode / DeepSeek Harness) + iScholar"
software_policy: "国产软件 + 开源软件（零翻墙）"
---

# 第_2_课B__英文文献检索与综述_Obsidian_Hermes版

> **工具栈说明**：本讲义将传统云端知识库工作流全面重构为 **Obsidian Vault + Hermes（OpenCode 或 DeepSeek Harness）+ 本地 iScholar 应用（Streamlit + FastAPI）**，配套软件全部采用国产软件与开源软件。

       📖
       第 2 课B — 英文文献检索与综述
         📖    课程目标： 掌握英文学术文献检索、Zotero 管理与英文综述写作方法，产
              出 Zotero 文献库 ≥ 15 篇 + 500 词英文综述初稿



         ⚠️ ⚠️ 关于科学上网的重要提示
              由于北京市最新的网络管理要求，请勿使用个人 VPN（"梯子"）访问境外
              网站。学校正在积极申请正规的外网访问渠道，届时将统一通知使用方式。
              本页面中标注   ⚠️ 的工具表示需要科学上网才能访问，请暂时使用国内替代
              方案。




       📍 模块一：英文学术数据库全景（10 分钟）
       🌐 核心数据库与工具
        工具             特色功能            适用场景          科学上网

        🔍 OpenAlex / Semantic Scholar / 知网（CNKI） 最全面的学术搜索，引用追
                         踪
                                           快速发现 + 引用链追
                                           踪
                                                       ⚠️ 需要
        🧠 Semantic       AI 驱动的语义搜索 + TLDR 快速筛选 + 影响力评
                                                       ❌ 不需要
        Scholar        摘要              估




第 2 课B — 英文文献检索与综述                                             1


---

        工具                       特色功能                         适用场景                 科学上网

        🤖 Semantic Scholar / 秘塔 AI 学术搜索 / AMiner（智谱开源学术平台）                 自然语言提问 → AI 结构化
                                 提取
                                                              系统性文献摸底              ❌ 不需要
        📊 Consensus              学术共识量化（Yes/No 仪
                                 表盘）
                                                              验证假设的证据基础            ❌ 不需要
        🕸️ Connected             文献引用网络可视化
                                                              发现核心文献与研究
                                                                                   ❌ 不需要
        Papers                                                前沿

        📑 Scite.ai               引用语境分析（支持/反对/
                                 提及）
                                                              评估论文争议性              ❌ 不需要
       🎯 课题案例：英文检索词设计
         💬       围绕模拟国社科课题的英文检索词扩展：

                     论文 1（目的地形象）： generative AI destination image , multimodal
                     tourism content analysis   , UGC tourism perception Beijing
                     论文 2（智能问答）： knowledge graph tourism Q&A , multilingual RAG
                     system   , cultural heritage intelligent service
                     论文 3（跨文化交际）： LLM cross-cultural communication , inbound tourism
                     language barrier   , AI-mediated intercultural interaction



       📍 模块二：Zotero 文献管理（15 分钟）
       📚 Zotero 7 安装与配置
        组件                              下载地址                         说明

        Zotero 7 桌面版                    zotero.org/download          主程序，Win/Mac/Linux

        浏览器 Connector                   Zotero 官网自动提示安装              一键抓取网页文献元数据

                                        retorque.re/zotero-better-
        Better BibTeX 插件                                             自动生成 Citation Key
                                        bibtex
        Zotero PDF Translate            Zotero 插件市场搜索                PDF 内划词翻译

       📂 文献库结构设计（按课题组织）
           📂 国社科课题：文化遗产旅游知识服务

第 2 课B — 英文文献检索与综述                                                                         2


---

              📁 论文 1：目的地形象 × 多模态 AI
              📁 论文 2：知识图谱 × RAG × 智能问答
              📁 论文 3：跨文化交际 × 入境旅游
              📁 理论框架（共用）
              📁 方法论参考
              📁 最新进展（2024–2026）
       📍 模块三：Connected Papers 文献网络图（10 分钟）
       操作流程：

        1. 访问 connectedpapers.com
        2. 输入种子论文标题或 DOI
        3. 系统生成引用网络图：
              🟢 核心文献（大节点）：必读的高被引论文
              🔵 前驱工作（Prior Works）：奠基文献
              🟡 衍生工作（Derivative Works）：最新进展
        4. 点击感兴趣的论文 → 保存到 Zotero


         💡    替代工具推荐： Litmaps 和 ResearchRabbit 提供类似功能。
              ResearchRabbit 被誉为"学术界的 Spotify"，能根据你的文献库自动推荐
              相关论文。




       📍 模块四：文献计量学与科学地图·VOSviewer & Pajek
       （10 分钟）

         🗺️   科学地图（Science Mapping） 是文献计量学的可视化分支，通过分析引
              用关系、共现网络等揭示学科结构与演进趋势。第 2 课A 介绍了
              CiteSpace（侧重中文文献），本模块聚焦国际主流工具 VOSviewer 和
              Pajek，适用于英文文献的大规模计量分析。




第 2 课B — 英文文献检索与综述                                            3


---

       🔧 三大工具对比
        工具            核心优势      适用数据源            学习曲线    费用

                                Web of
                      界面友好、密度
                                Science、
        🟢 VOSviewer   可视化出色、适
                      合关键词共现与
                                Scopus、          ⭐低      🆓 免费
                                PubMed、
                      引文网络
                                Crossref、Lens
                      超大规模网络分

        🔵 Pajek       析（百万节点）
                            、
                      社区检测算法丰
                                任意网络数据
                                （需转换格式）
                                                 ⭐⭐⭐ 高   🆓 免费
                      富

                      突现词检测、时   知网
        🟣 CiteSpace   间线视图、中文   （Refworks）
                                         、       ⭐⭐ 中    🆓 收费
                      文献支持最佳    Web of Science

       📊 VOSviewer 操作流程




第 2 课B — 英文文献检索与综述                                              4


---

                                📥 导出文献数据
                                 WoS / Scopus




                               📂 导入 VOSviewer
                                 选择分析类型




                                 ⚙️ 设置参数
                                阈值/聚类/时间




                                🗺️ 生成可视化
                                网络/叠加/密度图




                                📸 导出高清图
                                 用于论文插图




       VOSviewer 五种核心分析：
        分析类型              用途                课题应用示例

        📈 关键词共现           发现研究热点主题与聚类
                                            "cultural heritage tourism" +
        （Co-occurrence）                     "AI" 领域的国际热点关键词

        👥 作者合作（Co- 识别核心研究团队与国际合作 哪些国际学者      /机构在
                                 做"multilingual knowledge
        authorship）       网络
                                            service"？
        📚 共被引（Co-         发现知识基础与理论源头
                                            destination image 研究的经典理
        citation）                           论来源（Baloglu、Pike 等）

        📖 文献耦合                              2024–2026 年 GenAI +
        （Bibliographic    发现当前活跃的研究前沿
                                            tourism 的最新研究前沿在哪？
        Coupling）



第 2 课B — 英文文献检索与综述                                                          5


---

        分析类型              用途                 课题应用示例

        🌍 叠加可视化           按时间着色，展示主题演进
                                             "inbound tourism" 研究从传统
        （Overlay）                            营销→数字化→AI 的演进

           💡 VOSviewer 实操小贴士
           1. 数据导出：Web of Science → 检索结果 → Export → Plain Text File → Full
              Record and Cited References
           2. Scopus 导出：检索结果 → Export → CSV → 选择 Citation information +
              Bibliographical information + Abstract & keywords
           3. 推荐阈值：关键词共现 ≥ 5 次；作者合作 ≥ 3 篇；根据文献总量调整
           4. 图片导出：File → Save → 选择 PNG（300 dpi），直接用于论文插图
           5. 下载地址：VOSviewer 官网（Java 版 + 在线版均可）

       🕸️ Pajek：超大规模网络分析
         🔵    Pajek 是斯洛文尼亚学者 Vladimir Batagelj 和 Andrej Mrvar 开发的大规模
              网络分析工具，擅长处理百万级节点的复杂网络。在文献计量学中主要用
              于：

                     📐 社区检测：发现学术研究的隐性子群体
                     🔀 网络拓扑分析：识别桥接节点（跨学科关键文献）
                     📊 与 VOSviewer 互补：VOSviewer 出可视化图 → Pajek 做深度网络
                     统计




第 2 课B — 英文文献检索与综述                                                           6


---

         🤖      AI + 文献计量学实战技巧：
                     🧠 AI 解读计量图谱：将 VOSviewer 生成的密度图截图上传到 GPT-
                     4o / Kimi，AI 自动识别聚类主题并生成英文分析段落
                     📝 AI 撰写 Bibliometric 段落：基于 VOSviewer 统计数据（文献量、
                     国家分布、高频词），用提示词生成论文的 "Bibliometric Overview" 部
                     分

                     🔍 AI 辅助数据清洗：用 DeepSeek 合并 VOSviewer 中的同义关键词
                     （如 "AI" 与 "artificial intelligence"）

                     📊 趋势融合：CiteSpace 看中文趋势 + VOSviewer 看国际趋势 → AI
                     生成中英文对比分析




       📍 模块五：国际期刊分区体系概览（5 分钟）
        📮       🔗
                为第 6 课投稿做铺垫 —— 了解国际期刊的分区评价体系，有助于在英
                文文献检索阶段就关注高质量来源，也为后续选刊投稿打好基础。


       🌍 国际期刊两大评价体系
        体系               发布机构              核心指标              分区方式

        📕 JCR 分区         Clarivate（科睿唯 Impact Factor（IF）：
                         安）                期刊影响因子
                                                             按学科排名分为 Q1（前
                                                             25%）、Q2、Q3、Q4
                                                             按学科分为 1 区（前
        📗 中科院分区          中国科学院文献情
                         报中心
                                           综合 IF + 他引率 + 总
                                           被引等多项指标
                                                             5%）、2 区、3 区、4 区
                                                             （大类/小类）


       📚 SCI / SSCI / AHCI / ESCI 索引体系
        索引               全称                覆盖领域              课题相关说明

        🔬 SCI            Science
                         Citation Index
                                           自然科学（理工医）
                                                             计算机/AI 类论文可发
                                                             SCI
                                                             课题三篇论文的主要目标
        📊 SSCI           Social Sciences
                         Citation Index
                                           社会科学（管理、教育、
                                           经济、语言学等）
                                                             （旅游管理、情报学、翻
                                                             译学）




第 2 课B — 英文文献检索与综述                                                             7


---

        索引               全称               覆盖领域               课题相关说明

                         Arts &
        📖 AHCI           Humanities
                                          艺术与人文（文学、历
                                          史、哲学等）
                                                             文化遗产相关论文可考虑
                         Citation Index
                         Emerging
        🆕 ESCI           Sources
                                          新兴优质期刊（正在被评
                                          估纳入 SCI/SSCI）
                                                             新创期刊的"孵化器"，录
                                                             用率相对较高
                         Citation Index

       🎯 课题三篇论文的国际目标期刊定位
         🎯           论文 1（旅游+AI）→ Tourism Management（SSCI Q1, IF ≈ 12.9）/
                     Annals of Tourism Research（SSCI Q1）
                     论文 2（AI+多语种）→ JASIST（SSCI Q1, IF ≈ 3.5）/ Information
                     Processing & Management（SSCI Q1）
                     论文 3（跨文化+入境）→ Annals of Tourism Research（SSCI Q1）/
                     Tourism Management（SSCI Q1）
                     备选：Journal of Hospitality and Tourism Technology（SSCI
                     Q2）、Current Issues in Tourism（SSCI Q2）



         💡    检索阶段的选刊意识： 在 OpenAlex / Semantic Scholar / 知网（CNKI） / Semantic Scholar 检索英文
              文献时，留意论文发表期刊的 JCR 分区和 IF——优先引用 Q1/Q2 期刊的文
              献，这些也是你未来投稿的潜在目标。第 6 课将系统讲解 AI 期刊匹配三步
              法与投稿全流程。




       📍 模块六：ima.copilot（腾讯智能工作台）/ Kimi 知识库 / 本地 iScholar RAG 深度文献阅读（10 分钟）
        📓     ima.copilot（腾讯智能工作台）/ Kimi 知识库 / 本地 iScholar RAG 是 Google 推出的零代码 RAG 工具——上传论文后，AI 回
              答严格基于你的文献，零幻觉，每句话可溯源。
              ⚠️注意：ima.copilot（腾讯智能工作台）/ Kimi 知识库 / 本地 iScholar RAG 需科学上网访问。 由于北京市最新网络管理要
              求，请勿使用个人 VPN，等待学校正规外网渠道通知。在此期间可使用
              Kimi（长文档分析） 或 DeepSeek 作为替代方案。




第 2 课B — 英文文献检索与综述                                                           8


---

       实操步骤：

        1. 打开 notebooklm.google.com → 新建 Notebook
        2. 上传 5–10 篇核心英文 PDF
        3. 提问示例：
               "What methods are used to analyze destination image in social media?"


               "How do knowledge graphs improve multilingual information retrieval?"

               "Summarize the research gaps across all uploaded papers."


        4. AI 回答 + 精确引用标注 → 复制到 Obsidian + Hermes（OpenCode / DeepSeek Harness） 综述素材

       📍 模块七：英文文献综述写作（10 分钟）
       OCAR 模型：经典综述段落结构
        步骤                   含义                            功能

        O — Overview         概述研究领域现状                      为读者建立背景认知

        C — Contributions    指出关键文献贡献                      综合多篇文献的核心发现

        A — Arguments        讨论学术争议点                       呈现不同观点与矛盾

        R — Research Gap     指出现有研究空白                      为你的研究提供合理性


       ✍️ AI 辅助综述写作提示词




第 2 课B — 英文文献检索与综述                                                                     9


---

         💬       Prompt：英文综述段落生成
                 You are a senior researcher in [tourism management / information
                 science / applied linguistics]. Based on the following literature
                 summaries, write a literature review paragraph (about 200 words) on
                 [sub-topic]. Requirements:
                 1. Start with a topic sentence that states the main argument
                 2. Synthesize (not list) findings from multiple studies
                 3. Highlight agreements and disagreements
                 4. End with a clear research gap statement
                 5. Use APA 7th citation format
                 [Paste literature summaries]



       📍 模块八：学术伦理（5 分钟）
        🔴 ❌ 🚨    学术伦理红线

                       绝对不能：让 AI 编造你没读过的英文文献引用（AI 会虚构 DOI 和
                     作者名！）

                     ❌ 绝对不能：直接复制 AI 生成的综述作为最终稿
                     ✅ 正确做法：AI 生成框架和草稿 → 你逐条核实引用 → 你用自己的语
                     言重写 → 标注 AI 辅助声明




       📝 课后作业
        任务                     具体要求                                        分值

                               为你选定的论文方向建立 Zotero Collection，收
        任务 1：Zotero 文献库                                                    5分
                               录至少 15 篇英文文献

        任务 2：Connected         以种子论文生成文献网络图，截图保存，标注核
                                                                           5分
        Papers                 心/前驱/衍生文献

        任务 3：ima.copilot（腾讯智能工作台）/ Kimi 知识库 / 本地 iScholar RAG        上传 5 篇核心论文，提出 3 个跨文献问题，记录
                                                                           5分
        问答                     AI 回答


第 2 课B — 英文文献检索与综述                                                                     10


---

        任务                   具体要求                               分值

                             用 OCAR 模型撰写 500 词英文文献综述段落（1
        任务 4：英文综述初稿                                             5分
                                 ，附 AI 使用声明
                             个子主题）



       🔮 下节预告
        🏗️    第 3 课A — 研究设计基础·文科常用方法入门

                     定量/定性/混合方法入门

                     研究问题（RQ）的规范表述

                     AI 辅助生成"研究设计一页纸"



       🗺️
       实战
          附录：CiteSpace · VOSviewer · Pajek 科学计量分析


         🎯    研究课题： 生成式 AI 驱动的北京文化遗产旅游目的地形象多模态构建——
              基于小红书与 TripAdvisor 的跨平台比较研究
              目标： 使用三大文献计量工具对该课题相关文献进行系统性的科学知识图
              谱与科学地图分析，揭示研究热点、演进趋势、核心作者/机构网络与研究
              前沿。




       📍 Step 1：数据采集与预处理（三工具通用）
         📥    数据是科学计量分析的基石。 三个工具使用的数据来源和格式略有不同，
              需分别导出。


       1.1 检索策略设计

        数据库             检索式（英文）                    检索式（中文·知网）

        🔬 Web of        TS=("destination image"    —
        Science         OR "tourism perception")
                        AND TS=("generative AI"


第 2 课B — 英文文献检索与综述                                                   11


---

        数据库              检索式（英文）                      检索式（中文·知网）
                         OR "large language model"
                         OR "multimodal" OR
                         "UGC") AND TS=("cultural
                         heritage" OR "Beijing")
                         TITLE-ABS-
                         KEY("destination image"
                         AND ("generative AI" OR
        📊 Scopus         "multimodal") AND ("social   —
                         media" OR "UGC" OR
                         "Xiaohongshu" OR
                         "TripAdvisor"))
                                                      SU=("目的地形象" + "旅游感知")
        📚 知网 CNKI        —
                                                      AND SU=("生成式AI" + "多模态" +
                                                      "用户生成内容") AND SU=("文化遗
                                                      产" + "北京")



         💡    扩展检索技巧：

                     第一轮用核心词检索，第二轮扩展同义词（如 "AI-generated content"
                     "AIGC" "text-to-image"）
                     时间范围建议：2015–2026（覆盖深度学习兴起至今）

                     文献类型：Article + Review（排除会议摘要和书评）

                     预计检索量：WoS 300–800 篇，Scopus 500–1200 篇，知网 200–
                     500 篇


       1.2 数据导出格式

        工具               数据源                 导出格式                     导出要求

                                             WoS: Plain Text (Full
        🟣 CiteSpace      WoS / 知网
                                             Record + Cited
                                             References)
                                                                      每次最多 500 条，分
                                                                      批导出后合并
                                             知网: Refworks 格式

        🟢 VOSviewer      WoS / Scopus /      WoS: Plain Text (Tab-    单文件最大 10,000 条
                         PubMed              delimited, Full Record
                                             + Cited References)
                                             Scopus: CSV (含



第 2 课B — 英文文献检索与综述                                                                     12


---

        工具           数据源          导出格式                    导出要求
                                  Citation + Abstract +
                                  Keywords)
                                                          通常从 VOSviewer /
        🔵 Pajek      任意（需转换）
                                  .net 网络文件 + .clu 分
                                  区文件
                                                          CiteSpace 导出网络后
                                                          转换


       1.3 数据清洗流程



                                📥 原始数据
                           WoS + Scopus + 知网




                                  🔄 去重
                            基于 DOI / 标题匹配




                                  ✂️ 清洗
                                同义词合并
                                机构名标准化




                                 📊 统计概览
                               年份/国家/期刊分布




                                 💾 分别保存
                           CiteSpace / VOSviewer /
                                 Pajek 格式




第 2 课B — 英文文献检索与综述                                                          13


---

         🤖    AI 辅助清洗： 用 DeepSeek / GPT 合并同义关键词（如 "AI" 与 "artificial
              intelligence"、"destination image" 与 "destination branding"、"小红
              书" 与 "Xiaohongshu" 与 "RED"）。可将关键词列表粘贴给 AI，让其输出
              合并映射表。




       📍 Step 2：CiteSpace 分析（中文文献优势）




         🟣    CiteSpace（陈超美教授开发）擅长 突现词检测（Burst Detection） 和
              时间线视图（Timeline View），是中文文献计量的首选工具。
              下载： citespace.podia.com（需 Java 环境）
              学习资源： 6.4.R1 Demo Video（示范视频）（         ⚠️YouTube 需科学上网）
              ｜ Visual Analytic Studies of Science（学术讲座）（ ⚠️YouTube 需科学
              上网）


       2.1 CiteSpace 操作流程




第 2 课B — 英文文献检索与综述                                                             14


---

                              📂 导入数据
                          WoS/知网 Refworks




                              ⚙️ 参数设置
                             时间切片/阈值




                           🔍 选择分析类型
                          关键词/作者/机构/引文




                           🗺️ 生成知识图谱
                             Cluster View




                           📈 突现词检测
                           Burst Detection




                           ⏳ 时间线视图
                           Timeline View




                            📸 导出图谱
                             PNG/SVG




       2.2 CiteSpace 参数配置（本课题推荐）




第 2 课B — 英文文献检索与综述                           15


---

        参数                   推荐设置                          说明

                             2015–2026，Years Per           覆盖深度学习兴起到 GenAI
        Time Slicing
                             Slice = 1                     爆发期

                             依次选择：Keyword /
        Node Types           Author / Institution /        每种类型单独运行一次
                             Reference
                             Top N = 50 per slice 或 g-
        Selection Criteria                                 平衡节点数量与可读性
                             index (k=25)
                             Pathfinder + Pruning sliced
        Pruning                                            精简网络，突出核心路径
                             networks
                             Cluster View → Timeline
        Visualization                                      三种视图依次生成
                             View → Burst Detection

       2.3 CiteSpace 六大分析任务

       分析 1：关键词共现与聚类（Keyword Co-occurrence & Clustering）

           操作： Node Type → Keyword → 运行 → 自动聚类（LLR / LSI / MI 算法）

           解读要点：

               节点大小 = 频次，连线粗细 = 共现强度

               聚类标签揭示研究主题群：如 "#0 destination image", "#1 social media
               analytics", "#2 cultural heritage tourism", "#3 multimodal content", "#4
               generative AI"
               中介中心性（Betweenness Centrality）≥ 0.1 的节点为关键枢纽词

           本课题预期聚类：




第 2 课B — 英文文献检索与综述                                                                        16


---

                                             #2 cultural heritage
                                                文化遗产旅游




                                            #0 destination image
                                                目的地形象




                                            #1 social media UGC
                                             社交媒体用户内容




                               #3 multimodal analysis               #5 cross-platform
                                    多模态分析                              跨平台比较




                                     #4 generative AI
                                     生成式人工智能




       分析 2：突现词检测（Burst Detection）

           操作： 关键词共现图谱 → Burstness → 查看突现词列表

           解读要点： 突现词代表某时间段内急剧升温的研究热点

           本课题预期突现词示例：

        突现词             强度                   起始                         结束              解读

                                                                                        深度学习引入旅
        deep learning   5.82                 2018                       2021
                                                                                        游研究

                                                                                        情感分析成为
        sentiment
                        4.15                 2019                       2022            UGC 研究主流方
        analysis
                                                                                        法

                                                                                        🔥 当前最强突现
        generative AI   8.73                 2023                       2026            ——GenAI 重塑
                                                                                        旅游研究

        multimodal      6.41                 2024                       2026
                                                                                        🔥 多模态分析成
                                                                                        为新趋势

                                                                                        🔥 小红书作为旅
        Xiaohongshu     3.92                 2024                       2026            游 UGC 平台受
                                                                                        关注

       分析 3：时间线视图（Timeline View）


第 2 课B — 英文文献检索与综述                                                                                   17


---

           操作： Cluster View → Layout → Timeline View

           解读： 横轴为时间，纵轴为聚类，展示各研究主题的兴起、发展与衰退

           本课题预期时间线：


          gantt
             title 研究主题时间线演进（CiteSpace Timeline View 示意）
            dateFormat YYYY
            axisFormat %Y
            section #0 目的地形象
                经典认知-情感模型                   :2015, 2019
                社交媒体 DI 研究                   :2018, 2023
                AI 驱动 DI 构建                    :2023, 2026
            section #1 社交媒体 UGC
                评论文本分析                      :2016, 2020
                图文多模态分析                     :2020, 2024
                生成式内容分析                     :2024, 2026
            section #2 文化遗产旅游
                数字化保护                         :2015, 2020
                智慧旅游                          :2019, 2024
                AI + 文化遗产                      :2023, 2026
            section #3 多模态分析
                图像识别                           :2018, 2022
                CLIP/多模态模型                    :2022, 2025
                GPT-4V/Gemini 视觉              :2024, 2026
            section #4 生成式 AI
                GPT-3/DeepSeek                        :2022, 2024
                多模态生成                         :2024, 2026

                                                      研究主题时间线演进（CiteSpace Timeline View 示意）

                                                   经典认知-情感模型

                              #0 目的地形象                                       社交媒体 DI 研究

                                                                                                                    AI 驱动 DI 构建

                                                             评论文本分析

                              #1 社交媒体 UGC                                                  图文多模态分析

                                                                                                                           生成式内容分析

                                                        数字化保护

                              #2 文化遗产旅游                                                智慧旅游

                                                                                                                     AI + 文化遗产

                                                                             图像识别

                              #3 多模态分析                                                                  CLIP/多模态模型

                                                                                                                       GPT-4V/Gemini 视觉

                                                                                                    GPT-3/DeepSeek
                              #4 生成式 AI
                                                                                                                           多模态生成

                                     2015   2016      2017     2018   2019   2020   2021     2022       2023        2024     2025     2026




       分析 4：作者合作网络（Author Collaboration）

           操作： Node Type → Author → 运行

           解读： 识别高产作者、核心研究团队、跨机构合作关系

           关注 发文量 Top 10 作者 和 中介中心性高的桥接作者

       分析 5：机构合作网络（Institution Collaboration）

           操作： Node Type → Institution → 运行




第 2 课B — 英文文献检索与综述                                                                                                                           18


---

           解读： 哪些大学/机构是该领域的研究重镇？哪些机构间有密切合作？

       分析 6：文献共被引分析（Document Co-citation）

           操作： Node Type → Cited Reference → 运行

           解读： 发现知识基础（被共同引用的经典文献），如 Baloglu & McCleary
           (1999)、Pike (2002)、Stepchenkova & Zhan (2013) 等目的地形象研究奠基之
           作

       2.4 CiteSpace 输出示例图

                                                        📊 CiteSpace 输出成果
                          ⏳ 时间线视图         👥 作者合作网络     📚 共被引聚类图              🔑关键词共现聚类图              📈 突现词时间条形图
                         2015-2026 主题演进    Top 50 作者    知识基础结构             6个聚类 · Q=0.82 · S=0.91     Top 25 突现词




                                                                                   聚类质量               前沿识别



                                                                                  Q > 0.7✅          generative AI
                                                                                  S > 0.5✅           multimodal
                                                                                 聚类结构显著             Xiaohongshu
                                                                                                    为最新突现词




       📍 Step 3：VOSviewer 分析（国际文献可视化）




第 2 课B — 英文文献检索与综述                                                                                                  19


---

         🟢    VOSviewer（Leiden 大学 Nees Jan van Eck 团队开发）以密度可视化和
              叠加可视化见长，界面友好，适合国际英文文献分析。
              下载： vosviewer.com（Java 版 + 在线版均可）


       3.1 VOSviewer 操作流程




第 2 课B — 英文文献检索与综述                                                20


---

                                  📥 导入数据
                               WoS Tab-delimited
                                或 Scopus CSV




                                📋 选择分析类型
                                  Co-occurrence
                                  Co-authorship
                                    Co-citation
                              Bibliographic coupling




                                  ⚙️ 设置阈值
                                最低频次/文献数




                                 🗺️ 生成可视化
                          Network / Overlay / Density




                                 🎨 调整布局
                                颜色/标签/缩放




                                📸 导出高清图
                                 PNG 300dpi




       3.2 VOSviewer 五大分析任务

       分析 1：关键词共现网络（Co-occurrence → All Keywords）




第 2 课B — 英文文献检索与综述                                      21


---

           操作： Create → Based on bibliographic data → 选择 WoS/Scopus 文件 →
           Co-occurrence → All keywords → 最低出现次数设为 5
           三种视图切换：

        视图类型           特色                                                         本课题解读

                                                                                  "destination image" 与 "social
        🔵 Network      节点 + 连线，颜色区分聚类                                             media" 连线最粗，说明两者共现
                                                                                  频率最高

                                      "generative AI" "multimodal" 显
        🌈 Overlay      按时间着色（蓝→黄=早→近） 示为黄色（2024–2026）        ，是最新
                                                                                  热点

                                                                                  "destination image" "cultural
        🔴 Density      热力图，红色=高密度区域                                               heritage" "tourist perception" 为
                                                                                  高密度核心区

           本课题关键词网络示意：


                                                                                                    🟣 generative AI
                                                                                                          频次: 87




                                          🔴 destination image
                                               频次: 285




                            🟠 social media                🟠 Xiaohongshu           🟢 cultural heritage
                              频次: 210                           频次: 32                频次: 142




                             🟡 TripAdvisor             🟡 user-generated content         🔴 Beijing tourism
                                频次: 198                         频次: 156                      频次: 45




                                             🔵 sentiment analysis                                       💜 multimodal
                                                   频次: 118                                                频次: 63




       分析 2：作者合作网络（Co-authorship → Authors）

           操作： Co-authorship → Authors → 最低文献数设为 3

           解读： 识别该领域的核心研究团队和国际合作模式

           节点越大 = 发文量越多；连线越粗 = 合作越频繁

           不同颜色聚类 = 不同研究团队/合作圈

       分析 3：国家/地区合作网络（Co-authorship → Countries）

           操作： Co-authorship → Countries → 最低文献数设为 5




第 2 课B — 英文文献检索与综述                                                                                                     22


---

           本课题预期： 中国、美国、英国、澳大利亚、韩国为高产国家；中-美、中-英合
           作线最粗

       分析 4：期刊共被引分析（Co-citation → Sources）

           操作： Co-citation → Cited Sources → 最低引用数设为 20

           解读： 揭示该领域的核心期刊群

           本课题预期核心期刊：

        期刊                           被引次数   在本课题中的角色

        Tourism Management           ~520   目的地形象研究核心阵地

        Annals of Tourism
                                     ~480   旅游理论与方法论重镇
        Research
        Journal of Travel Research   ~350   旅游消费者行为研究

        International Journal of
                                     ~280   酒旅管理与技术应用
        Hospitality Management
        Computers in Human
                                     ~190   社交媒体与用户行为
        Behavior
       分析 5：文献耦合分析（Bibliographic Coupling → Documents）

           操作： Bibliographic coupling → Documents → 最低引用数设为 10

           解读： 揭示当前活跃的研究前沿（引用相同参考文献的论文构成研究前沿群）

           与共被引互补：共被引看「知识基础」，文献耦合看「研究前沿」

       3.3 VOSviewer 叠加可视化（Overlay）解读模板




第 2 课B — 英文文献检索与综述                                               23


---

         🌈    Overlay 视图是 VOSviewer 的核心优势——按发表年份着色，直观展示研
              究演进：

                     🔵 蓝色节点（2015–2019）：经典主题（destination image、tourism
                     marketing、content analysis）
                     🟢 绿色节点（2020–2022）：过渡主题（deep learning、sentiment
                     analysis、Instagram）
                     🟡 黄色节点（2023–2026）：前沿主题（generative AI、
                     multimodal、Xiaohongshu、GPT-4V）
              论文写作用法： 截图 + 描述 "As shown in the overlay visualization
              (Figure X), the research focus has shifted from traditional content
              analysis (blue) to AI-driven multimodal approaches (yellow) since
              2023."

       3.4 VOSviewer 密度可视化（Density）解读模板


         🔴    Density 视图用颜色深浅表示关键词/作者的聚集密度：
                     🔴 红色高密度区："destination image" + "tourist perception" +
                     "social media" = 研究最集中的核心区
                     🟡 黄色中密度区："cultural heritage" + "cross-cultural" = 稳定增长
                     的研究区

                     🟢 绿色低密度区："generative AI" + "multimodal" +
                     "Xiaohongshu" = 尚待开发的研究蓝海 🎯
              关键发现： 密度图清晰显示 "generative AI" 与 "cultural heritage
              tourism" 之间存在密度洼地——这正是本课题的研究空白！


       📍 Step 4：Pajek 深度网络分析（超大规模 + 拓扑指标）



第 2 课B — 英文文献检索与综述                                                                  24


---

         🔵     Pajek（斯洛文尼亚语"蜘蛛"）擅长超大规模网络分析（百万级节点）和精
               确的网络拓扑指标计算。与 VOSviewer 的「可视化优先」互补，Pajek 提
               供「统计优先」的深度分析。
               下载： mrvar.fdv.uni-lj.si/pajek（免费，Windows）


       4.1 Pajek 数据准备

          graph
             A["📥 VOSviewer 网络<br>导出 GML/Pajek 格式"] --> B["🔄 格式转换<br>.net + .clu + .ve
         c"]
             B --> C["📂 导入 Pajek<br>File → Network → Read"]
             C --> D["⚙️网络分析<br>拓扑指标计算"]
             D --> E["📊 社区检测<br>Louvain / VOS 聚类"]
             E --> F["📈 统计输出<br>度分布/中心性报告"]
             style A fill:#E3F2FD,stroke:#1565C0
             style D fill:#1565C0,stroke:#0D47A1,color:#fff
             style F fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px




第 2 课B — 英文文献检索与综述                                                                       25


---

                                       📥 VOSviewer 网络
                                       导出 GML/Pajek 格式




                                           🔄 格式转换
                                         .net + .clu + .vec




                                          📂 导入 Pajek
                                     File → Network → Read




                                          ⚙️ 网络分析
                                          拓扑指标计算




                                          📊 社区检测
                                       Louvain / VOS 聚类




                                          📈 统计输出
                                       度分布/中心性报告




         💡    数据转换路径：

                     VOSviewer → File → Save → Pajek 格式 (.net)
                     CiteSpace → Export → Network → Pajek 格式
                     或使用 Python networkx 库： nx.write_pajek(G, "network.net")



       4.2 Pajek 四大核心分析

第 2 课B — 英文文献检索与综述                                                             26


---

        分析类型              操作路径                                                                      本课题应用

        📐 度分布分析           Net → Partitions → Degree
                                                                                                    识别关键词网络是否符合幂律分
        （Degree                                                                                     布（无标度网络特征），验证少数
                          → All
        Distribution）                                                                               核心关键词主导研究

                                                                                                    发现桥接节点：连

        🎯 中心性分析           Net → Partitions →         接"destination
                          Centrality → Betweenness / image"与"generative AI"两大社
        （Centrality）
                          Closeness                  区的关键词（如"multimodal
                                                     analysis"）
        🏘️ 社区检测           Net → Partitions →
                                                                                                    自动划分研究子群体，与
        （Community                                                                                  CiteSpace/VOSviewer 聚类结
                          Communities → Louvain
        Detection）                                                                                  果三角验证

                                                                                                    区分核心研究主题（destination
        🌉 核心-边缘分析        Net → Partitions →                                                         image, social media）与边缘新
        （Core-Periphery） Core/Periphery                                                             兴主题（Xiaohongshu, GenAI
                                                                                                    multimodal）

       4.3 Pajek 网络拓扑指标输出

        指标                   预期值                                        解读

                                                                        中等密度，说明研究主题间有一定关联但
        网络密度（Density）        0.05–0.15
                                                                        未过度重叠

        平均路径长度（Avg                                                      "小世界"特征，任意两个关键词通过 2-3
                             2.5–3.5
        Path Length）                                                    步可达

        聚类系数（Clustering
                             0.3–0.6                                    高聚类 = 研究主题形成明显的子群体
        Coefficient）
        模块度（Modularity
                             > 0.4                                      社区结构显著，Q > 0.3 即有意义
        Q）

       4.4 Pajek 核心-边缘分析示意

                                                                      🔴 核心区 Core
                            social media   TripAdvisor           tourist perception             destination image   cultural heritage




                                             🔵 边缘区 Periphery（新兴
                                                         前沿）


                                 GPT-4V     Xiaohongshu                         generative AI




                                                    cross-platform            multimodal




第 2 课B — 英文文献检索与综述                                                                                                                      27


---

         🎯    核心发现： Pajek 核心-边缘分析显示，"generative AI" 和 "multimodal"
              正从边缘区向核心区迁移，但 "Xiaohongshu" 作为平台尚处于边缘——这
              意味着基于小红书的生成式 AI 旅游研究是一个高价值的学术蓝海。




       📍 Step 5：三工具交叉验证与综合分析
         🔀    三角验证（Triangulation） 是提升文献计量分析可信度的关键——用三个
              工具从不同角度分析同一数据集，互相印证结论。


       5.1 三工具分析结果对照表

        分析维度          CiteSpace           VOSviewer             Pajek
                      突现词：generative      Overlay 黄色节点：         度中心性 Top 5
        研究热点          AI (8.73)、          generative AI、        新增：generative
                      multimodal (6.41)   Xiaohongshu           AI
                                          共被引网络：                核心区：
                      共被引聚类：Baloglu      Tourism        destination
        知识基础
                      (1999)、Pike (2002) Management 最大节 image、social
                                         点              media
                                          文献耦合：2024–            边缘区→核心区迁
                      时间线：2024–2026
        研究前沿                              2025 论文集中于            移：multimodal
                      GenAI + 多模态
                                          AI+tourism            analysis
                      无突现词涉及「跨平           密度洼地：GenAI 与          桥接中心性低：缺
        研究空白          台+GenAI+文化遗         cultural heritage 之   乏连接两大社区的
                      产」三者交叉              间                     研究

                      时间线 + 突现词条形                               精确拓扑指标 +
        可视化优势                             密度图 + 叠加时间图
                      图                                         核心-边缘结构


       5.2 综合结论与研究启示




第 2 课B — 英文文献检索与综述                                                              28


---

                                                      🟣 CiteSpace    🟢 VOSviewer          🔵 Pajek
                                                       突现词检测             密度洼地            核心-边缘分析




                                                                    🎯 研究空白确认

                             ✅ 结论 1：generative AI +       ✅ 结论 2：小红书作为旅             ✅ 结论 3：跨平台（中外平    ✅ 结论 4：多模态分析方法
                                  文化遗产旅游                                                  台）比较研究          正从边缘
                                                              游 UGC 平台
                             是 2024–2026 最强突现方                                      在 AI 驱动目的地形象领域几   走向核心，但与文化遗产结
                                                            的学术研究严重不足
                                      向                                                    乎空白            合不足




                                                                                    🔬 本课题的研究问题
                                                                                   因此具有高度的创新性与学
                                                                                        术价值




       📍 Step 6：论文写作中的引用模板
         ✍️   将科学计量分析结果写入论文的标准表述模板：



       引言/文献综述部分（Bibliometric Overview 段落模板）：

         To systematically map the intellectual landscape of AI-driven destination
         image research, we conducted a bibliometric analysis using CiteSpace
         (v.6.3.R1), VOSviewer (v.1.6.20), and Pajek (v.5.18). A total of [N] publications
         were retrieved from Web of Science Core Collection and Scopus (2015–
         2026). Keyword co-occurrence analysis in VOSviewer revealed six major
         clusters, with "destination image," "social media," and "cultural heritage"
         forming the high-density core. CiteSpace burst detection identified
         "generative AI" (burst strength = 8.73, 2023–2026) and "multimodal" (burst
         strength = 6.41, 2024–2026) as the strongest emerging keywords. Pajek
         core-periphery analysis further confirmed that generative AI-related topics
         are transitioning from the periphery to the core of the research network.
         Notably, the intersection of generative AI, cultural heritage tourism, and
         cross-platform comparison (e.g., Xiaohongshu vs. TripAdvisor) represents a
         significant research gap, which this study aims to address.
       方法部分（Bibliometric Method 段落模板）：

         The bibliometric analysis followed a three-tool triangulation approach: (1)
         CiteSpace for burst detection and timeline visualization of research
         evolution; (2) VOSviewer for keyword co-occurrence network, overlay, and
         density visualization; (3) Pajek for network topology metrics (density,
         clustering coefficient, modularity) and core-periphery structure analysis.
         Data were collected from Web of Science (n = [X]) and Scopus (n = [Y]),


第 2 课B — 英文文献检索与综述                                                                                                     29


---

         deduplicated based on DOI, and cleaned using AI-assisted synonym
         merging. The PRISMA 2020 guidelines were followed for transparent
         reporting of the literature selection process.

       📍 Step 7：完整工作流总结
                                                           📥Step 1
                                                      数据采集与预处理
                                                     WoS + Scopus + 知网




                               🟣   Step 2                  🟢
                                                         Step 3
                                                                                    🔵 Step 4
                                                                                   Pajek 分析
                             CiteSpace 分析           VOSviewer 分析
                                                                                拓扑指标 + 社区检测 + 核
                           突现词 + 时间线 + 共被引        共现网络 + 密度图 + 叠加图
                                                                                    心-边缘




                                                           🔀
                                                           Step 5
                                                        三工具交叉验证
                                                        综合分析与结论




                                                   ✍️   Step 6
                                                    论文写作
                                             Bibliometric Overview +
                                                     Method




                                                   📸 Step 7
                                                   图表整理
                                             6-8 张高清图谱 + 统计表




       📸 论文建议配图清单（6–8 张）
        编号            图表内容                                             工具来源                  论文位置

        Fig. 1        年度发文量趋势图                                         Excel / Python        Bibliometric Overview
                      关键词共现网络图
        Fig. 2                                                         VOSviewer             Literature Review
                      （Network View）

                      关键词叠加时间图
        Fig. 3                                                         VOSviewer             Literature Review
                      （Overlay View）

                      关键词密度图（Density                                                         Literature Review /
        Fig. 4                                                         VOSviewer
                      View）                                                                  Discussion
        Fig. 5        突现词 Top 25 时间条形图                                 CiteSpace             Literature Review
        Fig. 6        关键词聚类时间线视图                                       CiteSpace             Literature Review
        Fig. 7        核心-边缘结构图                                         Pajek                 Discussion
                      三工具交叉验证综合结论                                      Mermaid / AI 制
        Fig. 8                                                                               Discussion / Conclusion
                      图                                                图




第 2 课B — 英文文献检索与综述                                                                                                     30


---

         🎓    实操建议：

               1. 先 VOSviewer（5 分钟出图）→ 再 CiteSpace（突现词+时间线独有
                  优势）→ 最后 Pajek（精确拓扑指标补充）

               2. 所有图谱导出为 PNG 300dpi，直接用于论文插图
               3. 用 AI（GPT-4o / Kimi）上传截图 → 自动生成英文图谱解读段落
               4. 参考期刊：Scientometrics、Journal of Informetrics 的文献计量论文
                     格式




第 2 课B — 英文文献检索与综述                                                      31


---

