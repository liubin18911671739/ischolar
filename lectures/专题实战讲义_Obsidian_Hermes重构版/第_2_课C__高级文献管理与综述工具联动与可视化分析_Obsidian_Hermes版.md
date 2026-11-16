---
title: "第_2_课C__高级文献管理与综述工具联动与可视化分析_Obsidian_Hermes版"
workflow: "Obsidian + Hermes (OpenCode / DeepSeek Harness) + iScholar"
software_policy: "国产软件 + 开源软件（零翻墙）"
---

# 第_2_课C__高级文献管理与综述工具联动与可视化分析_Obsidian_Hermes版

> **工具栈说明**：本讲义将传统云端知识库工作流全面重构为 **Obsidian Vault + Hermes（OpenCode 或 DeepSeek Harness）+ 本地 iScholar 应用（Streamlit + FastAPI）**，配套软件全部采用国产软件与开源软件。

      📊
       第 2 课C — 高级文献管理与综述·工具
       联动与可视化分析
        🎯    课程目标： 掌握 Zotero × Obsidian + Hermes（OpenCode / DeepSeek Harness） 双向联动、Hermes 智能体（OpenCode / DeepSeek Harness）在文献管理中的应
             用，以及使用专业工具进行文献计量可视化分析，构建完整的高级文献管理与综述
             能力。




       📋 课程大纲
       模块           主题                   内容详情

                                         1. Zotero Integration 插件安装与配置
                    Zotero Integration：Zotero ×      2. Zotero 文献自动同步到 Obsidian 文献库（YAML 元数据 + Dataview）
       A
                    Obsidian + Hermes（OpenCode / DeepSeek Harness） 联动            3. 在 Obsidian + Hermes（OpenCode / DeepSeek Harness） 中为文献添加笔记、标签、阅读状态
                                         4. 构建个人文献知识管理闭环
                                         1. Hermes Agent（OpenCode / DeepSeek Harness） 架构简介与插件生态
                                         2. 安装 Hermes Agent（OpenCode / DeepSeek Harness） 的 Zotero 插件——在对话中检索文献
                                         库
                    Hermes 智能体（OpenCode / DeepSeek Harness）：
       B                                 3. 安装 Hermes Agent（OpenCode / DeepSeek Harness） 的 Obsidian Skills（obsidian-search / Hermes Console）——在对话中读写
                    Zotero + Obsidian Skills（obsidian-search / Hermes Console）
                                         Obsidian Markdown 笔记
                                         4. 实战：让 Hermes Agent（OpenCode / DeepSeek Harness） 同时访问 Zotero 文献和 Obsidian + Hermes（OpenCode / DeepSeek Harness）
                                         笔记，完成跨工具文献分析

                                         1. CiteSpace——关键词共现、突发性检测、时间线图谱
                                         2. VOSviewer——作者合作网络、期刊共引、关键词聚类
                    文献计量可视化分析工
       C                                 3. Gephi——大规模引用网络的社区发现与力导向布局
                    具
                                         4. Pajek——大型学术网络的精确分区与层次分析
                                         5. 工具选型指南：四大工具适用场景对比
                                         1. OpenAlex——免费开放的全球学术元数据（替代
                                         MAG）
                                         2. Lens.org——专利 + 学术论文一站式检索
                                         3. 免费替代 Web of Science 的学术工具全景指南
                    免费学术数据源与全文
       D                                 （2026）
                    获取
                                         4. 免费全文获取推荐组合：
                                            · Unpaywall——浏览器插件一键查找 OA 版本
                                            · CORE——全球最大开放获取聚合平台
                                            · PubMed Central（PMC）——生物医学全文免费库




第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                      1


