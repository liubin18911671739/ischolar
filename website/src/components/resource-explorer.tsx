"use client";

import { useState } from "react";
import { Search } from "lucide-react";
import { courses, modules } from "@/content/courses";
import { resources } from "@/content/resources";
import { ResourceCard } from "./resource-card";

export function ResourceExplorer() {
  const [query, setQuery] = useState("");
  const [courseId, setCourseId] = useState("all");
  const [tag, setTag] = useState("all");
  const tags = [...new Set(resources.flatMap((resource) => resource.tags))];
  const filtered = resources.filter((resource) => {
    const related = courses.filter((course) => course.resourceIds.includes(resource.id));
    const text = `${resource.title} ${resource.description} ${resource.tags.join(" ")} ${related.map((course) => `${course.title} ${modules[course.module].label}`).join(" ")}`;
    return (courseId === "all" || related.some((course) => course.id === courseId)) && (tag === "all" || resource.tags.includes(tag)) && text.toLowerCase().includes(query.trim().toLowerCase());
  });
  return <div>
    <div className="resource-filters no-print">
      <label className="search-field"><Search size={18} aria-hidden="true" /><span className="sr-only">搜索模板</span><input type="search" value={query} onChange={(event) => setQuery(event.target.value)} placeholder="搜索模板、课程名称或标签" /></label>
      <label className="select-field"><span>关联课程</span><select value={courseId} onChange={(event) => setCourseId(event.target.value)}><option value="all">全部课程</option>{courses.map((course) => <option value={course.id} key={course.id}>{course.id} {course.title}</option>)}</select></label>
      <label className="select-field"><span>模板标签</span><select value={tag} onChange={(event) => setTag(event.target.value)}><option value="all">全部标签</option>{tags.map((item) => <option value={item} key={item}>{item}</option>)}</select></label>
    </div>
    <p className="result-count" aria-live="polite">找到 {filtered.length} 份空白模板 · 所有文件均可本地编辑</p>
    {filtered.length ? <div className="resource-grid">{filtered.map((resource) => <ResourceCard key={resource.id} resource={resource} />)}</div> : <div className="empty-state"><Search size={30} aria-hidden="true" /><h2>没有找到符合条件的模板</h2><button className="button" onClick={() => { setQuery(""); setCourseId("all"); setTag("all"); }}>清空筛选</button></div>}
  </div>;
}
