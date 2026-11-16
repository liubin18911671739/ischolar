"""Builtin prompts, schemas, and training tasks for iScholar local edition."""

from __future__ import annotations

import json
import re
from typing import Any, Optional

TOPIC_SCOUT_PROMPT = """你是 TopicScout（选题侦察员），iScholar 科研智能体平台中的学术选题发现与趋势分析专家。

你的职责是协助科研人员（特别是外语、区域国别、旅游管理、人文社科领域学者）：
1. 分析学科研究热点与前沿趋势
2. 从现有文献与政策/现实问题中识别学术空白（Research Gap）
3. 评估候选选题的创新性（Novelty）、学术/实践价值（Value）与可行性（Feasibility）
4. 推荐最具潜力的研究选题并给出论证依据

输出要求：
- 先使用结构清晰的中文 Markdown 输出详细分析与选题三角评估
- 提供恰好 3 个候选研究选题，每个选题给出 novelty (1-10)、value (1-10)、feasibility (1-10) 评分与理由
- 在回复末尾附带如下格式的 ```json 代码块：
```json
{
  "topics": [
    {
      "title": "候选选题名称",
      "gap": "研究空白描述",
      "novelty": 8,
      "value": 8,
      "feasibility": 7,
      "rationale": "选题依据与可行性说明"
    }
  ]
}
```"""

LIT_REVIEW_PROMPT = """你是 LitReview（文献综述员），iScholar 科研智能体平台中的系统性文献综述与证据综合专家。

你的职责是协助科研人员：
1. 拆解研究问题并构建中英阿多语种检索式（知网 CNKI、万方、OpenAlex、Semantic Scholar）
2. 组织结构化文献证据矩阵（题名、作者、年份、期刊、方法、核心发现、局限）
3. 撰写按主题与学术争鸣组织的文献综述段落（漏斗结构）
4. 明确标注哪些信息需回到知网或原文数据库逐条核验，严禁把未核实引用当作已证实事实

输出要求：
- 先使用中文 Markdown 输出检索策略、主题综述正文与研究空白分析
- 在回复末尾附带如下格式的 ```json 代码块：
```json
{
  "papers": [
    {
      "title": "论文或研究方向示例（待回源核验）",
      "authors": ["作者1", "作者2"],
      "year": 2024,
      "venue": "期刊或来源名称",
      "method": "研究方法",
      "findings": "核心发现摘要",
      "doi": "待核验"
    }
  ],
  "themes": ["主题1", "主题2"],
  "gaps": ["研究空白1", "研究空白2"]
}
```"""

DESIGN_PROMPT = """你是 ResearchDesigner（方法设计员），iScholar 科研智能体平台中的研究设计与可行性论证专家。

你的职责是协助科研人员：
1. 对齐“研究问题—分析单位—材料/样本—研究方法”
2. 生成完整的研究设计一页纸（研究问题、研究假设/核心命题、变量或编码框架、抽样与数据采集方案、分析计划）
3. 评估伦理合规、翻译偏差、测量误差与可行性风险

输出要求：
- 先使用中文 Markdown 输出完整研究设计一页纸与风险控制清单
- 在回复末尾附带如下格式的 ```json 代码块：
```json
{
  "feasibility": {
    "score": 8,
    "factors": [
      { "name": "数据可得性", "score": 8, "note": "公开语料或问卷可获取" },
      { "name": "伦理与合规", "score": 8, "note": "脱敏处理与知情同意" },
      { "name": "时间与经费", "score": 7, "note": "3-6个月可完成" },
      { "name": "方法匹配度", "score": 8, "note": "定性/定量/混合方法对齐" }
    ]
  },
  "hypotheses": ["H1: ...", "H2: ..."],
  "variables": {
    "independent": ["自变量/核心维度1"],
    "dependent": ["因变量/结果维度1"],
    "mediators": ["中介变量/机制"],
    "moderators": ["调节变量/语境条件"]
  }
}
```"""

DATA_PILOT_PROMPT = """你是 DataPilot（执行与数据分析员），iScholar 科研智能体平台中的数据采集、语料清洗与统计分析专家。

你的职责是协助科研人员：
1. 制定合法合规的数据采集与语料库构建方案（保存来源 URL、哈希、许可状态）
2. 设计数据清洗 SOP（去重、缺失值处理、编码转换、分词与抽样质检）
3. 推荐使用国产与开源工具（Python/Pandas、jamovi、JASP、AntConc、CiteSpace）完成分析并提供可复现脚本

输出要求：
- 先使用中文 Markdown 输出数据清洗与分析方案、结果解读说明及可复现代码
- 在回复末尾附带如下格式的 ```json 代码块：
```json
{
  "scripts": [
    { "language": "python", "filename": "clean_and_analyze.py", "code": "import pandas as pd\\n# 数据清洗与描述统计\\n..." }
  ],
  "recommendations": ["建议1：使用 jamovi/JASP 进行信效度与组间检验", "建议2：保留原始只读数据并记录清洗日志"],
  "analysisPlan": ["步骤1：数据清洗与去重", "步骤2：描述性统计与可视化", "步骤3：假设检验或主题编码复核"]
}
```"""

