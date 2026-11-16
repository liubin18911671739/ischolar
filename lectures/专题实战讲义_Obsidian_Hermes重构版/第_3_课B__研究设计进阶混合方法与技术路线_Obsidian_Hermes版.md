---
title: "第_3_课B__研究设计进阶混合方法与技术路线_Obsidian_Hermes版"
workflow: "Obsidian + Hermes (OpenCode / DeepSeek Harness) + iScholar"
software_policy: "国产软件 + 开源软件（零翻墙）"
---

# 第_3_课B__研究设计进阶混合方法与技术路线_Obsidian_Hermes版

> **工具栈说明**：本讲义将传统云端知识库工作流全面重构为 **Obsidian Vault + Hermes（OpenCode 或 DeepSeek Harness）+ 本地 iScholar 应用（Streamlit + FastAPI）**，配套软件全部采用国产软件与开源软件。

       🔬
       🔬 第 3 课B — 研究设计进阶·混合
       方法与技术路线

         🔬    课程目标： 掌握混合方法设计与变量操作化，完成技术路线图与策略报告
              框架，熟练运用 AI 工具链加速研究设计全流程



         🤖    本课 AI 技术全景

                 LLM 大模型：DeepSeek / 通义千问 4.5 Sonnet  ⚠️💰
                                            · GPT-5    ⚠️💰 · Gemini 2.5
                 Pro ⚠️💰                 🇨🇳
                       · 智谱 GLM-4.6 · DeepSeek-V3.2   🇨🇳🆓 · Qwen3-Max
                 🇨🇳🆓
                 研究设计智能体：Semantic Scholar / 秘塔 AI 学术搜索 / AMiner（智谱开源学术平台） Notebook ⚠️💰 · Consensus ⚠️💰 · Scite
                 Assistant ⚠️💰 · Research Rabbit ⚠️🆓
                 定性分析 AI：NVivo 15 AI 💰 · MAXQDA AI Assist 💰 · ATLAS.ti AI
                 💰 · Dovetail ⚠️💰 · Delve ⚠️💰
                 定量与问卷 AI：Qualtrics XM ⚠️💰 · SurveyMonkey Genius ⚠️💰 ·
                 SPSS Pro 🇨🇳💰 · JASP 🆓 · jamovi 🆓
                 可视化与绘图：Mermaid Chart AI 💰 · Whimsical AI ⚠️💰 · Napkin
                 AI ⚠️🆓 · Excalidraw 🆓 · tldraw 🆓
                 协作中控台：Hermes Agent（调用 DeepSeek / 通义千问 / 本地 Ollama） ⚠️💰 · n8n 🆓 · Hermes Agent（OpenCode / DeepSeek Harness） 🇨🇳🆓 · Zapier
                 Agents ⚠️💰 · LangGraph 🆓




🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                 1


---

         🇨🇳 ❗    国产化与开源平替原则

                 凡标注 ⚠️ 的工具需科学上网，请优先使用🇨🇳 国产版在内网直达
                 凡标注 💰 的商业软件，推荐使用🆓 开源版降低经费与数据主权风险

                 所有内网方案均支持部署在学校 GPU 集群（参见「高校数据中心部署
                 指南」）




        编号            论文标题            研究视角          核心方法         目标期刊

                      生成式 AI 驱动的
                      北京文化遗产旅                                    《旅游学刊》
                      游目的地形象多                       多模态内容分析      (CSSCI) /
                                      旅游管理 × AI ×
        论文 1          模态构建——基                       + 情感分析 + 深   Tourism
                                      多模态分析
                      于小红书与                         度学习图像识别      Management
                      TripAdvisor 的                              (SSCI)
                      跨平台比较研究

                      基于多语种知识
                                                    知识图谱构建 +     《情报学报》
                      图谱的北京文化         人工智能 × 多语
        论文 2                                        RAG + 系统原型   (CSSCI) /
                      遗产智能问答系         种 × 知识服务
                                                    + 用户实验       JASIST (SSCI)
                      统设计与评估

                      大语言模型赋能                                    《中国翻译》
                      入境游客跨文化                                    (CSSCI) /
                                      跨文化交际 × 入     混合方法（问卷
                      交际障碍消解                                     Annals of
        论文 3                          境旅游 × 语言服     + 深度访谈 + 原
                      ——北京文化遗                                    Tourism
                                      务             型测试）
                      产场景下的多语                                    Research
                      种服务策略研究                                    (SSCI)

       📍 模块一：混合方法研究设计（15 分钟）
       为什么选择混合方法？




🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                      2


---

         💡    我们的模拟国社科课题天然适合混合方法：

                 定量部分：问卷调查入境游客满意度、知识图谱覆盖率评估、系统可用
                 性量化测试

                 定性部分：深度访谈游客体验、案例分析文化遗产场景、原型用户反馈

                 技术部分：系统原型开发、知识图谱构建、多模态数据分析



       三种经典混合设计

        设计类型          特点        适用论文        国际版工具链          ⚠️ 🇨🇳
                                                               源平替
                                                                  国产 + 🆓 开


                                            Qualtrics XM → 问卷星 AI →
                      先定量收集数                SPSS Pro →     SPSSAU /    🆓
        解释性序贯设计
        QUAN → qual
                      据，再用定性解
                                论文 3（问卷→
                                访谈）
                                            NVivo 15 AI →  JASP →     🆓
                      释结果                   DeepSeek / 通义千问 4.5 综合 Taguette →
                                            解释             GLM-4.6
                                            MAXQDA AI
                                            Assist → GPT-5
                                                               🆓 QualCoder
                                论文 1（内容分                       → DeepSeek-
        探索性序贯设计       先定性探索，再               主题抽取 →
                                析→大规模数据                        V3.2 主题抽取
        qual → QUAN   用定量验证
                                挖掘）
                                            Python +
                                                               → 🆓  BERTopic
                                            BERTopic →
                                            JASP
                                                               → 🆓  jamovi

                                            ATLAS.ti AI +      🆓 Taguette +
                                            Dovetail ‖         见解 ‖ 🆓
        并行设计          定量和定性同时   论文 2（系统评
                                            Python +           Python +
        QUAN + QUAL   进行，最终整合   估 + 用户访谈）
                                            LangGraph          LangGraph +
                                            Evals              Qwen3-Max




🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                    3


---

         💡     AI 赋能混合方法的 4 个关键节点
                                    🇨🇳           🇨🇳
               1. 设计阶段：用 ima.copilot / Kimi 知识库 或自建 Dify    /🇨🇳🆓
                  FastGPT 🇨🇳🆓
                            知识库，上传理论框架 PDF，由 GLM-4.6      / 🇨🇳
                  Qwen3-Max 🇨🇳🆓
                              基于 Creswell (2023) 推荐最合适的混合设计

               2. 数据整合阶段：用 n8n      🆓 编排 SPSS 定量结果 → NVivo 定性编码 →
                  Obsidian 文献库（YAML 元数据 + Dataview）合并
               3. Joint Display 生成：Mermaid 🆓 / Napkin AI ⚠️🆓 自动生成定量-定
                 性并列展示图

               4. 结果解释阶段：RAG 检索同领域经典混合方法论文，生成讨论章节草稿



       📍 模块二：变量操作化（10 分钟）
        🧪      AI 辅助变量操作化的三步法
                ⚠️💰
               1. 概念澄清：Semantic Scholar / 秘塔 AI 学术搜索 / AMiner（智谱开源学术平台）     Notebook 聚合 30+ 篇文献的概念定义，
                         ⚠️💰 给出学术共识
                  Consensus
               2. 测量工具挖掘：SciSpace ⚠️💰 + Scite Assistant ⚠️💰 定位已验证
                  量表（如 DMO Image Scale、SUS、UTAUT）

               3. 本土化改编：DeepSeek 学术翻译指令 / 腾讯交互翻译 TranSmart Pro ⚠️💰 + Qwen3-Max 🇨🇳🆓 双向回译，确保
                 跨语言等价性（cross-cultural equivalence）



       三篇论文的变量框架
        论文            自变量（IV）        因变量（DV）           调节/中介变量

                      AI 生成内容类型（文    目的地形象感知维度得        平台类型（小红书 vs
        论文 1
                      本/图像/视频）       分                 TripAdvisor）
                      知识图谱覆盖度、RAG    问答准确率、用户满意        语言类型（中/英/日/
        论文 2
                      策略             度                 法）

                      LLM 辅助交际策略类
        论文 3                         交际障碍消解效果          游客母语、文化距离
                      型

          🔧 变量操作化 AI 工具对照表（点击展开）

🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                             4


---

           任务                 推荐 AI 工具                 国内平替

           概念定义聚合                  ⚠️ · Consensus ⚠️ 🇨🇳
                              Semantic Scholar / 秘塔 AI 学术搜索 / AMiner（智谱开源学术平台）
                                                          知网 AI 学术研究助手 · 智谱清
                                                       言·ima.copilot

           量表检索               SciSpace ⚠️ · Scite ⚠️ 💰
                                                       🇨🇳 知网研学 · 万方智搜 · 🆓
                                                       OpenAlex API + 自建 RAG
                              DeepSeek 学术翻译指令 / 腾讯交互翻译 TranSmart Pro ⚠️ 💰 · Qwen3-  🇨🇳 火山翻译 · 有道翻译 · 🆓
           量表汉化
                              Max                      NLLB-200 本地部署

                              Mermaid · Whimsical AI 💰
                                                       🇨🇳 ProcessOn · 亿图 AI · 🆓
                                                       Excalidraw · 🆓 draw.io
           变量图谱可视化


           信度效度模拟             SPSS Pro 💰 · GPT-5 ⚠️
                                                       🆓 JASP · 🆓 jamovi · 🆓 R
                                                       lavaan + DeepSeek 解读




       📍 模块三：技术路线图绘制（15 分钟）
        🗺️    绘图 AI 工具矩阵（含平替方案）

               🆓 代码式绘图： 🆓              Mermaid（全开源）·      🆓 D2
                                                       PlantUML ·
                 交互式白板：Whimsical AI 💰 · 🆓 Excalidraw + AI · 🆓 tldraw ·
                 Miro AI 💰⚠️
                 结构化生成：Napkin AI ⚠️ / 🇨🇳 讯飞智文 · Gamma ⚠️ / 🇨🇳 WPS AI
                 演示 · 讯飞 AIPPT

                 学术专用：BioRender 💰 / 🆓 Inkscape · 🆓 draw.io · Lucidchart AI
                 💰 / 🆓 diagrams.net
                 自托管开源方案：🆓 Kroki（自建图表渲染服务）· 🆓 Mermaid CLI +
                 GitHub Actions


       AI 辅助绘制技术路线图




🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                       5


