"use client";

import Link from "next/link";
import { useMemo, useState } from "react";
import { ArrowUpRight, CalendarDays, ChevronDown, List, Search } from "lucide-react";
import { courses, modules, type Course, type ModuleId } from "@/content/courses";
import { courseDateLabel } from "@/content/site";
import { CompletionToggle, PrintButton } from "./learning-tools";
import { ModuleTag } from "./ui";

export function CourseCard({ course }: { course: Course }) {
  return <article className={`course-card ${course.module}`}>
    <div className="course-meta"><span className="course-number">{course.id}</span><ModuleTag module={course.module} /><span>{course.hours} 小时{courseDateLabel(course.id) ? ` · ${courseDateLabel(course.id)}` : ""}</span></div>
    <details className="course-details">
      <summary><h3>{course.title}</h3><ChevronDown size={18} aria-hidden="true" /></summary>
      <div className="detail-content"><p>{course.summary}</p>
        <h4>学习目标</h4><ul>{course.goals.map((goal) => <li key={goal}>{goal}</li>)}</ul>
        <h4>课堂任务</h4><ol>{course.tasks.map((task) => <li key={task}>{task}</li>)}</ol>
        <h4>课后成果</h4><p>{course.outputs.join("；")}。</p>
        <h4>工具候选</h4><p>{course.tools.join(" / ")}</p>
        <h4>人工复核点</h4><ul>{course.review.map((item) => <li key={item}>{item}</li>)}</ul>
      </div>
    </details>
    <p className="course-teaser">{course.summary}</p>
    <div className="course-footer no-print"><CompletionToggle id={course.id} compact /><Link href={`/courses/${course.id}`} className="text-link">查看详情与笔记<ArrowUpRight size={15} aria-hidden="true" /></Link></div>
  </article>;
}

export function CalendarExplorer() {
  const [module, setModule] = useState<ModuleId | "all">("all");
  const [query, setQuery] = useState("");
  const [view, setView] = useState<"weeks" | "list">("weeks");
  const filtered = useMemo(() => courses.filter((course) => (module === "all" || course.module === module) && `${course.id} ${course.title} ${course.summary} ${modules[course.module].label}`.toLowerCase().includes(query.trim().toLowerCase())), [module, query]);
  return <div className="calendar-explorer">
    <div className="explorer-toolbar no-print">
      <div className="filter-buttons" role="group" aria-label="课程模块筛选">{(["all", "research", "teaching", "office"] as const).map((value) => <button key={value} aria-pressed={module === value} onClick={() => setModule(value)}>{value === "all" ? "全部课程" : modules[value].label}<span>{value === "all" ? courses.length : courses.filter((course) => course.module === value).length}</span></button>)}</div>
      <div className="view-buttons" role="group" aria-label="日历视图"><button aria-label="周视图" aria-pressed={view === "weeks"} onClick={() => setView("weeks")}><CalendarDays size={17} aria-hidden="true" />周视图</button><button aria-label="列表视图" aria-pressed={view === "list"} onClick={() => setView("list")}><List size={17} aria-hidden="true" />列表</button></div>
    </div>
    <div className="search-row no-print"><label className="search-field"><Search size={18} aria-hidden="true" /><span className="sr-only">搜索课程</span><input type="search" placeholder="搜索课程名称、编号或模块" value={query} onChange={(event) => setQuery(event.target.value)} /></label><PrintButton label="打印当前日历" /></div>
    <p className="result-count" aria-live="polite">共 {filtered.length} 次课 · {filtered.reduce((sum, course) => sum + course.hours, 0)} 小时{module !== "all" && ` · ${modules[module].label}`}{query.trim() && ` · 搜索“${query.trim()}”`}</p>
    {filtered.length === 0 ? <div className="empty-state"><Search size={30} aria-hidden="true" /><h2>没有找到符合条件的课程</h2><p>尝试使用“文献”“数字人”或“办公”等关键词。</p><button className="button" onClick={() => { setQuery(""); setModule("all"); }}>清空筛选</button></div> : view === "list" ? <div className="calendar-list">{filtered.map((course) => <div className="calendar-list-item" key={course.id}><span className="list-week">第 {course.week} 周</span><CourseCard course={course} /></div>)}</div> : <div className="calendar-weeks">{Array.from({ length: 8 }, (_, i) => i + 1).map((week) => {
      const weekCourses = filtered.filter((course) => course.week === week);
      return weekCourses.length > 0 && <section className="week-section" aria-labelledby={`week-${week}`} key={week}><div className="week-heading"><h2 id={`week-${week}`}><span>W{String(week).padStart(2, "0")}</span>第 {week} 周</h2><p>{weekCourses.length} 次课 · {weekCourses.reduce((sum, course) => sum + course.hours, 0)} 小时</p></div><div className="week-courses">{weekCourses.map((course) => <CourseCard key={course.id} course={course} />)}</div></section>;
    })}</div>}
  </div>;
}
