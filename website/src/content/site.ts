export type InformationStatus =
  | { kind: "proposal" | "pending" }
  | { kind: "tested" | "confirmed"; evidence: string; date: string; responsible: string };

export const statusLabels: Record<InformationStatus["kind"], string> = {
  proposal: "设计建议", pending: "待校方确认", tested: "已实测", confirmed: "校方已确认",
};

export interface PlatformInformation {
  title: string;
  description: string;
  status: InformationStatus;
}

export const siteConfig = {
  title: "iScholar · 科研与教学培训工作台",
  description: "面向高校教师的科研智能体（Obsidian + Hermes / OpenCode / DeepSeek Harness）、语料库与教学创作资源门户",
  contact: { email: "", label: "待管理员配置" },
  // 可填写 "01": "2026-11-03" 等 ISO 日期。留空时仅显示周次，不推算开课日期。
  courseDates: {} as Partial<Record<string, string>>,
  disclaimer: "本网站为 iScholar 课程资源方案与学习工作台，配套本地双击即用版 iScholar (Streamlit + FastAPI) 与百度网盘国产/开源工具包。",
  modelReminder: "模型生成结果可能出错；论文来源、数据、法规、统计和教学事实须回到知网（CNKI）或原始来源核验。",
};

export const platformInformation: PlatformInformation[] = [
  { title: "iScholar 本地工作台（Streamlit + FastAPI）", description: "支持用户自行填入 DeepSeek / 通义千问 / Kimi 秘钥或连接本地 Ollama，双击启动无需手动配环境。", status: { kind: "tested", evidence: "本地 7 大科研智能体与 Obsidian 导出全链路验证通过", date: "2026-11-15", responsible: "iScholar 课程组" } },
  { title: "Obsidian + Hermes（OpenCode / DeepSeek Harness）", description: "以本地 Markdown 知识库替代云端 Notion，配合 Hermes Agent（支持 OpenCode 与 DeepSeek Harness）按阶段编排科研工作流；随包提供 6 个科研 Skills 与 14 部实操视频。", status: { kind: "tested", evidence: "6 个 Hermes Skills 与 14 部实操视频已随包交付，10 课核心讲义完成 Obsidian + Hermes 口径重构", date: "2026-11-15", responsible: "iScholar 课程组" } },
  { title: "共享 L20 算力与校内多模型平台", description: "L20 为已知资源约束；具体显存、驱动、并发、模型组合、配额和运维责任人仍需校方确认或实测。", status: { kind: "pending" } },
  { title: "国产与开源软件工具箱（百度网盘同步）", description: "精选 Obsidian、Zotero 7、Unpaywall、CORE、Ollama、jamovi、JASP、PSPP、AntConc、Taguette、Paperpal、PaperPass、讯飞智文等国产与开源工具，配套 14 部操作视频，已归档至百度网盘。", status: { kind: "tested", evidence: "百度网盘 /apps/bypy/iScholar课程 目录核验通过", date: "2026-11-15", responsible: "iScholar 课程组" } },
];

export const navigation = [
  { href: "/", label: "工作台" },
  { href: "/calendar", label: "课程日历" },
  { href: "/research", label: "科研智能体" },
  { href: "/corpus", label: "生态语料库" },
  { href: "/creation", label: "教学创作" },
  { href: "/slides", label: "图像化 PPT" },
  { href: "/office", label: "办公与模型" },
  { href: "/resources", label: "资源中心" },
  { href: "/about", label: "关于与安全" },
];

export function courseDateLabel(id: string) {
  const date = siteConfig.courseDates[id];
  return date ? date.replaceAll("-", "/") : undefined;
}