---

       🔗 模块 A：Zotero Integration — Zotero × Obsidian 本地知识库联动
        💡    Zotero Integration 是一个 Zotero 插件，能将 Zotero 中的文献条目自动同步到 Obsidian + Hermes（OpenCode / DeepSeek Harness） 数据
             库，实现文献管理与知识管理的无缝衔接。


       安装与配置步骤
       1. 创建 Obsidian 文献库（Dataview 数据库视图）
             在 Obsidian + Hermes（OpenCode / DeepSeek Harness） 中新建一个数据库，包含以下属性：Title（标题）、Authors（作者）、
             Year（年份）、DOI、Tags（标签）、Status（阅读状态）、Notes（笔记）
       2. 创建 Obsidian Local REST / Hermes Console 桥接
             访问 Obsidian 社区插件市场 / Hermes Skills → 新建 Integration → 获取 API Token

             在文献数据库页面右上角 ··· → Connections → 添加刚创建的 Integration

       3. 安装 Zotero Integration 插件
             下载 Zotero Integration：https://github.com/dvanoni/notero

             Zotero → 工具 → 插件 → 从文件安装 → 选择 .xpi 文件
       4. 配置 Zotero Integration
             Zotero → 编辑 → 首选项 → Zotero Integration
             填入 Obsidian Vault 本地路径与 Hermes Profile 配置 和数据库 ID

             设置同步规则（自动/手动、同步哪些集合）

       5. 验证同步
             在 Zotero 中添加一篇文献 → 查看 Obsidian 文献库（YAML 元数据 + Dataview）是否自动出现对应条目

       工作流示意

        graph LR
           A["  📚Zotero<br>文献管理"] -->|"Better BibTeX + Zotero Integration 自动同步"| B["                                                    📋 Obsidian + Hermes（OpenCode / DeepSeek Harness）
        数据库<br>文献条目"]
           B -->|"添加笔记/标签"| C["       Obsidian Markdown 笔记<br>阅读笔记"]📝
           C -->|"汇总综述"| D["                 📄
                                  文献综述<br>初稿"]
           style A fill:#F3E5F5,stroke:#6A1B9A
           style B fill:#E3F2FD,stroke:#1565C0
           style D fill:#E8F5E9,stroke:#2E7D32

                            📚 Zotero   Better BibTeX + Zotero Integration 自动同步
                                                     📋 Obsidian 文献库（YAML 元数据 + Dataview）   添加笔记/标签
                                                                              📝 Obsidian Markdown 笔记   汇总综述
                                                                                                   📄 文献综述
                             文献管理                      文献条目                     阅读笔记                初稿




第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                                                          2


---

       🤖 模块 B：Hermes 智能体（OpenCode / DeepSeek Harness） — Zotero + Obsidian Skills（obsidian-search / Hermes Console）
        🧠    Hermes Agent（支持 OpenCode 或 DeepSeek Harness）支持浏览器插件生态，可在对话中直接访问 Zotero 文
             献库和 Obsidian Vault 本地工作区，实现 AI 驱动的跨工具文献分析。


       Zotero 插件
          功能： 让 Hermes Agent（OpenCode / DeepSeek Harness） 在对话中检索你的 Zotero 文献库

          典型用法：

             「帮我找出文献库中关于 knowledge graph + tourism 的论文」

             「总结我收藏的 2023-2025 年文献的研究趋势」

             「对比文献库中 A 和 B 两篇论文的研究方法」

       Obsidian Skills（obsidian-search / Hermes Console）
          功能： 让 Hermes Agent（OpenCode / DeepSeek Harness） 在对话中读取和写入 Obsidian Markdown 笔记

          典型用法：

             「把这篇论文的阅读笔记写入 Obsidian + Hermes（OpenCode / DeepSeek Harness） 的文献数据库」

             「根据 Obsidian + Hermes（OpenCode / DeepSeek Harness） 中的研究大纲，帮我从 Zotero 中筛选相关文献」

             「将分析结果整理成 Obsidian Markdown 笔记」

       实战场景

        graph TB
            USER[" 👩‍🏫
                     用户提问"] --> OC["🤖     Hermes 智能体（OpenCode / DeepSeek Harness）"]
                                    📚
            OC -->|"Zotero 插件"| ZOT["    Zotero 文献库<br>检索 / 筛选 / 摘
        要"]
                                    📋
            OC -->|"Obsidian Skills（obsidian-search / Hermes Console）"| NOT["    Obsidian Vault 本地工作区<br>读取 / 写入 / 整
        理"]
            ZOT --> OC
            NOT --> OC
            OC -->|"综合分析结果"| OUT[" 📄     输出<br>文献综述 / 对比表 / 笔记"]
            style OC fill:#F3E5F5,stroke:#6A1B9A,stroke-width:2px
            style ZOT fill:#FFF3E0,stroke:#E65100
            style NOT fill:#E3F2FD,stroke:#1565C0




第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                        3


---

                                                👩‍🏫 用户提问

                                              🤖 Hermes 智能体（OpenCode / DeepSeek Harness）

                                  Zotero 插件     Obsidian Skills（obsidian-search / Hermes Console）          综合分析结果




                            📚 Zotero 文献库         📋 Obsidian Vault 本地工作区        📄 输出
                            检索 / 筛选 / 摘要         读取 / 写入 / 整理   文献综述 / 对比表 / 笔记




       📊 模块 C：文献计量可视化分析
       四大工具对比
       工具           核心功能                       适用场景                      数据格式

       CiteSpace    关键词共现、突发性                  中文核心期刊分析
       （windows 调   检测、时间线视图、                  （知网导出）
                                                    、研究前                 知网/WoS/Scopus
       整时间）         聚类分析                       沿识别

       VOSviewer    作者合作网络、期刊
                                               国际文献的宏观图
       （mac 需要      共引、术语共现、密                                            WoS/Scopus/PubMed/OpenAlex
                                               谱、合作关系分析
       hack 方法）     度可视化

                    大规模网络可视化、
       Gephi（设置展    社区发现、                      超大引用网络分析、
                                                                         CSV/GEXF/GraphML
       示方法）         PageRank、力导向布              复杂关系挖掘
                    局

       Pajek
       （windows，数   大型网络精确分区、
                                               网络结构的精细数学
       据从           层次分解、k-core 分                                        .net/.pajek 专用格式
                                               分析
       VOSViewer中   析
       得多）


       推荐工作流

         flowchart LR
            DATA["  📥 数据源<br>OpenAlex / Lens.org<br>知网 / WoS"] --> CS
        ["CiteSpace<br>研究前沿<br>时间演化"]
            DATA --> VOS["VOSviewer<br>合作网络<br>关键词聚类"]
            DATA --> GEPHI["Gephi<br>引用网络<br>社区发现"]
            DATA --> PAJEK["Pajek<br>网络分区<br>层次分析"]
            CS --> REPORT[" 📄 综述论文<br>图谱 + 分析"]
            VOS --> REPORT
            GEPHI --> REPORT
            PAJEK --> REPORT



第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                                         4


---

              style DATA fill:#E3F2FD,stroke:#1565C0
              style REPORT fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px

                                                     CiteSpace
                                                     研究前沿
                                                     时间演化




                                   📥  数据源
                                                     VOSviewer
                                                      合作网络
                               OpenAlex / Lens.org
                                                     关键词聚类
                                   知网 / WoS



                                                      Gephi
                                                     引用网络
                                                                   📄 综述论文
                                                                    图谱 + 分析
                                                     社区发现




                                                      Pajek
                                                     网络分区
                                                     层次分析




       🌐 模块 D：免费学术数据源与全文获取
       免费替代 Web of Science 的学术工具（2026）
       工具 / 平台          核心特色                            网址

                        免费开放学术元数据，覆盖
                        2.5 亿+ 论文，API 友好，替
       OpenAlex                                         https://openalex.org
                        代已停服的 Microsoft
                        Academic Graph
                        专利 + 学术论文一站式检
       Lens.org                                         https://www.lens.org
                        索，支持引用分析和分面筛选

       Semantic         AI 驱动的引用图谱，TLDR 摘
                                                        https://www.semanticscholar.org
       Scholar          要，影响力评分

       OpenAlex / Semantic Scholar / 知网（CNKI）   最大的免费学术搜索引擎，覆
       ⚠️               盖面广（   ⚠️ 需科学上网）                https://scholar.google.com

                        免费版提供基础检索与引用分
       Dimensions                                       https://www.dimensions.ai
                        析，付费版功能接近 WoS

                        Bielefeld 大学运营的开放获
       BASE                                https://www.base-search.net
                        取搜索引擎，索引 3 亿+ 文档


       免费获取全文推荐组合


        📖     三件套组合使用，覆盖绝大多数可合法免费获取的学术全文。




第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                             5


---

       工具                   功能                 使用方式

                            浏览器插件，自动检测当前论文
                                               安装 Chrome/Firefox 插件 → 访问
       Unpaywall            页面是否有合法 OA 版本，一键
                                               论文页面 → 绿色锁图标 = 有免费版
                            跳转下载

                            全球最大开放获取聚合平台，索     https://core.ac.uk → 搜索标题/DOI
       CORE
                            引 2.7 亿+ 篇 OA 论文   → 直接下载 PDF

                            美国国立卫生研究院（NIH）运    https://www.ncbi.nlm.nih.gov/pmc
       PubMed Central
                            营的生物医学全文免费库        → 搜索 → 免费全文


       全文获取决策树

         flowchart TD
            START["     🔍
                      找到目标论文"] --> DOI{"有 DOI？"}
              DOI -->|"是"| UP["   1️⃣
                                  Unpaywall<br>检查 OA 版本"]
              DOI -->|"否"| TITLE["用标题搜索<br>OpenAlex / Semantic Scholar / 知网（CNKI）"]
              UP --> OA{"找到 OA？"}
              OA -->|"✅  找到"| DONE[" 📄 下载 PDF"]
              OA -->|"❌ 未找到"| CORE["2️⃣ CORE<br>搜索 DOI/标题"]
              CORE --> FOUND{"找到？"}
              FOUND -->|"✅"| DONE
              FOUND -->|"❌"| PMC["3️⃣ PubMed Central<br>（生物医学领域）"]
              PMC --> FOUND2{"找到？"}
              FOUND2 -->|"✅"| DONE
              FOUND2 -->|"❌"| LIB["4️⃣ 学校图书馆<br>数据库 / 馆际互借"]
              TITLE --> UP
              style DONE fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px
              style START fill:#E3F2FD,stroke:#1565C0




第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                     6


---

第 2 课C — 高级文献管理与综述·工具联动与可视化分析   7


---

                                  🔍 找到目标论文


                                       有 DOI？




                                  是        否



                                          用标题搜索
                                         OpenAlex / Semantic Scholar / 知网（CNKI）




                                  1️⃣ Unpaywall
                                  检查 OA 版本




                                      找到 OA？




                                           ❌ 未找到
                                           2️⃣ CORE
                                         搜索 DOI/标题




                                            找到？




                                ✅ 找到              ❌

                                  ✅         3️⃣ PubMed Central
                                               （生物医学领域）




                                                  找到？




第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                    8


---

                                           ✅      ❌
                                📄 下载 PDF       4️⃣ 学校图书馆
                                            数据库 / 馆际互借




       ✅ 课后产出
          Zotero Integration 配置完成，Zotero 文献自动同步到 Obsidian 文献库
          Hermes Agent（OpenCode / DeepSeek Harness） 安装 Zotero + Obsidian Skills（obsidian-search / Hermes Console），完成一次跨工具文献分析
          使用 VOSviewer 或 CiteSpace 生成至少 1 张文献计量图谱

          注册 OpenAlex + Lens.org，完成一次免费数据源检索

          安装 Unpaywall 浏览器插件，体验 OA 全文获取流程


       🚀 模块 E：Unpaywall + CORE + PMC 批量论文获取实战
        ⚡    目标： 给定一批 DOI 列表，自动依次查询 Unpaywall → CORE → PubMed
             Central，尽可能获取每篇论文的 OA 全文 PDF，生成下载报告。

       系统架构总览

         flowchart TB
            subgraph INPUT["    📥 输入"]
                 CSV["DOI 列表<br>CSV / BibTeX / RIS"]
                 ZOT["Zotero 导出"]
            end
                          🔧 DOI 解析器<br>去重 + 标准化"]
            CSV --> PARSE["
          ZOT --> PARSE
          PARSE --> PIPELINE["🔄 三级瀑布查询引擎"]
          subgraph PIPELINE["🔄 三级瀑布查询引擎"]
              direction TB
              UP["1️⃣ Unpaywall API<br>api.unpaywall.org/v2/{doi}<br>免
        费，需邮箱，无 Key"] --> UP_OK{"找到 OA？"}
              UP_OK -->|"✅ 有 PDF URL"| SAVE["💾 下载 PDF"]
              UP_OK -->|"❌"| CORE_Q["2️⃣ CORE API<br>api.core.ac.uk/v
        3/search<br>免费 API Key"]
                CORE_Q --> CORE_OK{"找到？"}
                                 ✅
                CORE_OK -->|" "| SAVE



第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                            9


---

                                ❌
                CORE_OK -->|" "| PMC_Q["   3️⃣ PubMed Central<br>E-utilitie
        s API<br>PMC ID → OA PDF"]
                PMC_Q --> PMC_OK{"找到？"}
                            ✅"| SAVE
                 PMC_OK -->|"
                            ❌"| FAIL["⚠️标记未获取"]
                 PMC_OK -->|"
            end
            SAVE --> OUT["📂 输出目录<br>papers/{doi}.pdf"]
            FAIL --> REPORT["📊 下载报告<br>CSV 统计"]
            OUT --> REPORT
            style INPUT fill:#E3F2FD,stroke:#1565C0
            style SAVE fill:#E8F5E9,stroke:#2E7D32
            style FAIL fill:#FFEBEE,stroke:#C62828
            style REPORT fill:#FFF3E0,stroke:#E65100,stroke-width:2px




第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                 10


---

第 2 课C — 高级文献管理与综述·工具联动与可视化分析   11


---

                                                 📥 输入
                                    DOI 列表
                                CSV / BibTeX / RIS                  Zotero 导出




                                        🔧 DOI 解析器
                                        去重 + 标准化



                                                    🔄 三级瀑布查询引擎
                                              1️⃣Unpaywall API
                                          api.unpaywall.org/v2/{doi}
                                           免费，需邮箱，无 Key




                                                    找到 OA？




                                                          ❌
                                                              2️⃣
                                                               CORE API
                                                      api.core.ac.uk/v3/search
                                                            免费 API Key




                                                                找到？




                                     ✅ 有 PDF URL                      ❌
                                                              3️⃣ PubMed Central
                                                ✅               E-utilities API
                                                              PMC ID → OA PDF




                                                                     找到？




                                                          ✅             ❌
                                        💾 下载 PDF                      ⚠️ 标记未获取

                                        📂 输出目录
                                       papers/{doi}.pdf




第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                      12


---

                                             📊 下载报告
                                                 CSV 统计




       API 对比
       数据源               API 端点                                   认证方式         限流

                         api.unpaywall.org/v2/{doi}?              邮箱（无需
       Unpaywall                                                               100,000 次/天
                         email=you@example.com                    Key）
                                                                               10 次/秒（免费
       CORE              api.core.ac.uk/v3/search/works           免费 API Key
                                                                               层）

                                                                               3 次/秒（无
                                                                               Key）
       PMC E-utilities   eutils.ncbi.nlm.nih.gov/entrez/eutils/   可选 API Key
                                                                               10 次/秒（有
                                                                               Key）

       详细流程图：单篇论文获取

         sequenceDiagram
            participant S as         🐍 Python 脚本
              participant U as Unpaywall API
              participant C as CORE API
              participant P as PMC E-utilities
              participant D as 磁盘
              S->>U: GET /v2/{doi}?email=...
              U-->>S: {best_oa_location: {url_for_pdf: ...}}
              alt PDF URL 存在
                  S->>D: 下载并保存 PDF                ✅
              else 无 OA
                   S->>C: GET /v3/search/works?q=doi:{doi}
                   C-->>S: {results: [{downloadUrl: ...}]}
                   alt downloadUrl 存在
                       S->>D: 下载并保存 PDF                   ✅
                   else 无结果
                         S->>P: esearch.fcgi?db=pmc&term={doi}
                         P-->>S: {IdList: [PMC_ID]}
                         alt PMC ID 存在
                              S->>P: efetch.fcgi?db=pmc&id={PMC_ID}
                              P-->>S: Full text XML / PDF link
                              S->>D: 下载并保存 PDF                ✅
                         else 无 PMC 记录
                             S->>D: 记录失败              ❌
第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                                13


---

                          end
                    end
              end

                                🐍 Python 脚本                                       Unpaywall API                    CORE API   PMC E-utilities   磁盘


                                                      GET /v2/{doi}?email=...

                                                {best_oa_location: {url_for_pdf: ...}}

                                    alt                                                                       [PDF URL 存在]


                                                                                                     下载并保存 PDF         ✅
                                                                                                              [无 OA]

                                                               GET /v3/search/works?q=doi:{doi}

                                                                   {results: [{downloadUrl: ...}]}

                                     alt                                                                 [downloadUrl 存在]


                                                                                                     下载并保存 PDF         ✅
                                                                                                              [无结果]

                                                                               esearch.fcgi?db=pmc&term={doi}

                                                                                         {IdList: [PMC_ID]}

                                          alt                                                                 [PMC ID 存在]


                                                                              efetch.fcgi?db=pmc&id={PMC_ID}

                                                                                     Full text XML / PDF link

                                                                                                     下载并保存 PDF         ✅
                                                                                                        [无 PMC 记录]

                                                                                                         记录失败      ❌

                                🐍 Python 脚本                                       Unpaywall API                    CORE API   PMC E-utilities   磁盘




       Python 完整代码示例

        📋     依赖安装： pip install requests tqdm
              使用前： 将 YOUR_EMAIL 替换为你的邮箱，将 YOUR_CORE_API_KEY 替换为 CORE 免费
              API Key。


        """
        batch_paper_fetcher.py
        批量论文全文获取工具 — Unpaywall + CORE + PubMed Central 三级瀑布策略

        用法:
            python batch_paper_fetcher.py dois.txt -o papers/ -e your@em
        ail.com -k YOUR_CORE_KEY
        """

        import os
        import csv
        import time
        import argparse
        import requests
        from pathlib import Path
        from tqdm import tqdm
        from typing import Optional
        from dataclasses import dataclass, field



第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                                                                                        14


---

        from datetime import datetime



        # ──────────────────────────────────────────────
        # 配置
        # ──────────────────────────────────────────────
        @dataclass
        class Config:
            email: str = "YOUR_EMAIL@example.com"
              core_api_key: str = "YOUR_CORE_API_KEY"
              ncbi_api_key: str = "" # 可选，有则 10 req/s，无则 3 req/s
              output_dir: str = "papers"
              report_file: str = "download_report.csv"
              timeout: int = 30
              retry: int = 2
              delay: float = 0.35   # 请求间隔（秒），避免限流



        @dataclass
        class FetchResult:
              doi: str
              source: str = ""       # unpaywall / core / pmc / failed
              pdf_path: str = ""
              pdf_url: str = ""
              error: str = ""



        # ──────────────────────────────────────────────
        # 1️⃣Unpaywall 查询
        # ──────────────────────────────────────────────
        def query_unpaywall(doi: str, cfg: Config) -> Optional[str]:
              """返回 OA PDF 的 URL，未找到返回 None"""
              url = f"https://api.unpaywall.org/v2/{doi}?email={cfg.emai
        l}"
              try:
                 resp = requests.get(url, timeout=cfg.timeout)
                 if resp.status_code == 200:
                     data = resp.json()
                     best = data.get("best_oa_location") or {}
                     pdf_url = best.get("url_for_pdf") or best.get("url")
                     if pdf_url:
                         return pdf_url



第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                               15


---

              except Exception:
                  pass
              return None



        # ──────────────────────────────────────────────
        #   2️⃣ CORE 查询
        # ──────────────────────────────────────────────
        def query_core(doi: str, cfg: Config) -> Optional[str]:
              """返回 CORE 的 PDF 下载 URL"""
              url = "https://api.core.ac.uk/v3/search/works"
              headers = {"Authorization": f"Bearer {cfg.core_api_key}"}
              params = {"q": f'doi:"{doi}"', "limit": 1}
              try:
                resp = requests.get(url, headers=headers, params=params,
        timeout=cfg.timeout)
                  if resp.status_code == 200:
                         results = resp.json().get("results", [])
                         if results:
                            dl = results[0].get("downloadUrl") or results
        [0].get("sourceFulltextUrls", [""])[0]
                        if dl:
                              return dl
              except Exception:
                  pass
              return None



        # ──────────────────────────────────────────────
        #   3️⃣
             PubMed Central 查询
        # ──────────────────────────────────────────────
        def query_pmc(doi: str, cfg: Config) -> Optional[str]:
              """通过 NCBI E-utilities 查找 PMC 全文 PDF"""
              base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
              params_search = {
                  "db": "pmc",
                  "term": f"{doi}[doi]",
                  "retmode": "json",
              }
              if cfg.ncbi_api_key:
                  params_search["api_key"] = cfg.ncbi_api_key
              try:



第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                               16


---

                  # Step 1: esearch 查找 PMC ID
                resp = requests.get(f"{base}/esearch.fcgi", params=param
        s_search, timeout=cfg.timeout)
                  if resp.status_code == 200:
                         ids = resp.json().get("esearchresult", {}).get("idli
        st", [])
                         if ids:
                             pmc_id = ids[0]
                            # PMC 全文 PDF 的固定 URL 模式
                        pdf_url = f"https://www.ncbi.nlm.nih.gov/pmc/art
        icles/PMC{pmc_id}/pdf/"
                            # 验证 PDF 是否可访问
                        head = requests.head(pdf_url, timeout=cfg.timeou
        t, allow_redirects=True)
                            if head.status_code == 200:
                                return pdf_url
                            # 备选：OA 服务 JSON
                        oa_url = f"https://www.ncbi.nlm.nih.gov/pmc/util
        s/oa/oa.fcgi?id=PMC{pmc_id}&format=pdf"
                            resp_oa = requests.get(oa_url, timeout=cfg.timeo
        ut)
                            if resp_oa.status_code == 200 and "<link" in res
        p_oa.text:
                                import re
                                match = re.search(r'href="(https?://[^"]+\.p
        df)"', resp_oa.text)
                            if match:
                                    return match.group(1)
              except Exception:
                  pass
              return None



        # ──────────────────────────────────────────────
        # 下载 PDF
        # ──────────────────────────────────────────────
        def download_pdf(url: str, save_path: Path, cfg: Config) -> boo
        l:
              """下载 PDF 到本地"""
              for attempt in range(cfg.retry):
                  try:
                         resp = requests.get(url, timeout=cfg.timeout, stream



第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                   17


---

        =True,
                                           headers={"User-Agent": "BatchPap
        erFetcher/1.0"})
                        if resp.status_code == 200:
                            content_type = resp.headers.get("Content-Type",
        "")
                            # 基本检查是否为 PDF
                            save_path.parent.mkdir(parents=True, exist_ok=Tr
        ue)
                            with open(save_path, "wb") as f:
                                for chunk in resp.iter_content(chunk_size=81
        92):
                                    f.write(chunk)
                            # 验证文件大小
                            if save_path.stat().st_size > 1024:   # > 1KB
                                return True
                            else:
                              save_path.unlink(missing_ok=True)
                  except Exception:
                      time.sleep(1)
              return False



        # ──────────────────────────────────────────────
        # 三级瀑布主逻辑
        # ──────────────────────────────────────────────
        def fetch_paper(doi: str, cfg: Config) -> FetchResult:
              """对单个 DOI 执行三级瀑布查询"""
              doi = doi.strip()
              safe_name = doi.replace("/", "_").replace(":", "_")
              save_path = Path(cfg.output_dir) / f"{safe_name}.pdf"

              # 如果已下载，跳过
              if save_path.exists() and save_path.stat().st_size > 1024:
                  return FetchResult(doi=doi, source="cached", pdf_path=st
        r(save_path))

              # ---   1️⃣ Unpaywall ---
              pdf_url = query_unpaywall(doi, cfg)
              if pdf_url:
                  if download_pdf(pdf_url, save_path, cfg):
                      return FetchResult(doi=doi, source="unpaywall", pdf_



第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                  18


---

        path=str(save_path), pdf_url=pdf_url)
            time.sleep(cfg.delay)


             # --- 2️⃣CORE ---
             pdf_url = query_core(doi, cfg)
             if pdf_url:
                  if download_pdf(pdf_url, save_path, cfg):
                      return FetchResult(doi=doi, source="core", pdf_path=
        str(save_path), pdf_url=pdf_url)
            time.sleep(cfg.delay)


             # --- 3️⃣PMC ---
             pdf_url = query_pmc(doi, cfg)
             if pdf_url:
                  if download_pdf(pdf_url, save_path, cfg):
                      return FetchResult(doi=doi, source="pmc", pdf_path=s
        tr(save_path), pdf_url=pdf_url)

             return FetchResult(doi=doi, source="failed", error="所有数据源
        均未找到 OA 全文")



        # ──────────────────────────────────────────────
        # 批量执行 + 报告生成
        # ──────────────────────────────────────────────
        def batch_fetch(doi_list: list[str], cfg: Config) -> list[FetchR
        esult]:
             """批量获取论文并生成报告"""
             results = []
             print(f"\n   📚 开始批量获取 {len(doi_list)} 篇论文...\n")
             for doi in tqdm(doi_list, desc="获取进度"):
                  result = fetch_paper(doi, cfg)
                  results.append(result)
                  status = "   ✅" if result.source != "failed" else "❌"
                  tqdm.write(f"    {status} {doi} → {result.source}")

             # 生成 CSV 报告
             report_path = Path(cfg.output_dir) / cfg.report_file
             report_path.parent.mkdir(parents=True, exist_ok=True)
             with open(report_path, "w", newline="", encoding="utf-8") as
        f:



第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                19


---

                writer = csv.DictWriter(f, fieldnames=["doi", "source",
        "pdf_path", "pdf_url", "error"])
                 writer.writeheader()
                 for r in results:
                     writer.writerow(r.__dict__)

            # 统计
            success = sum(1 for r in results if r.source != "failed")
            by_source = {}
            for r in results:
                 by_source[r.source] = by_source.get(r.source, 0) + 1

            print(f"\n{'='*50}")
            print(f"   📊 下载报告 — {datetime.now().strftime('%Y-%m-%d %H:%
        M')}")
            print(f"{'='*50}")
            print(f"    总计: {len(results)} 篇")
            print(f"    成功: {success} 篇 ({success/len(results)*100:.1
        f}%)")
            for src, cnt in sorted(by_source.items()):
                                        🔓             🏛️
                icon = {"unpaywall": " ", "core": " ", "pmc": "   🧬", "c
                  💾                ❌
        ached": " ", "failed": " "}.get(src, "?")
                print(f"   {icon} {src}: {cnt} 篇")
            print(f"    报告: {report_path}")
            print(f"{'='*50}\n")

            return results



        # ──────────────────────────────────────────────
        # 从文件读取 DOI 列表
        # ──────────────────────────────────────────────
        def load_dois(filepath: str) -> list[str]:
            """从 txt/csv 文件读取 DOI 列表（每行一个 DOI）"""
            dois = []
            with open(filepath, "r", encoding="utf-8") as f:
                 for line in f:
                      line = line.strip()
                      if line and not line.startswith("#"):
                          # 支持 URL 格式: https://doi.org/10.xxxx/yyyy
                          if "doi.org/" in line:
                              line = line.split("doi.org/")[-1]



第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                              20


---

                        dois.append(line)
            return list(dict.fromkeys(dois))   # 去重保序



        # ──────────────────────────────────────────────
        # 命令行入口
        # ──────────────────────────────────────────────
        if __name__ == "__main__":
            parser = argparse.ArgumentParser(description="批量论文全文获取
        — Unpaywall + CORE + PMC")
           parser.add_argument("input", help="DOI 列表文件（每行一个 DO
        I）")
            parser.add_argument("-o", "--output", default="papers", help
        ="PDF 输出目录")
            parser.add_argument("-e", "--email", required=True, help="你
        的邮箱（Unpaywall 需要）")
            parser.add_argument("-k", "--core-key", default="", help="CO
        RE API Key")
            parser.add_argument("-n", "--ncbi-key", default="", help="NC
        BI API Key（可选）")
            args = parser.parse_args()

            cfg = Config(
                 email=args.email,
                 core_api_key=args.core_key,
                 ncbi_api_key=args.ncbi_key,
                 output_dir=args.output,
            )


            dois = load_dois(args.input)
            if not dois:
                 print("   ❌ 未找到有效的 DOI，请检查输入文件")
                 exit(1)


            batch_fetch(dois, cfg)


       使用示例


        💻    Step 1 — 准备 DOI 文件 dois.txt （每行一个 DOI）：




第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                              21


---

        10.1038/s41586-023-06647-8
        10.1145/3580305.3599571
        10.1016/j.tourman.2023.104789
        https://doi.org/10.1177/00472875231180614
        10.1371/journal.pone.0287654




        💻    Step 2 — 运行脚本：


        # 安装依赖
        pip install requests tqdm

        # 基本用法
        python batch_paper_fetcher.py dois.txt -e your@email.com -k YOUR
        _CORE_KEY -o papers/

        # 带 NCBI Key（提高 PMC 限速）
        python batch_paper_fetcher.py dois.txt -e your@email.com -k YOUR
        _CORE_KEY -n YOUR_NCBI_KEY




        💻    Step 3 — 输出结构：


        papers/
        ├── 10.1038_s41586-023-06647-8.pdf
        ├── 10.1145_3580305.3599571.pdf
        ├── 10.1016_j.tourman.2023.104789.pdf
        ├── 10.1371_journal.pone.0287654.pdf
        └── download_report.csv          ← 包含每篇论文的来源和状态


       进阶用法：n8n 自动化集成架构


        🔧    进阶用法：将批量获取集成到 n8n 工作流，实现 Zotero 新增文献 → 自动获取全
             文 → 存入 Obsidian + Hermes（OpenCode / DeepSeek Harness）。




第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                              22


---

         flowchart LR
            ZOT[" 📚 Zotero<br>新增文献触发"] --> N8N["⚡ n8n 工作流"]
            N8N --> DOI["提取 DOI"]
            DOI --> UP_NODE["Unpaywall<br>HTTP Request"]
            UP_NODE --> CHECK1{"有 PDF？"}
                        ✅
            CHECK1 -->|" "| DL["下载 PDF"]
            CHECK1 -->|"❌"| CORE_NODE["CORE API<br>HTTP Request"]
            CORE_NODE --> CHECK2{"有 PDF？"}
            CHECK2 -->|"✅"| DL
            CHECK2 -->|"❌"| PMC_NODE["PMC API<br>HTTP Request"]
            PMC_NODE --> CHECK3{"有 PDF？"}
            CHECK3 -->|"✅"| DL
            CHECK3 -->|"❌"| NOTIFY["📧 通知<br>未找到全文"]
            DL --> NOTION["📋 Obsidian + Hermes（OpenCode / DeepSeek Harness）<br>更新文献记录<br>附件 PDF"]
            style N8N fill:#FF6D00,stroke:#E65100,color:#fff
            style DL fill:#E8F5E9,stroke:#2E7D32
            style NOTIFY fill:#FFEBEE,stroke:#C62828
                                                                                                               ✅                                        📋 Obsidian + Hermes（OpenCode / DeepSeek Harness）
                           📚 Zotero   ⚡ n8n 工作流             Unpaywall
                                                                          有 PDF？                                       ✅                       下载 PDF   更新文献记录
                           新增文献触发
                                                  提取 DOI
                                                           HTTP Request            ❌    CORE API
                                                                                                                                           ✅             附件 PDF

                                                                                                      有 PDF？
                                                                                       HTTP Request            ❌                               📧 通知
                                                                                                                     PMC API
                                                                                                                   HTTP Request
                                                                                                                                  有 PDF？   ❌   未找到全文




       Academic Claw 首发版




第 2 课C — 高级文献管理与综述·工具联动与可视化分析                                                                                                                                      23


---

