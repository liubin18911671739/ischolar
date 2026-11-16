import type { Metadata } from "next";
import { CalendarExplorer } from "@/components/calendar";
import { LearningProgress } from "@/components/learning-tools";
import { ModelReminder, PageIntro } from "@/components/ui";
import { courses, moduleHours } from "@/content/courses";

export const metadata: Metadata = { title: "课程日历" };
export default function CalendarPage() {
  const range = (module: "research" | "teaching" | "office") => { const selected = courses.filter((course) => course.module === module); return selected.length === 1 ? selected[0].id : `${selected[0].id}–${selected.at(-1)!.id}`; };
  return <div className="wrap page-content"><PageIntro eyebrow="CALENDAR / 8 周课程日历" title="每周两次，把实践逐步推进。"><p>{courses.length} 次课，每次 2 小时。按科研、教学与办公的顺序，逐步形成自己的研究流程与教学作品。未配置日期时仅显示周次。</p></PageIntro><div className="calendar-intro"><p><strong>{range("research")} 科研 {moduleHours("research")}h</strong><span>{range("teaching")} 教学 {moduleHours("teaching")}h</span><span>{range("office")} 办公综合 {moduleHours("office")}h</span></p><LearningProgress compact /></div><CalendarExplorer /><ModelReminder /></div>;
}
