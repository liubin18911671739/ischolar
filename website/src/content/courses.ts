export type ModuleId = "research" | "teaching" | "office";
export type TopicId = "research-agent" | "corpus" | "creation" | "slides" | "office";

export const modules: Record<ModuleId, { label: string; short: string }> = {
  research: { label: "科研", short: "研究与证据" },
  teaching: { label: "教学", short: "表达与创作" },
  office: { label: "办公", short: "协同与复核" },
};

export const topics: Record<TopicId, { label: string; href: string; module: ModuleId }> = {
  "research-agent": { label: "科研智能体与论文", href: "/research", module: "research" },
  corpus: { label: "生态语料库", href: "/corpus", module: "research" },
  creation: { label: "教学内容生产", href: "/creation", module: "teaching" },
  slides: { label: "图像化 PPT", href: "/slides", module: "teaching" },
  office: { label: "办公与综合", href: "/office", module: "office" },
};

export interface Course {
  id: string;
  number: number;
  week: number;
  hours: number;
  module: ModuleId;
  topic: TopicId;
  title: string;
  summary: string;
  goals: string[];
  tasks: string[];
  outputs: string[];
  tools: string[];
  review: string[];
  resourceIds: string[];
}

const records: Omit<Course, "id" | "number" | "week" | "hours" | "module">[] = [
  {
    topic: "research-agent", title: "科研智能体与选题问题定义",
    summary: "从真实研究问题出发，搭建 Obsidian 研究台账与 Hermes 步骤编排的基本框架。",
    goals: ["区分问答、工作流和阶段智能体", "将学科兴趣转成对象明确、材料可得的研究问题"],
    tasks: ["比较中阿生态叙事与旅游目的地传播两个演练方向", "建立项目目录，划分只读原始材料与工作成果", "填写研究问题卡，标记需要人工判断的步骤"],
    outputs: ["一张项目卡", "一个可继续使用的研究工作区目录"],
    tools: ["Obsidian", "Hermes Agent（OpenCode / DeepSeek Harness）", "iScholar 本地工作台", "DeepSeek / 校内获批模型"],
    review: ["研究问题由研究者确认", "原始材料不由智能体直接覆盖", "示例选题不预设结论"], resourceIds: ["project-card", "ai-record"],
  },
  {
    topic: "research-agent", title: "国家社科选题发现与证据地图",
    summary: "连接政策、学术争论与现实问题，为候选选题建立可回溯的来源依据。",
    goals: ["辨别问题线索与已证实事实", "比较候选题的学术价值和材料可行性"],
    tasks: ["依据正式指南和合法公开来源扩展关键词", "为候选题登记原文、位置、日期和使用限制", "绘制已有发现、争议与研究空白假设的关系"],
    outputs: ["候选选题比较表", "选题证据地图"], tools: ["学校图书馆数据库", "Obsidian", "校内模型"],
    review: ["使用正式公布的指南版本", "研究空白需要文献支持", "模型给出的政策、数字和引用逐项回源"], resourceIds: ["project-card", "evidence-card"],
  },
  {
    topic: "research-agent", title: "文献检索、筛选与综述矩阵",
    summary: "通过检索式、筛选记录和文献矩阵，组织有证据支持的综述提纲。",
    goals: ["将问题转成中阿英关键词与检索式", "形成按主题、方法和争议组织的文献综述"],
    tasks: ["记录检索来源、检索式和筛选标准", "核对题名、作者、年份、DOI 和原文位置", "填写综述矩阵，比较发现与局限"],
    outputs: ["文献综述矩阵", "一页综述提纲"], tools: ["合法可访问的文献数据库", "文献管理工具", "Obsidian"],
    review: ["摘要不能代替原文核验", "AI 标签只作为候选", "不让模型补造未找到的引用"], resourceIds: ["literature-matrix", "evidence-card"],
  },
  {
    topic: "research-agent", title: "方法设计与可行性论证",
    summary: "让研究问题、分析单位、材料和方法相互对应，提前识别偏差与实施风险。",
    goals: ["说明方法为何适合研究问题", "制定抽样、分析和复核方案"],
    tasks: ["比较定性、定量与混合设计", "为中阿话语或旅游管理案例填写方法卡", "检查抽样偏差、翻译偏差、数据泄漏和伦理要求"],
    outputs: ["方法设计卡", "可行性与风险清单"], tools: ["方法卡模板", "表格工具", "校内模型（辅助提出备选）"],
    review: ["方法选择由研究者决定", "数据取得与使用范围需明确", "分析计划修改应记录理由"], resourceIds: ["method-card", "evidence-card"],
  },
  {
    topic: "research-agent", title: "研究执行、实验/调研记录与智能体",
    summary: "把整理、分析与异常记录变成可重复执行的步骤，并保留人工确认点。",
    goals: ["记录一次可复现的运行", "明确智能体的输入、输出与文件权限"],
    tasks: ["绘制原始材料到结论的处理链", "记录数据版本、参数、脚本、模型与提示词版本", "用小任务比较两次运行，解释差异和异常"],
    outputs: ["运行日志与复现说明", "阶段智能体职责表"], tools: ["Hermes Agent（OpenCode / DeepSeek Harness）", "iScholar 本地工作台", "Python / Jupyter", "Git 版本管理"],
    review: ["真实观测、模拟示例和模型建议分开记录", "失败与负结果保留", "智能体不得未经批准更改研究方案"], resourceIds: ["run-log", "ai-record", "method-card"],
  },
  {
    topic: "research-agent", title: "论文写作、引用核查与投稿准备",
    summary: "将论证连接到证据，完成结构编辑、引文核验和投稿材料准备。",
    goals: ["构建问题、方法、结果和讨论的论证链", "按期刊实际要求准备投稿与 AI 使用说明"],
    tasks: ["把已核实证据组织成论文提纲", "逐条回查引文与研究结果", "依据期刊官网范围和规范整理投稿材料及修订记录"],
    outputs: ["论文提纲", "引用核验表与投稿准备清单"], tools: ["文字编辑器", "文献管理工具", "目标期刊官方网站"],
    review: ["作者负责事实、贡献和署名", "AI 不代替作者决定投稿", "按学校及期刊要求披露 AI 辅助"], resourceIds: ["literature-matrix", "output-review", "ai-record"],
  },
  {
    topic: "corpus", title: "生态语料库研究问题与语料设计",
    summary: "以中阿生态叙事或可持续旅游为演练题，规划子库、抽样与权利元数据。",
    goals: ["明确语料库服务的研究问题", "建立可比较、可追踪的子库结构"],
    tasks: ["界定语种、时期、地域、体裁和来源类型", "制定纳入排除标准与抽样策略", "设计元数据与许可登记字段"],
    outputs: ["一页语料库蓝图", "元数据字典"], tools: ["CSV / 表格工具", "Obsidian", "来源与许可登记"],
    review: ["题目仅作演练，不预设研究发现", "公开访问不等于可训练或可再发布", "跨语子库可比性需说明"], resourceIds: ["corpus-metadata", "method-card", "source-license"],
  },
  {
    topic: "corpus", title: "语料获取、清洗、标注与质量控制",
    summary: "保留原始材料及变更记录，对中文与阿拉伯语处理分别开展抽样质检。",
    goals: ["建立可审计的采集清洗流程", "记录标注规则、异常和分歧处理"],
    tasks: ["对小批授权样例执行正文提取、去重、分段和语种识别", "按需使用 OCR / ASR，并保留原文", "记录中文分词、阿语规范化及人工抽检结果"],
    outputs: ["清洗 SOP 与日志", "带权利字段的小批语料样例"], tools: ["Python / Jupyter", "OCR / ASR 候选工具", "CSV / SQLite"],
    review: ["遵守来源许可与平台条款", "个人信息与受限材料按制度处理", "双人抽检的真实比例和分歧必须记录"], resourceIds: ["cleaning-log", "corpus-metadata", "source-license"],
  },
  {
    topic: "corpus", title: "语料检索、分析与论文证据链",
    summary: "从关键词与上下文探索形成分析小样，让每条解释回指原始语料。",
    goals: ["区分探索结果、候选主题与研究结论", "说明跨语比较的方法和限制"],
    tasks: ["开展检索、搭配或共现探索并回看例句", "对主题与框架候选进行人工抽样核查", "连接图表、例句、数据版本和处理脚本"],
    outputs: ["可复现分析小样", "例句、图表与结论限制说明"], tools: ["语料检索工具", "Python / Jupyter", "Obsidian"],
    review: ["模型标签不能当作金标准", "跨语比较保留翻译与概念映射记录", "单次命中不能直接推出总体结论"], resourceIds: ["evidence-card", "run-log", "output-review"],
  },
  {
    topic: "creation", title: "教学目标与 AI 辅助脚本",
    summary: "从学生起点与学习目标出发，把内容写成带画面、来源和互动的脚本。",
    goals: ["对齐目标、活动与评价", "写出可进入分镜与视频制作的讲解脚本"],
    tasks: ["选择旅游或中阿区域教学单元", "设计导入、概念、案例、练习与反馈", "记录每段的时长、口播、画面和来源"],
    outputs: ["教学目标对齐表", "脚本与分镜初稿"], tools: ["校内模型", "文本编辑器", "脚本分镜模板"],
    review: ["教师核实教学事实", "AI 草稿须回源、改写和试讲", "练习对应学习目标"], resourceIds: ["video-script", "ai-record", "evidence-card"],
  },
  {
    topic: "creation", title: "数字人教学：肖像、声音与讲解制作",
    summary: "在获得授权的前提下制作短讲解，检查数字人输出与教学内容的匹配。",
    goals: ["判断数字人适用的教学场景", "理解人像、声音与生成内容的授权要求"],
    tasks: ["明确形象与声音的用途、期限和发布范围", "按脚本完成配音、口型、字幕与审片", "制作 30–60 秒教学样片"],
    outputs: ["数字人样片与项目文件", "授权和 AI 使用记录"], tools: ["经批准的数字人工具", "获授权配音或录音", "视频编辑工具"],
    review: ["肖像和声音取得授权", "核查口型、语速、字幕与事实", "教师负责互动、反馈和评价"], resourceIds: ["video-script", "source-license", "output-review"],
  },
  {
    topic: "creation", title: "图像生成、提示词与视觉叙事",
    summary: "根据教学用途选择视觉类型，形成可追溯、风格一致的素材包。",
    goals: ["将教学需求转成完整的图像提示词", "检查图像事实、偏差与跨页一致性"],
    tasks: ["写清主体、场景、构图、风格、镜头与排除项", "比较情境图、概念图与示意图的用途", "登记提示词、素材版本、来源与使用范围"],
    outputs: ["课程视觉素材包", "提示词与筛选记录"], tools: ["校内获批图像生成工具", "素材登记模板", "文本编辑器"],
    review: ["核实文字、地图和知识性细节", "检查偏差与误导", "生成图像不代替原始数据和证据"], resourceIds: ["image-prompt", "source-license", "ai-record"],
  },
  {
    topic: "creation", title: "视频生成、剪辑与字幕",
    summary: "用分镜组织素材，完成旁白、字幕与节奏剪辑，并做好发布前复核。",
    goals: ["让画面与讲解逐段对应", "保留可编辑项目及素材权利记录"],
    tasks: ["整理镜头表并筛选合法素材", "完成旁白、字幕、转场和剪影 / 蒙太奇片段", "输出 60–90 秒教学视频初版并审片"],
    outputs: ["教学视频初版", "可编辑项目、来源和标识说明"], tools: ["剪映或校内批准的剪辑工具", "视频生成候选工具", "字幕工具"],
    review: ["检查画面、旁白和字幕的一致性", "音乐、字体和素材分别核查授权", "按适用规范处理显式和隐式标识"], resourceIds: ["video-script", "source-license", "output-review"],
  },
  {
    topic: "slides", title: "图像化 PPT：信息结构与可定制样式",
    summary: "以教学任务组织页面，用清晰图解承载信息并保留可编辑文本与来源。",
    goals: ["根据内容关系选择合适的视觉类型", "形成可定制的课件样式与故事板"],
    tasks: ["比较地图、流程、时间线、对照与统计图", "规划每页的目标、标题、图解和证据", "制作 5–8 页课件故事板"],
    outputs: ["课件故事板", "字体、配色和版式规范"], tools: ["可编辑演示文稿工具", "故事板模板", "获授权图像素材"],
    review: ["每页有明确教学任务", "图像不替代数据与来源", "文字和图表保持可编辑"], resourceIds: ["slide-storyboard", "source-license"],
  },
  {
    topic: "slides", title: "PPT 迭代、无障碍与课堂使用",
    summary: "通过试讲与互评改进课件，检查大屏可读性、互动与信息可追溯性。",
    goals: ["识别学生理解过程中的障碍", "根据反馈记录修订并再次复核"],
    tasks: ["检查图表单位、引文、图片文字和来源", "试讲并检查对比度、字号、讲授节奏和互动", "记录修订理由和复核结果"],
    outputs: ["可编辑课件与讲授提示", "迭代记录与素材清单"], tools: ["演示文稿工具", "课堂投影 / 显示设备", "复核清单"],
    review: ["示意数据明确标注", "不使用未经验证的效果提升指标", "保留可访问说明和修订记录"], resourceIds: ["slide-storyboard", "output-review", "ai-record"],
  },
  {
    topic: "office", title: "多模型办公、安全与成果路演",
    summary: "以校内实际可用服务辅助办公，展示课程成果并制定后续行动计划。",
    goals: ["按任务与数据边界选择获批工具", "建立正式内容发布前的人工复核流程"],
    tasks: ["练习摘要、纪要、表格说明和通知草稿", "核查人名、数字、时间、责任与政策原文", "展示成果包并填写 30 天行动计划"],
    outputs: ["办公提示模板与复核清单", "个人行动计划与课程成果包"], tools: ["学校现有多模型 / 智能体平台（待确认）", "脱敏样例", "本地模板"],
    review: ["敏感内容不输入未经批准的外部服务", "正式文件由责任人确认", "具体模型、接口与 L20 能力以校方确认或实测为准"], resourceIds: ["office-prompt", "output-review", "action-plan"],
  },
];

export const courses: Course[] = records.map((record, index) => ({
  ...record, id: String(index + 1).padStart(2, "0"), number: index + 1,
  week: Math.floor(index / 2) + 1, hours: 2, module: topics[record.topic].module,
}));
export const totalHours = courses.reduce((sum, course) => sum + course.hours, 0);
export const topicHours = (topic: TopicId) => courses.filter((c) => c.topic === topic).reduce((sum, c) => sum + c.hours, 0);
export const moduleHours = (module: ModuleId) => courses.filter((c) => c.module === module).reduce((sum, c) => sum + c.hours, 0);
export const getCourse = (id: string) => courses.find((course) => course.id === id);