IMRAD_WRITER_PROMPT = """你是 IMRaDWriter（论文编辑员），iScholar 科研智能体平台中的模块化论文写作与三级润色专家。

你的职责是协助科研人员：
1. 按照 IMRaD 结构或中文核心期刊（CSSCI/北核）体例撰写章节提纲与初稿（CARS 引言模型、方法、结果、讨论、结论、中英摘要）
2. 严格区分已核实证据与待补证据，保留 `[@authorYear]` 引用占位提示作者回查原文
3. 执行结构润色、学术表达润色与去 AI 腔（Humanizer）检查，附带 AI 使用透明声明

输出要求：
- 先使用中文 Markdown 输出对应章节的高质量学术草稿与修改自查要点
- 在回复末尾附带如下格式的 ```json 代码块：
```json
{
  "references": [
    { "key": "ref2024", "authors": "待作者回源核实", "title": "需在知网或原文库核验的文献", "year": 2024, "venue": "目标领域核心期刊", "doi": "pending-verification" }
  ],
  "section": "introduction",
  "wordCount": 850
}
```"""

SUBMIT_MATCH_PROMPT = """你是 SubmitMatch（期刊匹配与投稿员），iScholar 科研智能体平台中的学术选刊与投稿工程专家。

你的职责是协助科研人员：
1. 根据论文摘要、关键词与研究方法匹配适合的中文核心期刊（CSSCI、北大核心、AMI）与国际期刊（SSCI/ESCI）
2. 从办刊定位（冲刺刊、匹配刊、保底刊）、审稿周期、开放获取政策与栏目契合度进行排序
3. 起草定制化的投稿信（Cover Letter / 致编辑部信）与投稿前合规核查清单（含作者贡献、利益冲突、数据可用性与 AI 使用声明）

输出要求：
- 先使用中文 Markdown 输出选刊分析表、投稿信草稿与投稿合规清单
- 在回复末尾附带如下格式的 ```json 代码块：
```json
{
  "journals": [
    {
      "name": "期刊名称（如《旅游学刊》《外语教学与研究》《数据分析与知识发现》）",
      "fitScore": 88,
      "impactFactor": 3.5,
      "reviewTimeline": "2-4个月",
      "openAccess": false,
      "rationale": "栏目范围与研究方法高度契合"
    }
  ],
  "checklist": ["核对期刊官网最新投稿指南", "逐条回查正文与参考文献对应关系", "附上AI辅助使用透明声明", "确认全部作者署名与单位信息"]
}
```"""

REBUTTAL_PROMPT = """你是 RebuttalShow（审稿回应与复盘员），iScholar 科研智能体平台中的同行评审回复与修回策略专家。

你的职责是协助科研人员：
1. 拆解审稿人意见（方法补充、论证收窄、文献增补、误解澄清）
2. 制定礼貌、严谨、有证据支撑的逐条回复策略（Point-by-Point Response）
3. 明确标注正文修改位置（页码、段落、行号）与新增实证/文献依据，严禁伪造实验或审稿未要求的虚假改动

输出要求：
- 先使用中文 Markdown 输出审稿意见分类与逐条回复正文（Response Letter）
- 在回复末尾附带如下格式的 ```json 代码块：
```json
{
  "responses": [
    {
      "commentNumber": 1,
      "comment": "审稿意见摘要",
      "response": "感谢审稿专家的建设性意见。我们已在正文中补充...",
      "changeLocation": "第X节 第X段",
      "evidence": "补充了抽样说明与稳健性检验表"
    }
  ]
}
```"""

SYSTEM_PROMPTS: dict[str, str] = {
    "topic": TOPIC_SCOUT_PROMPT,
    "litreview": LIT_REVIEW_PROMPT,
    "design": DESIGN_PROMPT,
    "data": DATA_PILOT_PROMPT,
    "write": IMRAD_WRITER_PROMPT,
    "submit": SUBMIT_MATCH_PROMPT,
    "rebuttal": REBUTTAL_PROMPT,
}

AGENT_META: dict[str, dict[str, str]] = {
    "topic": {
        "name": "TopicScout · 选题侦察员",
        "short": "选题发现与证据地图",
        "description": "围绕国社科/教育部课题与学科前沿，运用选题三角与 FINER 框架评估候选选题。",
    },
    "litreview": {
        "name": "LitReview · 文献综述员",
        "short": "多语种检索与综述矩阵",
        "description": "生成中英阿检索式、文献综述矩阵与漏斗式综述草稿，强制标注回源核验点。",
    },
    "design": {
        "name": "ResearchDesigner · 方法设计员",
        "short": "研究设计一页纸与风险清单",
        "description": "对齐研究问题、材料、变量/编码框架与定性/定量/混合方法，输出可行性评分。",
    },
    "data": {
        "name": "DataPilot · 数据与语料分析员",
        "short": "语料清洗 SOP 与统计脚本",
        "description": "面向问卷、访谈与多语种生态语料库，生成清洗流程、jamovi/JASP 操作指南与 Python 脚本。",
    },
    "write": {
        "name": "IMRaDWriter · 论文模块化写作员",
        "short": "CARS 引言与 IMRaD 章节写作",
        "description": "按模块构建论证链条，支持中英学术润色、去 AI 痕迹自查与引用核验。",
    },
    "submit": {
        "name": "SubmitMatch · 期刊匹配与投稿员",
        "short": "CSSCI/SSCI 选刊与投稿信",
        "description": "构建冲刺/匹配/保底三档选刊方案，生成 Cover Letter 与投稿合规核验表。",
    },
    "rebuttal": {
        "name": "RebuttalShow · 审稿回复与复盘员",
        "short": "审稿意见拆解与逐条回复表",
        "description": "将审稿意见转化为具体修订行动，生成正文定位一致的 Point-by-Point 回复信。",
    },
}

