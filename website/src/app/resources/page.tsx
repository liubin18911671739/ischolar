import type { Metadata } from "next";
import { PageIntro } from "@/components/ui";
import { ResourceExplorer } from "@/components/resource-explorer";
import { LocalRecords } from "@/components/learning-tools";
import { SourceRegistry } from "@/components/source-registry";

export const metadata: Metadata = { title: "资源中心" };
export default function ResourcesPage() {
  return <div className="wrap page-content"><PageIntro eyebrow="RESOURCES / 资源中心" title="一份模板，一次可复用的开始。"><p>按课程选择空白模板，复制或下载后继续编辑。CSV 适合表格工具，Markdown 适合 Obsidian 或文本编辑器；示例字段不代表已经完成研究或审批。</p></PageIntro><div className="anchor-links no-print"><a href="#templates">模板下载</a><a href="#source-registry">来源与许可登记</a><a href="#local-records">本地记录与导出</a></div><section id="templates" className="section-block compact-section" aria-labelledby="templates-heading"><h2 id="templates-heading" className="sr-only">模板库</h2><ResourceExplorer /></section><SourceRegistry /><LocalRecords /></div>;
}