---

         💬⚡      升级版提示词模板 — 生成 Mermaid 技术路线图

                你是一位资深科研方法论专家。请根据以下研究设计，生成一个 Merm
                aid flowchart 格式的技术路线图：
                - 研究主题：\[你的论文主题\]
                - 研究方法：\[定量/定性/混合\]
                - 数据来源：\[具体数据\]
                - 分析步骤：\[主要步骤\]
                - 理论框架：\[理论名称\]
                要求：
                1. 节点命名使用"动词+名词"结构（如"抽取主题词"）
                2. 关键环节用 emoji 标注（ 🎯📊🤖📝
                                     ）
                3. 为不同阶段填充不同颜色（理论=蓝色, 方法=紫色, 数据=绿色,
                产出=橙色）
                4. 在关键决策点加入菱形判断节点
                5. 输出完整 Mermaid 代码，含 style 定义




       课题总体技术路线图示例（AI 增强版）

          graph TD
               🎯 课题启动<br>文献综述 + 理论框架"] --> AI1{"🤖 AI 选题
             A["
         三角<br>Gap×Feasibility×Venue"}
            AI1 --> B["📊 论文1<br>目的地形象多模态分析"]
            AI1 --> C["🌐 论文2<br>多语种知识图谱 + RAG"]
            AI1 --> D["🗣️ 论文3<br>跨文化交际策略"]
            B --> B1["🧠 CLIP + BLIP-2<br>图文联合编码"]
            C --> C1["🕸️ Neo4j + LangGraph<br>知识图谱构建"]
            C --> C2["🔍 BGE-M3 + RAG 2.0<br>多语种检索"]
            D --> D1["💬 GPT-5 + Qwen3<br>跨文化对话生成"]
            B1 --> E["💻 程序原型<br>多语种智能问答系统"]
             C1 --> E
             C2 --> E
             D1 --> F["  📋策略报告<br>多语种服务策略与机制"]
             E --> EVAL{" 🧪红队 + 人工评估"}
             EVAL -->|通过| G[" 📕专著撰写<br>Hermes Agent（调用 DeepSeek / 通义千问 / 本地 Ollama） + Overleaf"]
             EVAL -->|迭代| E



🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                     6


---

             F --> G
             G --> H["   📦 结项<br>论文+专著+原型+报告"]
             style A fill:#1565C0,stroke:#0D47A1,color:#fff
             style AI1 fill:#7B1FA2,stroke:#4A148C,color:#fff
             style EVAL fill:#F57C00,stroke:#E65100,color:#fff
             style H fill:#2E7D32,stroke:#1B5E20,color:#fff
             style B1 fill:#E3F2FD,stroke:#1565C0
             style C1 fill:#E3F2FD,stroke:#1565C0
             style C2 fill:#E3F2FD,stroke:#1565C0
             style D1 fill:#E3F2FD,stroke:#1565C0

                                                                                     🎯
                                                                                     课题启动
                                                                                  文献综述 + 理论框架




                                                                                    🤖 AI 选题三角
                                                                                 Gap×Feasibility×Venue




                                                📊
                                               论文1
                                                                           🌐
                                                                           论文2                           🧪 红队 + 人工评估                        🗣️
                                                                                                                                             论文3
                                           目的地形象多模态分析                                                                                     跨文化交际策略
                                                                      多语种知识图谱 + RAG




                              🧠 CLIP + BLIP-2       🕸️ Neo4j + LangGraph             🔍 BGE-M3 + RAG 2.0          迭代       通过
                                                                                                                                        💬 GPT-5 + Qwen3
                               图文联合编码                   知识图谱构建                            多语种检索                                           跨文化对话生成




                                                                                         💻
                                                                                         程序原型                                              📋策略报告
                                                                                      多语种智能问答系统                                         多语种服务策略与机制




                                                                                                                      📕 专著撰写
                                                                                                                 Hermes Agent（调用 DeepSeek / 通义千问 / 本地 Ollama） + Overleaf




                                                                                                                       📦
                                                                                                                      结项
                                                                                                                 论文+专著+原型+报告




       🧬 核心 AI 技术栈分层架构
                                🏗️ 基础设施层                           🧠 模型层                                 ⚙️ 编排层                           🎨 应用层
                                    Neo4j                           多模态                                  RAG 2.0                           多端 Bot
                                   知识图谱                          CLIP / BLIP-2                           混合检索                           Web/WeChat/TG




                                   校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama                            LLM                                 LangGraph                         Obsidian + Hermes（OpenCode / DeepSeek Harness）
                                3090/H20 GPU               GLM-4.6 / DeepSeek-V3.2                        多智能体                             中控台




                                 PostgreSQL                       Embedding                                n8n                            Hermes Agent（OpenCode / DeepSeek Harness）
                                  + pgvector                       BGE-M3                                 工作流                             智能体网关




       📍 模块四：策略报告框架设计（10 分钟）

🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                                                                                               7


---

         📝    策略报告写作 AI 工具链

                 政策文本检索：北大法宝 AI     🇨🇳💰 · 威科先行 🇨🇳💰 · OpenLegalAI 🆓
                 结构化大纲：Hermes Agent（调用 DeepSeek / 通义千问 / 本地 Ollama） ⚠️💰（大纲生成）· Lex ⚠️💰 · Jenni AI ⚠️💰

                 数据可视化：Flourish ⚠️💰 · Datawrapper ⚠️🆓 · ECharts 🇨🇳🆓

                 润色与合规：Grammarly ⚠️💰 · QuillBot ⚠️💰 · DeepSeek 学术翻译指令 / 腾讯交互翻译 TranSmart Write ⚠️💰

                 引用管理：Zotero 7 🆓 + GPT · Paperpile ⚠️💰 · ReadCube ⚠️💰



       《北京文化遗产旅游多语种智能服务策略与运营机制》报告框架
        1. 研究背景与问题界定
              北京入境旅游现状与文化遗产旅游痛点

              多语种服务供给缺口分析

        2. 国内外经验借鉴
              国际文化遗产旅游智能服务案例

              国内智慧旅游建设经验

        3. AI 赋能多语种知识服务的策略框架
              技术策略：GenAI + 知识图谱 + RAG

              内容策略：多语种文化遗产知识体系建设

              运营策略：平台化、可持续、可扩展

        4. 运营机制设计
              政府-学术-企业协同机制

              数据治理与隐私保护机制

              内容质量控制与更新机制

        5. 政策建议


       🤖 本课 AI 工具链总览（四列对比版）

🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                             8


---

         📌    图例：
              署
                    ⚠️ 需科学上网 · 💰 商业收费 · 🇨🇳 国产 · 🆓 开源免费 · 🐳 可本地部

        研究阶段          国际主流            商业软件      💰      🇨🇳 国产内网平替 🆓 开源/自托管
                                                                 平替 🐳

                                                       智谱 GLM-4.6 ·   Qwen3-Max +
                      DeepSeek / 通义千问 4.5 ·
                                                       DeepSeek ·     vLLM + RAG ·
        理论框架梳理        ima.copilot（腾讯智能工作台）/ Kimi 知识库 / 本地 iScholar RAG      Semantic Scholar / 秘塔 AI 学术搜索 / AMiner（智谱开源学术平台） · Scite
                      ⚠️                               Kimi K2 ·
                                                       ima.copilot
                                                                      Ollama +
                                                                      Llama3.3🐳
                                                                🆓 Taguette ·
                      Creswell 教材 · NVivo 15 AI ·      见解 · 帆软
                                                                🆓 QualCoder ·
        混合方法设计
                ⚠️
                      DeepSeek / 通义千问 Projects MAXQDA AI
                                                                🆓 LangGraph
                                                       FineBI · 腾讯乐
                                                                编码智能体 🐳
                                      Assist    视分析

                Scite ⚠️💰 ·                                     🆓 OpenAlex
                Consensus ⚠️ · Semantic                         API · 🆓 Paper-
                                                知网研学 · 万方
        文献与量表检索                                 智搜 · 超星发现 ·
                Research       Scholar API                      QA + BGE-M3
                Rabbit ⚠️                                       🐳
                                                AMiner

                Mermaid AI ·                                    🆓 draw.io · 🆓
                Whimsical 💰 · Miro AI 💰 ·                       Excalidraw · 🆓
                                                ProcessOn · 亿
                Napkin ⚠️ ·    Figma 💰
        技术路线绘图                                  图 AI · 百度 AI
                                                                Mermaid CLI ·
                Lucidchart 💰                                    🆓 Kroki 🐳
                                                图表 · 讯飞智文

                Qualtrics XM                                    🆓 LimeSurvey
                💰  ·
                               Typeform 💰
                                                问卷星 AI · 腾讯
                                                                · 🆓 SurveyJS ·
        问卷设计
                SurveyMonkey
                                                问卷 AI · 金数据
                                                                🆓 Formbricks
                💰                               · 雷锋 AI
                                                                🐳
                                                                🆓 JASP · 🆓
                SPSS 30 AI 💰 · SAS 💰 ·          SPSSAU · SPSS jamovi · 🆓 R +
                Stata 💰        MATLAB 💰                         lavaan · 🆓
        定量分析
                                                Pro · 粤数广联
                                                                PSPP 🐳
                Dovetail 💰 ·                    NVivo 简体版 · 🆓 Taguette ·
                               NVivo 💰 ·
                Delve 💰 ·                       MAXQDA 中文 · 🆓 QualCoder ·
                               MAXQDA 💰
        定性编码
                ATLAS.ti AI 💰                   QDA Miner Lite 🆓 RQDA(R) 🐳

                Grammarly 💰 ·
                                                                🆓
                               Jenni AI 💰 ·
                                                秘塔写作猫 · 火
                QuillBot 💰 ·
                                                                LanguageTool ·
                               Paperpal 💰                       🆓 Qwen3 本地
        写作与润色                                   龙果写作 · 讯飞
                DeepSeek 学术翻译指令 / 腾讯交互翻译 TranSmart Write ⚠️
                                                                部署 🐳
                                                智程 · 火山写作

        报告生成    Hermes Agent（调用 DeepSeek / 通义千问 / 本地 Ollama） ·    Beautiful.ai 💰 · WPS AI ·        🆓 AFFiNE · 🆓
                Gamma ⚠️💰 · Canva 💰             ima.copilot · 讯 AppFlowy · 🆓



🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                          9


---

        研究阶段          国际主流           商业软件    💰       🇨🇳 国产内网平替 🆓 开源/自托管
                                                               平替 🐳
                      Tome    ⚠️                     飞 AIPPT · 百度    Outline + n8n
                                                     文库 AI         🐳
                      Paperpile 💰 ·   EndNote 💰 ·
                                                    NoteExpress ·  🆓 Zotero 7 +
                      ReadCube 💰
        文献管理                                        知网 E-Study ·   Better BibTeX ·
                                      Mendeley
                                                    豆包看文           🆓 JabRef 🐳
                                      Make 💰 ·
                                                                   🆓 n8n · 🆓
                                                                   Hermes Agent（OpenCode / DeepSeek Harness） · 🆓
                      LangGraph ·                   智谱 AgentOS ·

                                                                   Dify · 🆓
        智能体编排         CrewAI · Zapier Microsoft     阑中天 · 会写
                      Agents 💰        Copilot 💰
                                                                   FastGPT 🐳
                                                    Coze

                      Pinecone 💰 ·
                                                                   🆓 pgvector ·
                                                    阿里
                      Weaviate Cloud Zilliz Cloud 💰 DashVector · 腾
                                                                   🆓 Milvus · 🆓
                                                                   Chroma · 🆓
        向量数据库
                      💰                             讯云 VectorDB
                                                                   Qdrant 🐳


         🏆✨      推荐组合：完全国产化 + 开源组合方案

                 LLM：GLM-4.6 （在线）+ Qwen3-Max （本地 vLLM）
                 知识库：Zotero 7 + Milvus + BGE-M3

                 编排：n8n + Dify + Hermes Agent（OpenCode / DeepSeek Harness）

                 中控台：AFFiNE（自托管）+ Obsidian + Hermes（OpenCode / DeepSeek Harness）（个人）双向同步

                 分析：JASP / jamovi + Taguette + Python

                 写作：秘塔写作猫 + DeepSeek 学术翻译指令 / 腾讯交互翻译 TranSmart 国内版 + LanguageTool

                 ✅ 特点：零外网依赖 · 零订阅费 · 数据主权完全自控

       🔬 AI 智能体实验沙箱（拓展）
        🧪     可选：在 Hermes Agent（OpenCode / DeepSeek Harness） 中搭建「研究设计助手」智能体



          🛠️ 智能体配置清单（点击展开）
              角色定位：研究设计教练 + 方法论顾问




🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                          10


---

              核心能力：

                 读取已有文献综述 → 推荐 3 种可行的研究设计

                 根据研究问题 → 生成变量操作化表格

                 接入 Mermaid API → 自动输出技术路线图

                 调用 Semantic Scholar / 秘塔 AI 学术搜索 / AMiner（智谱开源学术平台） API → 验证量表已有文献支撑

                 输出到 Obsidian 文献库（YAML 元数据 + Dataview） → 形成可追溯的设计档案

              技术栈（国际版）：LangGraph       🆓 + DeepSeek / 通义千问 4.5 ⚠️💰 + Semantic Scholar / 秘塔 AI 学术搜索 / AMiner（智谱开源学术平台） MCP ⚠️💰 +
              Obsidian + Hermes（OpenCode / DeepSeek Harness） MCP ⚠️💰 + Mermaid API 🆓
              技术栈（国产化 + 开源版）：🆓 Dify 🇨🇳🆓 + GLM-4.6 🇨🇳 + OpenAlex
              MCP 🆓 + AFFiNE MCP 🆓 + Mermaid CLI 🆓
              交付流程：

                 sequenceDiagram
                    participant U as 用户
                    participant C as Hermes Agent（OpenCode / DeepSeek Harness）
                     participant L as LangGraph
                     participant E as Semantic Scholar / 秘塔 AI 学术搜索 / AMiner（智谱开源学术平台）
                     participant N as Obsidian + Hermes（OpenCode / DeepSeek Harness）
                     U->>C: 提交研究问题
                     C->>L: 路由到设计智能体
                     L->>E: 查询相关文献
                     E-->>L: 返回 30 篇核心文献
                     L->>L: 生成设计方案 + 变量表
                     L->>N: 写入研究设计数据库
                     N-->>U: 返回可编辑的设计文档

                               用户            Hermes Agent（OpenCode / DeepSeek Harness）      LangGraph             Semantic Scholar / 秘塔 AI 学术搜索 / AMiner（智谱开源学术平台）   Obsidian + Hermes（OpenCode / DeepSeek Harness）


                                    提交研究问题

                                                    路由到设计智能体

                                                                       查询相关文献

                                                                   返回 30 篇核心文献

                                                         生成设计方案 + 变量表



                                                                           写入研究设计数据库

                                                         返回可编辑的设计文档



                               用户            Hermes Agent（OpenCode / DeepSeek Harness）      LangGraph             Semantic Scholar / 秘塔 AI 学术搜索 / AMiner（智谱开源学术平台）   Obsidian + Hermes（OpenCode / DeepSeek Harness）




       📝 课后作业
🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                                        11


---

         ✅    完成以下作业，并将产出物同步到个人 Obsidian + Hermes（OpenCode / DeepSeek Harness） 课程库（或
              AppFlowy 自托管课程库）
                                                                     🆓 AFFiNE /

                          🇨🇳            🆓
         A. 使用 DeepSeek / 通义千问 / GLM-4.6 / Qwen3-Max 为你选定的论文完成变量操作
       化表（含 IV/DV/中介/调节 + 量表来源 + 信度系数）

                                🇨🇳 ProcessOn / 🆓 Excalidraw 绘制技术路线图
         B. 使用 Mermaid Chart AI /
       （要求含判断节点 + 分层配色）

         C. 使用 Hermes Agent（调用 DeepSeek / 通义千问 / 本地 Ollama） / 🇨🇳 秘塔写作猫 / 🆓 LanguageTool 撰写策略报告的一个章节
       大纲（500 词，含 3 级标题）

         D. 🌟（进阶）在 🆓 Dify 或 Hermes Agent（OpenCode / DeepSeek Harness） 中搭建一个简易的「研究设计助手」智
       能体，至少完成变量推荐功能

         E. 🌟🌟（挑战）将整套工作流迁移至全国产化或全开源链路，对比记录产出质量
       与时间成本



         📚    延伸阅读

                 Creswell, J. W., & Plano Clark, V. L. (2023). Designing and
                 Conducting Mixed Methods Research (4th ed.)
                 Fetters, M. D. (2020). The Mixed Methods Research Workbook
                 陈向明 (2022). 《质的研究方法与社会科学研究》

                 《AI4Science: 科研范式变革》— 微软研究院 2024 白皮书




       🇨🇳 十一、标注图例系统
         📍 ⚠️       ：需科学上网方可访问，优先使用国产平替

                 💰：商业收费，高校多有文教价但仍需经费
                 🇨🇳：国产方案，无需外网，注册即用
                 🆓：完全开源免费，适合学术共享与长期积累
                 🐳：可使用 Docker 在学校 GPU 集群或个人服务器本地部署

🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                       12


---

       📖 术语与工具全释（Glossary）
        🔤     本节对本课所有研究方法概念与AI 工具进行统一解释，按类别折叠，点击
              展开查看。适合作为课后备查手册。


       🧪 一、研究方法与方法论概念
          混合方法与研究设计（点击展开）

              混合方法研究 (Mixed Methods Research)：同时或序贯使用定量与定性方
              法，相互补充以对研究问题形成更全面的认识。代表学者：Creswell 与
              Plano Clark。
              解释性序贯设计 (Explanatory Sequential Design)：QUAN → qual。先定
              量收集大样本数据，再通过小样本访谈/案例解释定量结果，适用于“为什么会
              这样”问题。

              探索性序贯设计 (Exploratory Sequential Design)：qual → QUAN。先定
              性探索新概念/构造，再用定量验证其普遍性，适用于新领域研究。

              并行汇聚设计 (Convergent Parallel Design)：QUAN + QUAL 同时进行，
              在解释阶段融合，适用于系统评估与交叉验证。

              变量操作化 (Operationalization)：将抽象概念转化为可观察、可测量的指
              标/题项的过程。

              自变量 (IV)：研究者主动操纵的原因变量。

              因变量 (DV)：受 IV 影响的结果变量。

              中介变量 (Mediator)：说明 IV 如何作用于 DV 的“内在机制”。

              调节变量 (Moderator)：改变 IV → DV 关系强度/方向的边界条件。

              信度 (Reliability)：重复测量一致程度。常用 Cronbach α，≥ 0.7 可接受。

              效度 (Validity)：测量的真实度，包括内容效度、构造效度、准则效度。

              Brislin 回译法：EN→ZH→EN 双向翻译对比，验证跨文化量表等价性。
              Joint Display：混合方法中定量-定性结果的并列展示矩阵，用于高效整合双
              边证据。



🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                            13


---

              红队检验 (Red Team)：以对抗性角色主动挑战 AI 系统/研究设计的漏洞，提
              升鲁棒性。

          量表与经典量表（点击展开）

              DMO Image Scale：目的地营销组织形象量表，测量目的地认知、情感与总
              体形象（Baloglu & McCleary, 1999）。

              SUS (System Usability Scale)：系统可用性量表，10 题 5 点量表，得分 ≥
              68 为可接受。
              UTAUT：整合技术接受与使用理论，含绩效期望、努力期望、社会影响、便
              利条件四维。

              Cronbach α：内部一致性信度系数，是简单易算的信度指标。
          IMRaD 与学术写作结构（点击展开）
              IMRaD：Introduction、Methods、Results and Discussion，主流
              SCI/SSCI 论文标准章节结构。
              Rebuttal Letter：回复审稿意见的正式信件，逐条对应审稿人评论并说明修
              改。

              Change Log：版本修改历史的结构化记录，便于审稿人追踪修改点。

       🤖 二、大语言模型（LLM）
          国际主流 LLM（点击展开）

              DeepSeek / 通义千问 4.5 Sonnet   ⚠️💰：Anthropic 推出的长上下文模型，在长文本理
              解、学术写作、代码方面表现突出，支持 Projects 长期记忆。

              GPT-5 ⚠️💰：OpenAI 旗舰模型，处理多模态与推理，准确率与交互体验领
              先。

              Gemini 2.5 Pro ⚠️💰：Google DeepMind 模型，长上下文窗口最大，适合
              大文档问答。

          国产/开源 LLM（点击展开）

              GLM-4.6🇨🇳：智谱 AI 最新旗舰模型，支持中文深度理解与知识推理，国内
              直接可调用。

              DeepSeek-V3.2 🇨🇳🆓：深度求索开源模型，性能对标 GPT-4，API 价格极
              低，适合批量处理。

              Qwen3-Max 🇨🇳🆓：阿里通义千问旗舰模型，开源可本地部署，支持 vLLM
              高吞吐推理。



🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                          14


---

              Kimi K2 🇨🇳：月之暗面长上下文模型，擅长文档与 RAG 场景。
              Llama 3.3 🆓：Meta 开源模型，可用 Ollama 本地一键启动，适合离线学术
              环境。

       📚 三、研究与文献 AI 工具
          学术搜索与文献综述（点击展开）

              Semantic Scholar / 秘塔 AI 学术搜索 / AMiner（智谱开源学术平台）⚠️💰：基于 AI 的论文答疑与证据聚合平台，支持 Notebook 与代理工
              流。

              Consensus ⚠️💰：学术共识量化引擎，对一个问题聚合数十篇论文结论并
              给出倾向。

              Scite Assistant ⚠️💰：基于 Smart Citations 的引文情境分析（支持/反对/
              提及）。

              SciSpace ⚠️💰：AI 阅读助手 + 文献表格化聚合。
              Research Rabbit ⚠️🆓：论文引用网络可视化与推荐，类似"文献版
              Spotify"。
              Connected Papers ⚠️🆓：以种子论文为中心建立相关性图谱，快速理清领
              域脉络。

              ima.copilot（腾讯智能工作台）/ Kimi 知识库 / 本地 iScholar RAG ⚠️🆓：Google 零代码 RAG 工具，上传文档后即可问答 + 生
              成音频总结。

              Zotero 7 🆓：开源文献管理，配合 Better BibTeX、ZotFile 与 GPT 插件可
              构建个人知识库。

              知网研学 🇨🇳💰 / 万方智搜 🇨🇳💰 / 超星发现 🇨🇳💰 / AMiner 🇨🇳🆓：中文文
              献库的 AI 增强检索入口。

              OpenAlex 🆓：完全开放的学术元数据 API，无需登录，适合自建研究检索
              平台。

              Paper-QA 🆓：开源学术 RAG 框架，自动引用文献原文作为证据。
          研究设计与理论介绍（点击展开）

                           ⚠️💰
              DeepSeek / 通义千问 Projects ：DeepSeek / 通义千问 的长期记忆工作区，可上传理论框架/教材
              PDF，持续上下文引用。
              Creswell 教材 💰：Designing and Conducting Mixed Methods
              Research，混合方法领域的经典教材（Creswell & Plano Clark）。



🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                           15


---

       🔍 四、定性分析与编码工具
          商业定性分析工具（点击展开）

              NVivo 15 AI 💰：QSR 旗舰定性分析软件，集成 AI 自动编码、主题抽取，推
              荐用于大规模访谈与文本语料。

              MAXQDA AI Assist 💰：德国质性分析软件，支持混合方法 Joint Display。
              ATLAS.ti AI 💰：德国质性研究软件，擅长网络化关联分析（网络图 + 嵌套
              编码）。

              Dovetail ⚠️💰：产品研究、用户访谈场景常用的定性 SaaS。
              Delve ⚠️💰：轻量级在线定性编码工具，适合学生与小团队。
          开源定性分析工具（点击展开）

              Taguette🆓：完全免费开源的在线定性编码平台，支持多人协作。
              QualCoder 🆓：桌面级开源替代，功能近似 NVivo 但零费用。
              RQDA 🆓：基于 R 语言的定性数据分析包，适合混合研究。
              BERTopic 🆓：基于 BERT 嵌入的主题模型开源包，适用于大规模中文主题
              发现。

       📊 五、定量分析与问卷工具
          统计分析软件（点击展开）

              SPSS Pro  🇨🇳💰 / SPSSAU 🇨🇳💰：国产在线版 SPSS，内建 AI 解读功能，
              适合文科零基础。

              SPSS 30 AI 💰：IBM 商业旗舰版，新增 AI 自动补数与模型建议。
              JASP 🆓：阿姆斯特丹大学开源贝叶斯统计软件，界面类似 SPSS。
              jamovi 🆓：开源统计软件，底层 R，适合教学与论文复现。
              PSPP 🆓：SPSS 的完全开源克隆本，语法兼容。
              R + lavaan 🆓：结构方程模型（SEM）的主流开源包，支持验证性因子分
              析。

              Stata 💰 / SAS 💰 / MATLAB 💰：经典商业统计与建模软件，许可费贵。
          问卷与数据采集（点击展开）

                         ⚠️💰：高端商业问卷平台，支持复杂逻辑与实验设计。
              Qualtrics XM
              SurveyMonkey Genius ⚠️💰：AI 辅助问卷设计与质量检查工具。


🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                       16


---

              问卷星 AI     🇨🇳
                       / 腾讯问卷     🇨🇳 / 金数据 🇨🇳：国内主流问卷平台，支持微信分发
              与 AI 模板。

              LimeSurvey 🆓 / SurveyJS 🆓 / Formbricks 🆓：开源问卷系统，支持自
              托管，适合学术伦理/数据主权严格的场景。

       🎨 六、可视化与绘图工具
          图表与技术路线绘制（点击展开）

              Mermaid  🆓：开源 Markdown 风绘图语言，支持流程图、时序图、类图、
              甘特图等，Obsidian + Hermes（OpenCode / DeepSeek Harness） 原生支持渲染。

              Mermaid Chart 💰：Mermaid 官方商业版，支持自然语言转 Mermaid 代
              码。

              PlantUML 🆓 / D2 🆓：另两种开源代码化绘图语言，适合软件架构与
              UML。
              Whimsical AI ⚠️💰 / Miro AI ⚠️💰 / Figma ⚠️💰：协作式白板与设计工
              具，支持 AI 生成框架图。

              Excalidraw 🆓：开源手绘风白板，内置 AI 文本→图生成。
              tldraw 🆓：开源交互式白板，推出 computer 子项支持 AI 运行流程。
              Napkin AI ⚠️🆓：文本→信息图一键生成。
              Gamma ⚠️💰 / Tome ⚠️💰：AI 演示文稿生成平台。
              BioRender 💰：生命科学专用科研插图，商业订阅。
              Inkscape 🆓：开源矢量图编辑器，可代替 BioRender 手绘角色。
              draw.io 🆓 / diagrams.net 🆓：开源流程图工具，支持本地部署。
              Lucidchart AI 💰：商业图表平台，支持数据绑定。
              ProcessOn 🇨🇳 / 亿图 AI 🇨🇳💰 / 百度 AI 图表 🇨🇳 / 讯飞智文 🇨🇳：国产在线
              图表绘制平台。

              Kroki 🆓：自托管图表渲染服务，支持 Mermaid、PlantUML 等 20+ 种图表
              格式。

          数据可视化（点击展开）

              Flourish⚠️💰 / Datawrapper ⚠️🆓：新闻级交互式图表生成平台。
              ECharts 🇨🇳🆓：百度开源图表库，国内最流行的综合可视化方案。



🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                           17


---

              Apache Superset   🆓：开源 BI 平台，可与 PostgreSQL 直连搭建科研仪表
              板。

       🌐 七、RAG、知识图谱与向量数据库
          RAG 相关概念（点击展开）
              RAG (Retrieval-Augmented Generation)：检索增强生成，先从知识库检
              索相关文档再交由 LLM 生成答案。

              RAG 2.0⚠️：提升版，特征包括混合检索（关键词+向量）、重排序、多步推
              理、自适应分段。

              Embedding ⚠️：将文本转为固定维向量，衡量语义相似性的基础操作。
              BGE-M3 ⚠️🆓：智源多语种多功能开源 embedding 模型，适合中文场景。
              CLIP ⚠️🆓 / BLIP-2 ⚠️🆓：多模态模型，将图像与文本映射到同一向量空
              间。

              Knowledge Graph (知识图谱)：以实体-关系-实体三元组结构化表示知识的
              数据库。

          向量数据库与图数据库（点击展开）

              Neo4j 🆓💰：图数据库老牌产品，单机版开源，适合知识图谱存储。
              pgvector 🆓：PostgreSQL 的向量扩展，一张表既存业务数据又做向量检
              索。

              Milvus 🆓 / Chroma 🆓 / Qdrant 🆓：主流开源向量数据库，支持亿级向量
              检索。

              Pinecone ⚠️💰 / Weaviate Cloud ⚠️💰 / Zilliz Cloud ⚠️💰：管理版向量
              数据库 SaaS，无需运维但需收费。

              阿里 DashVector 🇨🇳💰 / 腾讯云 VectorDB 🇨🇳💰：国产云端向量数据库。

       ⚙️ 八、编排与智能体平台
          工作流编排（点击展开）

              n8n 🆓：开源可视化工作流平台，类似"开源版 Zapier"，支持自托管与 AI
              节点。

              Zapier Agents ⚠️💰 / Make ⚠️💰 / Microsoft Copilot ⚠️💰：商业自动
              化平台，计量计费。




🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                18


---

              LangGraph   🆓：LangChain 旗下多智能体状态机编排库,适合复杂分支逻
              辑。

              CrewAI   🆓：多角色智能体协作框架，强调角色分工。
          智能体平台（点击展开）

              Hermes Agent（OpenCode / DeepSeek Harness）   🇨🇳🆓：开源多模态智能体网关，支持浏览器自动化 + MCP。
              Dify🇨🇳🆓：国产开源 LLM 应用开发平台，内置 RAG、Agent、工作流三大
              轴。

              FastGPT 🇨🇳🆓：国产开源知识库问答平台，问题拆解与工作流编排很成熟。
              Zhipu AgentOS 🇨🇳 / Coze 🇨🇳：国产智能体研发平台。
              MCP (Model Context Protocol) 🆓：Anthropic 主导的模型与工具连接协
              议，类似"智能体的 USB-C"。

       🏫 九、知识库与写作平台
          笔记与知识管理（点击展开）

              Obsidian + Hermes（OpenCode / DeepSeek Harness） / Hermes Agent（调用 DeepSeek / 通义千问 / 本地 Ollama）   ⚠️💰：一体化文档·数据库·协作平台，内置 AI 助手，本
              课的中控台。

              AFFiNE  🆓：开源 Obsidian + Hermes（OpenCode / DeepSeek Harness） 的可自托管替代，支持图谱视图 + 白板。
              AppFlowy 🆓：开源的 Obsidian + Hermes（OpenCode / DeepSeek Harness） 替代，简洁轻量。
              Outline 🆓💰：开源团队知识库，适合 Wiki 组织模式。
              Anytype 🆓：本地优先的开源笔记库。
          写作与润色（点击展开）

              Grammarly  ⚠️💰：英文语法商业检查工具。
              QuillBot ⚠️💰：英文改写降重工具，当前为商业订阅。
              DeepSeek 学术翻译指令 / 腾讯交互翻译 TranSmart Pro / DeepSeek 学术翻译指令 / 腾讯交互翻译 TranSmart Write ⚠️💰：一流机器翻译与润色，头部有 DeepSeek 学术翻译指令 / 腾讯交互翻译 TranSmart 国
              内版。

              LanguageTool 🆓：开源多语种语法检查器，可自托管。
              秘塔写作猫 🇨🇳 / 火龙果写作 🇨🇳 / 讯飞智程 🇨🇳 / 火山写作 🇨🇳：国产中文写作
              辅助。

              Overleaf 🆓💰：在线 LaTeX 协作平台，商业+开源混合模式。
              Jenni AI ⚠️💰 / Paperpal ⚠️💰：商业英文学术写作助手。


🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                          19


---

          演示与报告生成（点击展开）

              Gamma  ⚠️💰：AI 一键生成演示文稿，响应迅速。
              Tome ⚠️💰 / Beautiful.ai ⚠️💰 / Canva ⚠️💰：商业演示工具。
              WPS AI 🇨🇳💰 / ima.copilot 🇨🇳 / 讯飞 AIPPT 🇨🇳 / 百度文库 AI 🇨🇳：国产一
              站式文档助手。

       🏗️ 十、基础设施与部署
          计算与训练平台（点击展开）

              校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama  ⚠️💰（国内平替 AutoDL 🇨🇳💰）：按小时付费的云端 GPU 平台，
              适合科研模型实验。

              Hugging Face ⚠️🆓（国内 魔塔 🇨🇳🆓 平替）：全球最大开源模型与数据集
              社区。

              Weights & Biases ⚠️💰：实验记录与超参搜索商业平台。
              vLLM 🆓：伯克利推出的高吞吐 LLM 推理引擎，国内首选。
              Ollama 🆓：本地一键运行开源 LLM 的开源工具，适合离线实验。
              LoRA 🆓：低秩适配微调技术，让模型微调内存占用降至原来的 1/10。
              Axolotl 🆓：开源 LLM 微调工具链，是本课快速微调首选。

       📘 附录：Creswell & Plano Clark (2023) 混合方法论著
       深度解读

         📖    Creswell, J. W., & Plano Clark, V. L. (2023). Designing and
              Conducting Mixed Methods Research (4th ed.). SAGE Publications.
              本书是混合方法研究（Mixed Methods Research, MMR）领域的经典教
              材，第 4 版新增 核心与复杂设计两层分类、文化与社会正义视角、AI 辅助
              编码伦理 等内容，是国社科、教育部规划基金、SSCI 期刊审稿人最认可的
              方法论权威。


       🏛️ 1. 著作整体架构（Book Architecture）


🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                     20


---

         🧭    全书按 「定义 → 设计 → 实施 → 解释 → 写作 → 评估」 六大板块进行，既
              是教材也是操作手册。




          graph TB
             subgraph P1["    📐
                             第一部分：基础与概念"]
                 C1["     📌
                        Ch.1 MMR 的本质<br>定义·起源·意义"]
                 C2["     🧠
                        Ch.2 哲学与理论<br>实用主义·转换框架"]
             end
             subgraph P2["    🏗️
                             第二部分：设计"]
                 C3["     🎯
                        Ch.3 核心设计选择"]
                 C4["     🔀
                        Ch.4 复杂设计扩展"]
                 C5["     📋
                        Ch.5 研究问题 & 假设"]
             end
             subgraph P3["⚙️第三部分：实施"]
                     📥 Ch.6 数据采集"]
                   C6["
                     🔍 Ch.7 数据分析与整合"]
                   C7["
             end
             subgraph P4["📝 第四部分：解释与写作"]
                 C8["📊 Ch.8 结果解释与 Joint Display"]
                   C9["✍️Ch.9 论文/报告写作"]
             end
             subgraph P5["    🏆
                             第五部分：质量与评估"]
                 C10["    🔎
                         Ch.10 效度与质量标准"]
                 C11["    🌍
                         Ch.11 伦理·文化·AI 新议题"]
             end
             P1 --> P2 --> P3 --> P4 --> P5
             style P1 fill:#E3F2FD,stroke:#1565C0
             style P2 fill:#F3E5F5,stroke:#4A148C
             style P3 fill:#E8F5E9,stroke:#1B5E20
             style P4 fill:#FFF3E0,stroke:#E65100
             style P5 fill:#FCE4EC,stroke:#880E4F




🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                21


---

                                                    📐 第一部分：基础与概念
                                          📌 Ch.1 MMR 的本质     🧠 Ch.2 哲学与理论
                                             定义·起源·意义            实用主义·转换框架




                                                       🏗️ 第二部分：设计
                              📋 Ch.5 研究问题 & 假设         🎯 Ch.3 核心设计选择       🔀 Ch.4 复杂设计扩展

                                                      ⚙️ 第三部分：实施
                                          📥 Ch.6 数据采集        🔍 Ch.7 数据分析与整合

                                                  📝 第四部分：解释与写作
                                       📊 Ch.8 结果解释与 Joint   ✍️ Ch.9 论文/报告写作
                                             Display




                                                  🏆 第五部分：质量与评估
                                     🔎 Ch.10 效度与质量标准       🌍 Ch.11 伦理·文化·AI 新议
                                                                       题




       🔑 2. 核心观点（Key Propositions）
        编号            核心命题                                 内涵与对研究者的启示

                                                           必须在设计阶段明确定性 / 定量的权重、先后顺
        K1            MMR 不是简单拼接
                                                           序、整合点

                                                           所有混合设计都必须回答：为何混合、在哪里混
        K2            整合是灵魂
                                                           合、如何混合

                                                           QUAN + qual / quan + QUAL / QUAN + QUAL
        K3            标记体系
                                                           表示权重，× 表示混合时机

                                                           先改善三个核心设计，再在其上加衍生设计（如
        K4            核心 × 复杂二层分类
                                                           MMAR、MMET、MMCS）
                                                           通过并列表格/图形呈现定量-定性结果的“碰撞与
        K5            Joint Display 必备
                                                           扩展”，避免始终“并行而不交互”

                                                           第 4 版新增 「Integration Quality」
                                                                                       ：设计质量
        K6            整合质量标准
                                                           + 解释严谨 + 元推理 (meta-inference)
                                                           新版强调：使用 LLM 辅助编码/翻译 必须披露、
        K7            AI/文化新议题
                                                           验证、保留人类判断层


       🎨 3. 定义混合设计的 「6 个决策点」
          flowchart LR
             Q1{"   1️⃣ 方法前后顺序？"}
             Q2{"   2️⃣ 定性 vs 定量的权重？"}

🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                                          22


---

               Q3{"3️⃣在哪个阶段混合？"}
               Q4{"4️⃣如何整合数据？"}
               Q5{"5️⃣谁来解释结果？"}
               Q6{"6️⃣如何展示整合？"}
               Q1 --> Q2 --> Q3 --> Q4 --> Q5 --> Q6
               Q1 -.->|并行| QA["QUAN + QUAL同步"]
               Q1 -.->|序贯| QB["QUAN→qual 或 qual→QUAN"]
               Q4 -.-> MG1["合并 Merging"]
               Q4 -.-> MG2["解释 Explaining"]
               Q4 -.-> MG3["构建 Building"]
               Q4 -.-> MG4["嵌套 Embedding"]
               Q6 -.-> JD["       📊
                             Joint Display"]
               style Q1 fill:#1565C0,color:#fff
               style Q6 fill:#2E7D32,color:#fff
               style JD fill:#F57C00,color:#fff

                                                                                             5️⃣ 谁来解释结果？
                                                                                                              6️⃣ 如何展示整合？
                                                                                                                            📊 Joint Display
                                           2️⃣ 定性 vs 定量的权重？     3️⃣ 在哪个阶段混合？
                                                                                             合并 Merging




                                                                               4️⃣ 如何整合数据？   解释 Explaining


                             1️⃣ 方法前后顺序？         并行           QUAN + QUAL同步

                                                                                             构建 Building
                                                 序贯

                                                                 QUAN→qual 或
                                                                  qual→QUAN
                                                                                             嵌套 Embedding




       📦 4. 三大核心设计 + 三大复杂设计（第 4 版体系）
        层级               设计名称                                 符号表示                                           适用场景                             与本课论文对应

                         收敛并行设计                                                                              同时采集，交叉                          论文 2（系统评
        核心 1                                                  QUAN + QUAL
                         Convergent                                                                          验证同一现象                           估 + 用户访谈）

                         解释性序贯设计
                                                                                                             用定性解释定量                          论文 3（问卷 →
        核心 2             Explanatory                          QUAN → qual
                                                                                                             中的意外/差异                          访谈）
                         Sequential
                         探索性序贯设计
                                                                                                             先探索新概念，                          论文 1（内容分
        核心 3             Exploratory                          qual → QUAN
                                                                                                             再大样本验证                           析 → 数据挖掘）
                         Sequential
                         混合方法行动研
                                                              核心 + 参与式行                                      带行动干预的口                          策略报告 + 原型
        复杂 1             究
                                                              动                                              译/旅游项目                           迭代
                         MMAR
                         混合方法评估研
                                                                                                             系统/课程/政策                         智能问答系统评
        复杂 2             究                                    核心 + 评估周期
                                                                                                             评估                               估
                         MMET



🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                                                                                               23


---

        层级               设计名称         符号表示        适用场景       与本课论文对应

                         混合方法案例研
                                      核心 + 多案例边   单个/多个文化遗   小异优先的深度
        复杂 3             究
                                      界           产案例        设计
                         MMCS

       🔄 5. 全流程：从问题到发表的 10 步路径
         graph TD
             S1["  1️⃣
                    界定研究问题<br>是否需要混合？"] --> S2{"混合必要性评
         估"}
             S2 -->|是| S3["     2️⃣
                            选择混合方法理论视角"]
               S2 -->|否| STOP["回到单一方法"]
               S3 --> S4["3️⃣
                            判断设计类型<br>核心 vs 复杂"]
               S4 --> S5["4️⃣
                            确定符号与优先级"]
               S5 --> S6["5️⃣
                            设计样本策略<br>并行/嵌套/分层"]
               S6 --> S7["6️⃣
                            收集定量 & 定性数据"]
               S7 --> S8["7️⃣
                            分别分析两类数据"]
               S8 --> S9["8️⃣ 整合：合并/解释/构建/嵌套"]
               S9 --> S10["9️⃣ Joint Display & 元推理"]
               S10 --> S11["🔟 论文写作 + 质量自检"]
               S11 --> EVAL{"效度 & 整合质量检查"}
               EVAL -->|通过| PUB["📖 投稿 / 结项"]
               EVAL -->|返工| S8
               style S1 fill:#1565C0,color:#fff
               style S9 fill:#7B1FA2,color:#fff
               style EVAL fill:#F57C00,color:#fff
               style PUB fill:#2E7D32,color:#fff
               style STOP fill:#B71C1C,color:#fff




🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                            24


---

🔬 第 3 课B — 研究设计进阶·混合方法与技术路线   25


---

                                           1️⃣ 界定研究问题
                                            是否需要混合？




                                            混合必要性评估




                                              是                否



                              2️⃣ 选择混合方法理论视角                 回到单一方法




                                    3️⃣ 判断设计类型
                                      核心 vs 复杂




                                      4️⃣ 确定符号与优先级

                                              5️⃣ 设计样本策略
                                               并行/嵌套/分层




                                           6️⃣ 收集定量 & 定性数据

                                            7️⃣ 分别分析两类数据

                                   8️⃣ 整合：合并/解释/构建/嵌
                                               套




                                   9️⃣ Joint Display & 元推理     返工




                                    🔟 论文写作 + 质量自检



                                          效度 & 整合质量检查




🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                           26


---

                                           通过



                                        📖 投稿 / 结项


       🧩 6. 四种整合策略深解（Integration Strategies）
          graph LR
               subgraph M["   🔀
                            Merging 合并"]
                   M1["同一问题同时采集"] --> M2["侧边并列比较"] --> M3["Jo
         int Display"]
             end
               subgraph E["   🔍
                            Explaining 解释"]
                   E1["定量结果"] --> E2["定性追踪意外案例"] --> E3["解释论
         述"]
               end
               subgraph B["   🏗️ Building 构建"]
                     B1["定性主题"] --> B2["变量或量表"] --> B3["定量测量"]
               end
               subgraph EM["  🎉
                             Embedding 嵌套"]
                   EM1["主设计"] --> EM2["次设计嵌套其中"] --> EM3["互补信
         息"]
               end
               style M fill:#E3F2FD,stroke:#1565C0
               style E fill:#F3E5F5,stroke:#4A148C
               style B fill:#E8F5E9,stroke:#1B5E20
               style EM fill:#FFF3E0,stroke:#E65100




🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                      27


---

                                         🎉 Embedding 嵌套
                                主设计      次设计嵌套其中           互补信息




                                          🏗️ Building 构建
                                 定性主题       变量或量表          定量测量




                                         🔍 Explaining 解释
                               定量结果      定性追踪意外案例           解释论述




                                          🔀 Merging 合并
                              同一问题同时采集       侧边并列比较         Joint Display




       🏅 7. 质量与效度 (Quality & Validity) 检查清单
         ✅    第 4 版将效度划分为三层，任何 SSCI 论文审稿人都会逐项核查。



          🔎 三层质量检查框架（点击展开）
              L1 设计质量 (Design Quality)
                 研究问题与混合理由匹配

                 设计类型标注明确（符号 + 核心/复杂层级）

                 样本与数据与设计一致

              L2 解释严谨性 (Interpretive Rigor)
                 定量侧：统计假设 + 效应量 + 置信区间

                 定性侧：三角验证 + 成员检验 + 厚描述

                 跨文化 / 跨语言样本的等价性（Brislin 回译）

              L3 整合质量 (Integration Quality)★ 第 4 版新增
                 Joint Display 是否呈现碰撞点
                 Meta-inference 是否超越单一方法
                 AI 辅助编码/分析时是否披露模型、Prompt、人工复核程度

       📑 8. 混合方法论文章节模板（第 4 版推荐）
🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                 28


---

        章节               必备要素                   本课论文对应案例

                         问题陈述 + 混合必要性 +         入境旅游多语种服务缺口 →
        Introduction
                         贡献声明                   QUAN+QUAL 同时必须
                         设计名称 + 符号图 + 样本        依次推出“解释性序贯”符号图与样本流
        Method
                         策略图                    程图

                         分别呈现 QUAN / qual，      插入 2-3 个 Joint Display 呈现交叉发
        Results
                         加 Joint Display        现

                         Meta-inference + 理论贡   跟进 Creswell (2023) 指出 AI 介入后
        Discussion
                         献 + 实践启示               的方法论启示

                         混合特有局限：整合张力·
        Limitations                             披露 LLM Prompt 与人工复核比例
                         资源·AI 偏见


       🤖 9. AI 时代的混合方法新议题（第 4 版亮点）
         ⚡            AI 辅助编码：LLM 生成初编码 → 研究者审核 → 报告一致性。要求泄
                      露模型版本、Prompt、人工复核比例。

                      AI 辅助翻译：全部自动翻译量表需作 Brislin 回译 + 本土专家复核。
                      数据主权：敏感诱导数据不送入境外 API，改用本地部署
                      （Qwen3/GLM）+ RAG 自建知识库。

                      元推理的人机分工：LLM 提出候选假设 → 研究者判定 → Joint
                      Display 展示谁产生、谁验证。


       🔧 10. 本课工具链与 Creswell (2023) 的一一映射
        Creswell 步骤        传统做法                         本课 AI + 国产/开源实现

                                                        ima.copilot / Dify 知识库
        混合必要性评估            手工论证
                                                        + GLM-4.6 诊断
                                                        Mermaid / draw.io / 即梦
        设计符号图绘制            手画 / Visio
                                                        AI
                                                        OpenAlex + Paper-QA 自
        量表发现与汉化            OpenAlex / Semantic Scholar / 知网（CNKI） 手检
                                                        建 RAG + 火山翻译

                                                        JASP / jamovi / 国产
        定量分析               SPSS 手动
                                                        SPSSAU + AI 解读
                                                        Taguette / QualCoder +
        定性编码               NVivo 手动
                                                        LLM 初编码 + 人工复核


🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                      29


---

        Creswell 步骤        传统做法                          本课 AI + 国产/开源实现

                                                         Mermaid / Napkin AI /
        Joint Display 生成   Excel 拼表
                                                         ECharts 一键生成
                                                         Hermes Agent（调用 DeepSeek / 通义千问 / 本地 Ollama） / 秘塔写作猫 起
        元推理与讨论             独自写作
                                                         稿 + 人工精改

                                                         Dify 搭建“混合方法审稿
        质量自检               手动 Checklist
                                                         员”智能体自动打分


       📝 11. 建议精读章节（给时间紧张的学者）
         ⏰    如果只有一周：Ch.3 核心设计 + Ch.7 整合策略 + Ch.8 Joint Display +
              Ch.11 AI/伦理新议题，四章构成最小可用闭环，足以在申报书与方法章节中
              吸收方法论权威。



         📚    延伸阅读

                  Fetters, M. D. (2020). The Mixed Methods Research Workbook —
                  搭配本书的实操水手册

                  Plano Clark, V. L. & Ivankova, N. V. (2016). Mixed Methods
                  Research: A Guide to the Field — 领域体系化地图
                  Tashakkori, A., Johnson, R. B., & Teddlie, C. (2020). Foundations
                  of Mixed Methods Research (2nd ed.)
                  Creswell 个人网站与录像课：https://johnwcreswell.com




🔬 第 3 课B — 研究设计进阶·混合方法与技术路线                                                           30


---