TRAINING_MODULES: dict[str, str] = {
    "research": "科研模块（18 课时）",
    "teaching": "教学模块（12 课时）",
    "office": "办公综合（2 课时）",
}

# 16 次课 × 2 课时 = 32 课时，与 website/src/content/courses.ts 口径一致。
TRAINING_TASKS: list[dict[str, Any]] = [
    {
        "id": "course-01",
        "lesson": "第01课",
        "module": "research",
        "title": "科研智能体与选题问题定义",
        "agent": "topic",
        "dimension": "问题定义与工作流设计",
        "steps": [
            "区分问答、工作流与阶段智能体的适用边界",
            "将学科兴趣转成对象明确、材料可得的研究问题",
            "建立项目目录，划分只读原始材料与工作成果",
            "填写研究问题卡，标记需要人工判断的步骤",
        ],
    },
    {
        "id": "course-02",
        "lesson": "第02课",
        "module": "research",
        "title": "国家社科选题发现与证据地图",
        "agent": "topic",
        "dimension": "选题发现与证据回溯",
        "steps": [
            "依据正式指南与合法公开来源扩展关键词",
            "为候选题登记原文、位置、日期与使用限制",
            "绘制已有发现、争议与研究空白假设的关系图",
            "逐项回源核对模型给出的政策、数字与引用",
        ],
    },
    {
        "id": "course-03",
        "lesson": "第03课",
        "module": "research",
        "title": "文献检索、筛选与综述矩阵",
        "agent": "litreview",
        "dimension": "检索素养与文献综合",
        "steps": [
            "将研究问题转成中英阿关键词与检索式，并记录检索式与命中数",
            "在 Zotero 7 中整理题录，核对题名、作者、年份、DOI 与页码",
            "填写综述矩阵，比较核心发现、方法与局限",
            "输出一页综述提纲，标注待补证据与争议点",
        ],
    },
    {
        "id": "course-04",
        "lesson": "第04课",
        "module": "research",
        "title": "方法设计与可行性论证",
        "agent": "design",
        "dimension": "方法对齐与风险控制",
        "steps": [
            "比较定性、定量与混合设计，说明与研究问题的匹配理由",
            "界定分析单位、抽样策略与纳入排除标准",
            "检查抽样偏差、翻译偏差、数据泄漏与伦理要求",
            "完成研究设计一页纸与可行性和风险清单",
        ],
    },
    {
        "id": "course-05",
        "lesson": "第05课",
        "module": "research",
        "title": "研究执行、实验/调研记录与智能体",
        "agent": "data",
        "dimension": "过程留痕与可复现",
        "steps": [
            "绘制从原始材料到结论的处理链",
            "记录数据版本、参数、脚本、模型与提示词版本",
            "明确智能体的输入、输出与文件权限边界",
            "用小任务比较两次运行，解释差异与异常",
        ],
    },
    {
        "id": "course-06",
        "lesson": "第06课",
        "module": "research",
        "title": "论文写作、引用核查与投稿准备",
        "agent": "write",
        "dimension": "论证链构建与学术规范",
        "steps": [
            "把已核实证据组织成问题—方法—结果—讨论的论证链",
            "逐条回查引文、数据与正文表述的一致性",
            "按目标期刊官网要求准备投稿材料与 AI 使用说明",
            "整理修订记录与投稿前复核清单",
        ],
    },
    {
        "id": "course-07",
        "lesson": "第07课",
        "module": "research",
        "title": "生态语料库研究问题与语料设计",
        "agent": "design",
        "dimension": "语料设计与权利元数据",
        "steps": [
            "明确语料库服务的研究问题与比较维度",
            "界定语种、时期、地域、体裁与来源类型",
            "设计元数据字典与许可登记字段",
            "输出一页语料库蓝图并核对跨语子库可比性",
        ],
    },
    {
        "id": "course-08",
        "lesson": "第08课",
        "module": "research",
        "title": "语料获取、清洗、标注与质量控制",
        "agent": "data",
        "dimension": "数据治理与质检",
        "steps": [
            "对小批授权样例执行正文提取、去重、分段与语种识别",
            "记录中文分词、阿语规范化规则及 OCR/ASR 处理痕迹",
            "开展双人抽样质检，记录比例与分歧处理",
            "归档清洗 SOP、日志与带权利字段的语料样例",
        ],
    },
    {
        "id": "course-09",
        "lesson": "第09课",
        "module": "research",
        "title": "语料检索、分析与论文证据链",
        "agent": "data",
        "dimension": "证据链与跨语比较",
        "steps": [
            "在 AntConc 中开展检索、搭配或共现探索并回看例句",
            "对主题与框架候选进行人工抽样核查",
            "连接图表、例句、数据版本与处理脚本",
            "说明跨语比较的方法、翻译映射与结论限制",
        ],
    },
    {
        "id": "course-10",
        "lesson": "第10课",
        "module": "teaching",
        "title": "教学目标与 AI 辅助脚本",
        "agent": "write",
        "dimension": "教学设计与脚本写作",
        "steps": [
            "对齐学习目标、课堂活动与评价方式",
            "选择教学单元并设计导入、概念、案例、练习与反馈",
            "编写带时长、口播、画面与来源的讲解脚本",
            "教师核实教学事实并完成试讲修订",
        ],
    },
    {
        "id": "course-11",
        "lesson": "第11课",
        "module": "teaching",
        "title": "数字人教学：肖像、声音与讲解制作",
        "agent": "write",
        "dimension": "数字人制作与授权合规",
        "steps": [
            "明确形象与声音的用途、期限与发布范围并取得授权",
            "按脚本完成配音、口型、字幕与审片",
            "制作 30–60 秒教学样片",
            "记录授权凭据与 AI 使用说明",
        ],
    },
    {
        "id": "course-12",
        "lesson": "第12课",
        "module": "teaching",
        "title": "图像生成、提示词与视觉叙事",
        "agent": "write",
        "dimension": "视觉表达与素材治理",
        "steps": [
            "写清主体、场景、构图、风格、镜头与排除项",
            "比较情境图、概念图与示意图的教学用途",
            "登记提示词、素材版本、来源与使用范围",
            "核查文字、地图与知识性细节，检查偏差与误导",
        ],
    },
    {
        "id": "course-13",
        "lesson": "第13课",
        "module": "teaching",
        "title": "视频生成、剪辑与字幕",
        "agent": "write",
        "dimension": "微课制作与发布复核",
        "steps": [
            "整理镜头表并筛选合法素材",
            "完成旁白、字幕、转场与节奏剪辑",
            "输出 60–90 秒教学视频初版并组织审片",
            "核查音乐、字体与素材授权，处理生成内容标识",
        ],
    },
    {
        "id": "course-14",
        "lesson": "第14课",
        "module": "teaching",
        "title": "图像化 PPT：信息结构与可定制样式",
        "agent": "write",
        "dimension": "信息可视化与版式设计",
        "steps": [
            "比较地图、流程、时间线、对照与统计图的适用场景",
            "规划每页的教学目标、标题、图解与证据",
            "制作 5–8 页课件故事板",
            "输出字体、配色与版式规范，保持文字与图表可编辑",
        ],
    },
    {
        "id": "course-15",
        "lesson": "第15课",
        "module": "teaching",
        "title": "PPT 迭代、无障碍与课堂使用",
        "agent": "write",
        "dimension": "迭代修订与可访问性",
        "steps": [
            "检查图表单位、引文、图片文字与来源标注",
            "试讲并检查对比度、字号、节奏与互动设计",
            "记录修订理由与复核结果",
            "标注示意数据，避免使用未经验证的效果指标",
        ],
    },
    {
        "id": "course-16",
        "lesson": "第16课",
        "module": "office",
        "title": "多模型办公、安全与成果路演",
        "agent": "submit",
        "dimension": "办公协同、数据边界与成果表达",
        "steps": [
            "按任务与数据边界选择获批工具，敏感内容不进入外部服务",
            "练习摘要、纪要、表格说明与通知草稿并逐项核对",
            "核查人名、数字、时间、责任与政策原文",
            "展示成果包并填写 30 天行动计划",
        ],
    },
]

