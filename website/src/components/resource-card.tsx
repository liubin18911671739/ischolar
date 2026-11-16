"use client";

import { useState } from "react";
import { Check, Copy, Download, FileSpreadsheet, FileText } from "lucide-react";
import type { Resource } from "@/content/resources";
import { downloadText } from "@/lib/download";

export function ResourceCard({ resource }: { resource: Resource }) {
  const [message, setMessage] = useState("");
  async function copy() {
    try { await navigator.clipboard.writeText(resource.body); setMessage("已复制模板正文"); }
    catch { setMessage("复制不可用，请展开模板手动选择，或下载文件。"); }
  }
  return <article className="resource-card" id={`resource-${resource.id}`}>
    <div className="resource-top"><span className="resource-icon" aria-hidden="true">{resource.format === "csv" ? <FileSpreadsheet size={22} /> : <FileText size={22} />}</span><span className="file-type">{resource.format.toUpperCase()} · 空白模板</span></div>
    <h3>{resource.title}</h3><p>{resource.description}</p>
    <div className="tags">{resource.tags.map((tag) => <span key={tag}>{tag}</span>)}</div>
    <div className="button-row no-print"><button className="button small" onClick={copy}><Copy size={15} aria-hidden="true" />复制模板</button><button className="button small subtle" onClick={() => downloadText(`${resource.title}.${resource.format}`, (resource.format === "csv" ? "\uFEFF" : "") + resource.body, resource.format === "csv" ? "text/csv;charset=utf-8" : "text/markdown;charset=utf-8")}><Download size={15} aria-hidden="true" />下载 {resource.format.toUpperCase()}</button></div>
    <details className="template-preview"><summary>查看模板正文</summary><pre tabIndex={0}>{resource.body}</pre></details>
    <p className="feedback" aria-live="polite">{message && <><Check size={14} aria-hidden="true" />{message}</>}</p>
  </article>;
}
