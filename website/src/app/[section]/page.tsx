import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { ArrowRight, ArrowUpRight, Check } from "lucide-react";
import Link from "next/link";
import { guides } from "@/content/guides";
import { courses, topicHours, type TopicId } from "@/content/courses";
import { platformInformation } from "@/content/site";
import { ExternalLink, ModelReminder, PageIntro, StatusTag, TextLink } from "@/components/ui";

const routes: Record<string, TopicId> = { research: "research-agent", corpus: "corpus", creation: "creation", slides: "slides", office: "office" };
export const dynamicParams = false;
export function generateStaticParams() { return Object.keys(routes).map((section) => ({ section })); }
export async function generateMetadata({ params }: { params: Promise<{ section: string }> }): Promise<Metadata> {
  const id = routes[(await params).section];
  return { title: id ? guides[id].eyebrow.split(" / ")[1] : "页面不存在" };
}
export default async function GuidePage({ params }: { params: Promise<{ section: string }> }) {
  const id = routes[(await params).section];
  if (!id) notFound();
  const guide = guides[id];
  const related = courses.filter((course) => course.topic === id);
  return <div className="wrap page-content guide-page"><PageIntro eyebrow={guide.eyebrow} title={guide.title}><p>{guide.intro}</p></PageIntro><div className="guide-band"><span>{topicHours(id)} 小时 · {related.length} 次课</span><p>{guide.outcome}</p><span className="status-tag status-proposal">设计建议</span></div>
    <section className="section-block" aria-labelledby="workflow-heading"><div className="section-heading"><div><p className="eyebrow">WORKFLOW / 实践流程</p><h2 id="workflow-heading">每一步，都有明确的输入与产出。</h2></div></div><ol className="workflow">{guide.steps.map((step, index) => <li key={step.title}><span className="workflow-index">0{index + 1}</span><h3>{step.title}</h3><p>{step.text}</p><div className="workflow-output"><Check size={14} aria-hidden="true" />{step.output}</div></li>)}</ol></section>
    <div className="guide-articles">{guide.sections.map((section, index) => <section key={section.title}><div className="article-number">0{index + 1}</div><div><h2>{section.title}</h2><p>{section.body}</p><ul>{section.points.map((point) => <li key={point}>{point}</li>)}</ul></div></section>)}</div>
    <section className="section-block examples"><div className="section-heading"><div><p className="eyebrow">EXERCISE / 案例演练</p><h2>把方法放进具体的学科问题。</h2></div></div><div className="example-grid">{guide.examples.map((example) => <article key={example.title}><span>演练示例 · 不预设结果</span><h3>{example.title}</h3><p>{example.text}</p></article>)}</div></section>
    {id === "office" && <section className="section-block"><div className="section-heading"><h2>平台与资源状态</h2></div><div className="platform-information">{platformInformation.map((info) => <article key={info.title}><StatusTag status={info.status} /><h3>{info.title}</h3><p>{info.description}</p>{(info.status.kind === "tested" || info.status.kind === "confirmed") && <p className="fine-print">依据：{info.status.evidence} · {info.status.date} · {info.status.responsible}</p>}</article>)}</div></section>}
    <section className="section-block"><div className="section-heading"><div><p className="eyebrow">RELATED LESSONS / 关联课程</p><h2>按课次继续实践。</h2></div><TextLink href="/resources">查看空白模板</TextLink></div><div className="related-lessons">{related.map((course) => <Link key={course.id} href={`/courses/${course.id}`}><span className="course-number">{course.id}</span><h3>{course.title}</h3><span>{course.hours}h</span><ArrowUpRight size={18} aria-hidden="true" /></Link>)}</div></section>
    <ModelReminder />{guide.references.length > 0 && <section className="reference-section"><h2>官方文档与参考入口</h2><p>供了解工具或规范使用；具体版本、许可证与适用范围仍需核对。</p><div>{guide.references.map((ref) => <ExternalLink key={ref.url} href={ref.url}>{ref.label}</ExternalLink>)}</div></section>}<div className="button-row no-print"><Link href="/calendar" className="button">回到课程日历<ArrowRight size={16} aria-hidden="true" /></Link></div>
  </div>;
}