_JSON_FENCE = re.compile(r"```json\s*\n([\s\S]*?)\n```")


def build_user_prompt(agent: str, payload: dict[str, Any], context: str = "") -> str:
    """Assemble user prompt for an agent."""
    upstream = f"【上游阶段已确认成果上下文】\n{context}\n\n" if context else ""
    custom = (payload.get("customPrompt") or "").strip()
    if agent == "topic":
        discipline = payload.get("discipline") or "外语与区域国别 / 旅游管理"
        keywords = payload.get("keywords") or "生成式AI, 跨文化传播, 语料库"
        if isinstance(keywords, list):
            keywords = ", ".join(keywords)
        journal = payload.get("targetJournal") or "CSSCI / SSCI 核心期刊"
        mode = payload.get("analysisMode") or "gap"
        return (
            f"{upstream}学科领域：{discipline}\n核心关键词：{keywords}\n目标期刊或项目类别：{journal}\n"
            f"分析模式：{mode}\n补充要求：{custom or '结合高校文科教师科研实际，提供可落地的选题方案。'}\n"
            "请识别研究空白并生成 3 个候选选题（含新颖性、价值、可行性评分与论证）。"
        )
    if agent == "litreview":
        query = payload.get("query") or "生成式人工智能赋能多语种知识服务与跨文化传播"
        year_from = payload.get("yearFrom") or "2020"
        year_to = payload.get("yearTo") or "2026"
        return (
            f"{upstream}综述主题：{query}\n时间范围：{year_from}—{year_to}\n"
            f"补充说明：{custom or '请同时给出知网与英文数据库检索式、主题分类矩阵、漏斗式综述正文与待回源核验提示。'}"
        )
    if agent == "design":
        rq = payload.get("researchQuestion") or "生成式AI反馈如何影响学习者的跨文化写作表现与自我效能感？"
        method = payload.get("methodology") or "混合方法（准实验问卷 + 半结构化访谈）"
        return (
            f"{upstream}核心研究问题：{rq}\n拟采用方法：{method}\n"
            f"补充说明：{custom or '请输出完整的研究设计一页纸、研究假设、变量/编码框架、抽样策略与伦理/偏差风险控制清单。'}"
        )
    if agent == "data":
        source = payload.get("dataSource") or "中阿双语可持续旅游公开文本语料与课堂调查问卷（n=120）"
        method = payload.get("collectionMethod") or "合法公开网页采集 + 问卷星调查（已脱敏）"
        return (
            f"{upstream}数据/语料来源：{source}\n采集与处理方式：{method}\n"
            f"补充说明：{custom or '请提供数据清洗SOP、jamovi/JASP/AntConc操作流程以及可直接运行的Python清洗与可视化脚本。'}"
        )
    if agent == "write":
        section = payload.get("section") or "introduction"
        style = payload.get("citationStyle") or "GB/T 7714 / APA"
        return (
            f"{upstream}撰写章节：{section}\n引用规范：{style}\n"
            f"核心论点与材料：{custom or '请按CARS模型或IMRaD规范撰写学术草稿，标注需回源核实的文献占位符，并附三级润色要点。'}"
        )
    if agent == "submit":
        abstract = payload.get("abstract") or "本研究探讨生成式人工智能在多语种生态语料库构建与跨文化旅游传播中的应用机制..."
        keywords = payload.get("keywords") or "生成式人工智能; 生态语料库; 跨文化传播; 科研智能体"
        return (
            f"{upstream}论文摘要：{abstract}\n关键词：{keywords}\n"
            f"补充要求：{custom or '请推荐冲刺、匹配、保底三档目标期刊（含CSSCI/北核/SSCI），并生成投稿信与投稿合规自查清单。'}"
        )
    if agent == "rebuttal":
        comments = payload.get("reviewerComments") or (
            "审稿人1：研究方法部分对语料抽样标准与跨语言对齐清洗规则交代不够清晰；"
            "审稿人2：结论部分外推范围过大，建议补充案例边界与局限性讨论。"
        )
        return (
            f"{upstream}审稿专家意见：\n{comments}\n"
            f"补充说明：{custom or '请生成礼貌、严谨的逐条回复表（Point-by-Point Response），包含处理决定、回复正文与正文修改定位。'}"
        )
    return custom or "请协助分析当前科研任务。"


