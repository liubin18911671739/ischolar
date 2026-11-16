import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, ArrowRight, CheckCircle2, Clock3, FileCheck2, ListChecks, Wrench } from "lucide-react";
import { courses, getCourse, topics } from "@/content/courses";
import { courseDateLabel } from "@/content/site";
import { resources } from "@/content/resources";
import { CourseNotebook, PrintButton } from "@/components/learning-tools";
import { ModelReminder, ModuleTag } from "@/components/ui";
import { ResourceCard } from "@/components/resource-card";

export const dynamicParams = false;
export function generateStaticParams() { return courses.map((course) => ({ id: course.id })); }
export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const course = getCourse((await params).id);
  return { title: course ? `${course.id} ${course.title}` : "课程不存在" };
}
export default async function CoursePage({ params }: { params: Promise<{ id: string }> }) {
  const course = getCourse((await params).id);
  if (!course) notFound();
  const related = resources.filter((resource) => course.resourceIds.includes(resource.id));
  const previous = courses[course.number - 2]; const next = courses[course.number];
  return <div className="wrap page-content course-page"><div className="breadcrumb no-print"><Link href="/calendar"><ArrowLeft size={15} aria-hidden="true" />返回课程日历</Link><PrintButton label="打印本课详情" /></div>
    <div className="course-page-header"><div className="course-meta"><span className="course-number">{course.id}</span><ModuleTag module={course.module} /><span>第 {course.week} 周 · {course.hours} 小时{courseDateLabel(course.id) ? ` · ${courseDateLabel(course.id)}` : ""}</span></div><h1>{course.title}</h1><p>{course.summary}</p><Link href={topics[course.topic].href} className="text-link">专题说明：{topics[course.topic].label}<ArrowRight size={15} aria-hidden="true" /></Link></div>
    <div className="course-body-grid"><div><section className="course-section"><h2><CheckCircle2 size={21} aria-hidden="true" />学习目标</h2><ul>{course.goals.map((item) => <li key={item}>{item}</li>)}</ul></section><section className="course-section"><h2><ListChecks size={21} aria-hidden="true" />课堂任务</h2><ol className="numbered-tasks">{course.tasks.map((item, index) => <li key={item}><span>0{index + 1}</span><p>{item}</p></li>)}</ol></section><section className="course-section"><h2><FileCheck2 size={21} aria-hidden="true" />课后成果</h2><ul>{course.outputs.map((item) => <li key={item}>{item}</li>)}</ul></section></div><aside className="course-side" aria-label="课程工具与人工复核"><section><h2><Wrench size={19} aria-hidden="true" />工具候选</h2><ul>{course.tools.map((item) => <li key={item}>{item}</li>)}</ul><p className="fine-print">具体工具、模型、账号与权限以校方批准范围为准。</p></section><section><h2><FileCheck2 size={19} aria-hidden="true" />人工复核点</h2><ul>{course.review.map((item) => <li key={item}>{item}</li>)}</ul></section></aside></div>
    <section className="lesson-rhythm"><h2><Clock3 size={20} aria-hidden="true" />120 分钟课堂节奏 <small>设计建议</small></h2><div>{[{ name: "导入", minutes: 15 }, { name: "示范", minutes: 25 }, { name: "上机", minutes: 55 }, { name: "互评", minutes: 15 }, { name: "提交反思", minutes: 10 }].map((item) => <p key={item.name}><strong>{item.minutes}<small>min</small></strong><span>{item.name}</span></p>)}</div></section>
    <section className="section-block"><div className="section-heading"><div><p className="eyebrow">TOOLKIT / 本课工具箱</p><h2>从模板开始，留下自己的版本。</h2></div></div><div className="resource-grid">{related.map((resource) => <ResourceCard key={resource.id} resource={resource} />)}</div></section>
    <CourseNotebook id={course.id} /><ModelReminder /><nav className="course-pagination no-print" aria-label="相邻课程">{previous ? <Link href={`/courses/${previous.id}`}><ArrowLeft size={17} aria-hidden="true" /><span><small>上一课 · {previous.id}</small>{previous.title}</span></Link> : <span />}{next ? <Link href={`/courses/${next.id}`}><span><small>下一课 · {next.id}</small>{next.title}</span><ArrowRight size={17} aria-hidden="true" /></Link> : <Link href="/resources#local-records">导出学习记录<ArrowRight size={17} aria-hidden="true" /></Link>}</nav>
  </div>;
}
