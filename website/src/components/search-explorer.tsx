"use client";

import Link from "next/link";
import { useState } from "react";
import { ArrowUpRight, Search } from "lucide-react";
import { courses, modules, topics } from "@/content/courses";
import { resources } from "@/content/resources";
import { ModuleTag } from "./ui";

export function SearchExplorer() {
  const [query, setQuery] = useState("");
  const [scope, setScope] = useState<"all" | "courses" | "resources">("all");
  const q = query.trim().toLowerCase();
  const foundCourses = scope === "resources" ? [] : courses.filter((course) => `${course.id} ${course.title} ${modules[course.module].label} ${topics[course.topic].label}`.toLowerCase().includes(q));
  const foundResources = scope === "courses" ? [] : resources.filter((resource) => `${resource.title} ${resource.description} ${resource.tags.join(" ")}`.toLowerCase().includes(q));
  return <div className="search-explorer">
    <label className="search-field large"><Search size={22} aria-hidden="true" /><span className="sr-only">搜索全部课程与模板</span><input type="search" autoComplete="off" value={query} onChange={(event) => setQuery(event.target.value)} placeholder="试试“语料”“数字人”或“复核”" /></label>
    <div className="filter-buttons" role="group" aria-label="搜索范围">{(["all", "courses", "resources"] as const).map((value) => <button key={value} aria-pressed={scope === value} onClick={() => setScope(value)}>{{ all: "全部", courses: "课程", resources: "模板" }[value]}</button>)}</div>
    <p className="result-count" aria-live="polite">{foundCourses.length} 次课 · {foundResources.length} 份模板{q && ` · 搜索“${query.trim()}”`}</p>
    {!foundCourses.length && !foundResources.length && <div className="empty-state"><h2>没有找到相关内容</h2><p>尝试模块名或模板标签，也可以直接浏览课程日历。</p><button className="button" onClick={() => { setQuery(""); setScope("all"); }}>清空筛选</button></div>}
    {foundCourses.length > 0 && <section className="search-results" aria-labelledby="search-courses"><h2 id="search-courses">课程</h2>{foundCourses.map((course) => <Link className="search-result" href={`/courses/${course.id}`} key={course.id}><span className="course-number">{course.id}</span><div><h3>{course.title}</h3><p>{course.summary}</p></div><ModuleTag module={course.module} /><ArrowUpRight size={18} aria-hidden="true" /></Link>)}</section>}
    {foundResources.length > 0 && <section className="search-results" aria-labelledby="search-resources"><h2 id="search-resources">模板</h2>{foundResources.map((resource) => <Link className="search-result" href={`/resources#resource-${resource.id}`} key={resource.id}><span className="file-type">{resource.format.toUpperCase()}</span><div><h3>{resource.title}</h3><p>{resource.description}</p></div><span className="result-tags">{resource.tags.join(" / ")}</span><ArrowUpRight size={18} aria-hidden="true" /></Link>)}</section>}
  </div>;
}