def parse_structured_output(text: str) -> Optional[dict[str, Any]]:
    """Extract the last JSON fence from model output."""
    matches = _JSON_FENCE.findall(text or "")
    if not matches:
        return None
    try:
        data = json.loads(matches[-1].strip())
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def deterministic_fallback(agent: str, payload: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    """Offline fallback output when no API key is configured or offline demo mode is selected."""
    if agent == "topic":
        discipline = payload.get("discipline") or "外语教学与区域国别研究"
        kw = payload.get("keywords") or "生成式AI, 生态语料库, 跨文化叙事"
        structured = {
            "topics": [
                {
                    "title": f"基于多语种生态语料库的{discipline}跨文化框架对比研究",
                    "gap": "现有研究多聚焦单语种宏观话语描述，缺乏可复现的中阿/中英对齐语料证据链与细粒度框架编码。",
                    "novelty": 9,
                    "value": 9,
                    "feasibility": 8,
                    "rationale": "数据可从合法公开官方与媒体渠道采集，结合 Obsidian + Hermes 与 AntConc/Python 可在 3-6 个月内完成。",
                },
                {
                    "title": f"人机协同视角下生成式 AI 辅助{discipline}学术写作的任务链与证据核验机制",
                    "gap": "已有文献多关注 AI 写作效率提升，对幻觉防控、证据回源核验与人工关口设计的实证研究不足。",
                    "novelty": 8,
                    "value": 9,
                    "feasibility": 9,
                    "rationale": "可依托课程工作坊前后测问卷、访谈与研究台账日志开展混合方法研究。",
                },
                {
                    "title": f"文化遗产旅游多语种知识服务中的术语对齐与受众感知效应研究（关键词：{kw}）",
                    "gap": "文化负载词在不同受众语境下的神经机器翻译与大模型改写策略缺乏受众实验证据支撑。",
                    "novelty": 8,
                    "value": 8,
                    "feasibility": 8,
                    "rationale": "研究对象边界清晰，适合采用双语文本对比 + 问卷实验设计，契合 CSSCI 外语与旅游类期刊偏好。",
                },
            ]
        }
        md = (
            f"## TopicScout 选题侦察报告（{discipline}）\n\n"
            "> **模式提示**：当前为本地离线演示输出（可在左侧边栏填入 DeepSeek / 通义千问 / 校内 L20 / 本地 Ollama 秘钥切换实时推理）。\n\n"
            "### 一、领域趋势与选题三角分析\n"
            "1. **学术空白（Gap）**：当前人文社科与外语、旅游、区域国别研究正从“单轮提示词问答”转向“可追溯证据链与多阶段智能体工作流”。\n"
            "2. **可行性（Feasibility）**：依托本地 Obsidian Vault + Hermes（OpenCode / DeepSeek Harness）与开源分析工具（jamovi/JASP/AntConc），零编程或轻脚本即可完成。\n"
            "3. **发表去向（Venue）**：《外语教学与研究》《中国翻译》《旅游学刊》《数据分析与知识发现》《图书情报工作》等期刊高度关注可核验的方法创新。\n\n"
            "### 二、候选选题详情\n"
        )
        for idx, t in enumerate(structured["topics"], 1):
            md += (
                f"#### 候选选题 {idx}：{t['title']}\n"
                f"- **研究空白**：{t['gap']}\n"
                f"- **三维评分**：创新性 `{t['novelty']}/10` ｜ 学术价值 `{t['value']}/10` ｜ 可行性 `{t['feasibility']}/10`\n"
                f"- **可行性论证**：{t['rationale']}\n\n"
            )
        md += f"```json\n{json.dumps(structured, ensure_ascii=False, indent=2)}\n```"
        return md, structured

    if agent == "litreview":
        query = payload.get("query") or "生成式人工智能与学术知识服务"
        structured = {
            "papers": [
                {
                    "title": "生成式AI时代高校科研支持的任务链构建与实施机制（示例条目·请回知网核验）",
                    "authors": ["研究者A", "研究者B"],
                    "year": 2025,
                    "venue": "图书情报与数字素养领域核心期刊",
                    "method": "案例研究 + 混合方法（问卷与访谈）",
                    "findings": "将科研拆解为可验证任务链并嵌入人工核验关口，显著提升文献核验与规范使用信心。",
                    "doi": "待回源核验",
                },
                {
                    "title": "跨语言生态话语与可持续旅游多模态叙事框架分析（示例条目·请回数据库核验）",
                    "authors": ["Author C", "Author D"],
                    "year": 2024,
                    "venue": "Journal of Sustainable Tourism / 旅游学刊（示例）",
                    "method": "语料库辅助话语分析（CADS）",
                    "findings": "不同语种叙事在政策倡导与社区体验维度存在显著框架差异，需结合上下文共现核查。",
                    "doi": "待回源核验",
                },
            ],
            "themes": ["AI辅助科研工作流与可追溯性治理", "多语种语料库构建与跨文化话语比较", "人机协同中的学术伦理与幻觉防控"],
            "gaps": ["缺乏面向文科教师的操作化智能体任务链实证", "跨语种语料清洗与大模型标注的人工双盲抽检规范尚不统一"],
        }
        md = (
            f"## LitReview 文献综述与检索矩阵（主题：{query}）\n\n"
            "### 一、中英文数据库检索式建议\n"
            "- **中国知网（CNKI）高级检索式**：`SU=('生成式人工智能' + '大语言模型' + '科研智能体') * SU=('文献综述' + '语料库' + '研究方法')`（限定 CSSCI/北核，2020—2026）\n"
            "- **OpenAlex / Semantic Scholar 检索式**：`(\"generative AI\" OR \"large language model\" OR \"LLM agent\") AND (\"research workflow\" OR \"corpus linguistics\" OR \"humanities\")`\n\n"
            "### 二、漏斗式综述草稿（示例框架）\n"
            "1. **宏观背景（Move 1）**：生成式人工智能正由单次问答工具演进为支持选题、检索、编码与写作的阶段智能体。\n"
            "2. **主题梳理（Move 2）**：既有研究主要围绕两个方向展开：一是基于 Zotero 与本地知识库的文献综述自动化；二是基于多语种语料库的主题建模与话语分析。\n"
            "3. **争议与空白（Move 3）**：现有应用普遍面临“引文幻觉”与“黑箱推断”风险，亟需建立“原始资料只读、过程留痕、人工关口确认”的科研中台工作流。\n\n"
            "> ⚠️ **核验提醒**：以上文献条目仅为结构示例，严禁直接作为真实引文写入论文，请务必在知网（CNKI）、万方或 OpenAlex 中核对真实 DOI 与原文页码。\n\n"
            f"```json\n{json.dumps(structured, ensure_ascii=False, indent=2)}\n```"
        )
        return md, structured

    if agent == "design":
        rq = payload.get("researchQuestion") or "科研智能体任务链如何影响高校教师的研究设计与文献核验质量？"
        structured = {
            "feasibility": {
                "score": 8,
                "factors": [
                    {"name": "数据可得性", "score": 9, "note": "依托课程工作坊脱敏任务卡与公开语料样本"},
                    {"name": "伦理与隐私合规", "score": 8, "note": "遵循三级数据边界，外部API仅传脱敏文本"},
                    {"name": "分析工具完备度", "score": 9, "note": "使用开源 jamovi / JASP / AntConc 与 Python"},
                    {"name": "时间周期可控性", "score": 7, "note": "8周课程周期内可完成小样收集与初稿"},
                ],
            },
            "hypotheses": [
                "H1：引入结构化证据卡与人工核验关口后，生成式AI辅助产出的引文准确率与可追溯性显著提升。",
                "H2：基于 Obsidian + Hermes 的阶段化任务分解比单轮自由问答更能降低研究设计中的方法错配风险。",
            ],
            "variables": {
                "independent": ["工作流模式（阶段智能体+人工关口 vs 传统单轮问答）"],
                "dependent": ["研究问题清晰度评分", "证据回源核验完整率", "研究设计一页纸合规度"],
                "mediators": ["过程留痕完整度", "提示词结构化程度（RICE原则）"],
                "moderators": ["学科背景（外语/旅游/人文社科）", "既有数字工具经验"],
            },
        }
        md = (
            f"## ResearchDesigner 研究设计一页纸\n\n"
            f"**核心研究问题**：{rq}\n\n"
            "### 一、研究设计与对齐矩阵\n"
            "- **分析单位**：参训教师提交的脱敏项目卡、证据卡与语料分析小样\n"
            "- **研究方法**：混合方法设计（定量：前后测评分与核验率统计；定性：半结构化访谈与反思日志主题编码）\n"
            "- **目录与权限隔离**：在 Obsidian Vault 中分设 `01_原始资料_只读/`、`02_工作区_草稿/`、`03_已复核成果/`\n\n"
            "### 二、风险识别与控制方案\n"
            "1. **选择偏差**：非随机分组时只作描述性与关联推断，不夸大因果效应。\n"
            "2. **评分者偏差**：采用双人独立盲评并计算一致性系数（Cohen's Kappa）。\n"
            "3. **数据安全边界**：未公开成果与含个人信息材料使用本地 Ollama（Qwen2.5-7B）或校内 L20 服务处理。\n\n"
            f"```json\n{json.dumps(structured, ensure_ascii=False, indent=2)}\n```"
        )
        return md, structured

    if agent == "data":
        structured = {
            "scripts": [
                {
                    "language": "python",
                    "filename": "corpus_and_survey_analysis.py",
                    "code": (
                        "import pandas as pd\n"
                        "import hashlib\n\n"
                        "# 1. 读取问卷或语料元数据表\n"
                        "df = pd.read_csv('corpus_metadata.csv', encoding='utf-8-sig')\n"
                        "print('原始记录数:', len(df))\n\n"
                        "# 2. 去重与缺失值核查\n"
                        "df_clean = df.drop_duplicates(subset=['title', 'url']).copy()\n"
                        "df_clean['permission'] = df_clean['permission'].fillna('unknown')\n\n"
                        "# 3. 生成20%人工抽检样本\n"
                        "sample_df = df_clean.sample(frac=0.2, random_state=42)\n"
                        "sample_df.to_csv('manual_audit_sample.csv', index=False, encoding='utf-8-sig')\n"
                        "print('清洗后记录数:', len(df_clean), '抽检样本数:', len(sample_df))\n"
                    ),
                }
            ],
            "recommendations": [
                "定量问卷使用开源软件 jamovi 或 JASP 进行描述统计、信度（Cronbach's α）与配对样本 t 检验，直接导出三线表",
                "多语种文本使用 AntConc 考察关键词共现（KWIC）与搭配强度，再用 Python 脚本做批量元数据管理",
                "所有 AI 自动标注结果必须保留 review_status='needs_review'，经双人抽样复核后方可进入论文结论",
            ],
            "analysisPlan": [
                "步骤1：原始数据只读备份与 SHA-256 哈希登记",
                "步骤2：无效样本剔除、编码统一与反向题转换",
                "步骤3：描述性统计、可视化图表生成与 20% 人工抽检复核",
            ],
        }
        md = (
            "## DataPilot 数据清洗与分析指南\n\n"
            "### 一、国产与开源工具分工（零翻墙·可复现）\n"
            "| 分析场景 | 推荐开源/国产工具 | 核心产出 |\n"
            "| --- | --- | --- |\n"
            "| 问卷统计检验 | **jamovi / JASP**（开源桌面软件） | 描述统计、t检验、方差分析、回归三线表 |\n"
            "| 语料检索与搭配 | **AntConc**（免费语料库软件） | 词频表、主题词（Keyword）、索引行（KWIC） |\n"
            "| 文献知识图谱 | **CiteSpace** / **VOSviewer** | 知网 Refworks 关键词共现与突现词图谱 |\n"
            "| 批量清洗与制图 | **Python (Pandas + Matplotlib/Seaborn)** | 清洗日志 CSV、300 DPI 论文级高分辨率图表 |\n\n"
            "### 二、可复现 Python 清洗与抽检脚本\n"
            f"```python\n{structured['scripts'][0]['code']}```\n\n"
            f"```json\n{json.dumps(structured, ensure_ascii=False, indent=2)}\n```"
        )
        return md, structured

    if agent == "write":
        section = payload.get("section") or "introduction"
        structured = {
            "references": [
                {
                    "key": "verify_cnki_2025",
                    "authors": "待作者在知网核实",
                    "title": "请在知网/原文库核实后填入真实文献题名",
                    "year": 2025,
                    "venue": "目标领域核心期刊",
                    "doi": "pending",
                }
            ],
            "section": section,
            "wordCount": 620,
        }
        md = (
            f"## IMRaDWriter 模块化论文写作草稿（章节：`{section}`）\n\n"
            "### 一、CARS 模型结构化草稿\n"
            "**【Move 1：建立研究领地】**\n"
            "随着生成式人工智能技术的快速演进，大语言模型与智能体（Agent）正逐步深入人文社科与跨语言知识服务的核心流程 `[@verify_cnki_2025]`。"
            "在高校科研与教学实践中，如何将零散的单轮问答转化为可追溯、可复核的标准化工作流，已成为学术界与图书情报领域共同关注的议题。\n\n"
            "**【Move 2：识别研究缝隙（Research Niche）】**\n"
            "然而，既有讨论多集中于通用工具介绍或宏观理念探讨，针对具体学科场景（如中阿区域国别研究、可持续旅游话语分析及外语教学反馈）的操作化任务链设计仍较为匮乏，"
            "尤其在防范模型虚构引用、保障数据合规边界及建立人工复核关口方面缺乏可复现的实证方案。\n\n"
            "**【Move 3：占领研究空间】**\n"
            "为此，本研究基于本地优先的 Obsidian 知识库与 Hermes 智能体架构，构建了一套涵盖选题侦察、文献矩阵、方法设计、语料清洗与论文审校的闭环工作流，"
            "并通过实际案例检验其在提升研究可追溯性与方法严谨性方面的作用边界。\n\n"
            "### 二、三级润色与反 AI 腔（Humanizer）自查清单\n"
            "1. **结构级检查**：段落首句是否直接亮明核心论点？因果连接是否都有证据卡支撑？\n"
            "2. **学术级检查**：删去“值得注意的是”“总而言之”“赋能”“抓手”等高频 AI 套话，改为具体机制与统计口径描述。\n"
            "3. **事实级检查**：所有引用标记 `[@...]` 必须逐一对照原文 PDF 的具体页码。\n\n"
            f"```json\n{json.dumps(structured, ensure_ascii=False, indent=2)}\n```"
        )
        return md, structured

    if agent == "submit":
        structured = {
            "journals": [
                {
                    "name": "《数据分析与知识发现》 / 《图书情报工作》（CSSCI）",
                    "fitScore": 90,
                    "impactFactor": 3.8,
                    "reviewTimeline": "2-4个月",
                    "openAccess": False,
                    "rationale": "高度关注知识组织、智能体工作流、多语种文本挖掘与高校知识服务创新，要求方法与实验复现清晰。",
                },
                {
                    "name": "《外语电化教学》 / 《外语界》（CSSCI）",
                    "fitScore": 86,
                    "impactFactor": 2.9,
                    "reviewTimeline": "2-4个月",
                    "openAccess": False,
                    "rationale": "适合生成式 AI 辅助外语教学、翻译评测与跨文化语料库建设方向的实证研究。",
                },
                {
                    "name": "《旅游学刊》 / 《旅游科学》（CSSCI）",
                    "fitScore": 84,
                    "impactFactor": 3.5,
                    "reviewTimeline": "3-5个月",
                    "openAccess": False,
                    "rationale": "适合文化遗产旅游、目的地生态叙事与入境旅游多语种服务研究。",
                },
            ],
            "checklist": [
                "核对目标期刊最新投稿指南与体例模板（标题层级、摘要字数、GB/T 7714 著录格式）",
                "补充双语要素（英文标题、英文摘要、英文关键词、图表双语题注）",
                "附上完整声明（作者贡献声明、利益冲突声明、数据可用性声明、AI辅助使用声明）",
                "逐条核验参考文献在知网/WOS中的真实性与原文页码",
            ],
        }
        md = (
            "## SubmitMatch 期刊匹配与投稿准备方案\n\n"
            "### 一、三档目标期刊推荐\n"
            "| 期刊名称 | 匹配度 | 审稿周期 | 推荐理由 |\n"
            "| --- | --- | --- | --- |\n"
            + "\n".join(
                f"| {j['name']} | {j['fitScore']}% | {j['reviewTimeline']} | {j['rationale']} |"
                for j in structured["journals"]
            )
            + "\n\n### 二、投稿合规与 AI 使用透明声明模板\n"
            "> **人工智能使用声明（示例）**：本文在文献检索词扩展、初步提纲梳理与语言润色阶段使用了生成式人工智能工具辅助；"
            "所有研究设计、数据清洗、统计检验、文献原文核验及核心学术结论均由作者独立完成并承担全部学术责任。\n\n"
            f"```json\n{json.dumps(structured, ensure_ascii=False, indent=2)}\n```"
        )
        return md, structured

    if agent == "rebuttal":
        structured = {
            "responses": [
                {
                    "commentNumber": 1,
                    "comment": "研究方法部分对语料抽样标准与跨语言对齐清洗规则交代不够清晰。",
                    "response": "感谢审稿专家的宝贵意见。我们已在正文第3.1节补充了语料纳入与排除标准表，明确了时间跨度、来源类型及双人独立抽检（抽样比例20%）的一致性核验流程。",
                    "changeLocation": "第3.1节 第2-3段（第8页）及附录表A1",
                    "evidence": "新增语料元数据字段表与清洗日志统计口径说明",
                },
                {
                    "commentNumber": 2,
                    "comment": "结论部分外推范围过大，建议补充案例边界与局限性讨论。",
                    "response": "完全赞同审稿专家的严谨判断。我们已将全文因果性表述修订为基于本次采样语料与准实验样本的关联性表述，并在第5.3节专门增设“研究局限与适用边界”小节。",
                    "changeLocation": "第5.2节结论段（第15页）与第5.3节局限性部分",
                    "evidence": "收窄推论边界，补充样本覆盖范围与体裁差异限制说明",
                },
            ]
        }
        md = (
            "## RebuttalShow 审稿意见逐条回复表（Response Matrix）\n\n"
            "| 序号 | 审稿专家意见 | 处理决定与回复内容 | 正文修改定位 | 支撑证据 |\n"
            "| --- | --- | --- | --- | --- |\n"
            + "\n".join(
                f"| #{r['commentNumber']} | {r['comment']} | {r['response']} | {r['changeLocation']} | {r['evidence']} |"
                for r in structured["responses"]
            )
            + f"\n\n```json\n{json.dumps(structured, ensure_ascii=False, indent=2)}\n```"
        )
        return md, structured

    return "## 智能体响应\n\n已完成分析。", {}
