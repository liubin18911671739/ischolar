"use client";

import { useRef, useState } from "react";
import { Check, Download, HardDrive, Printer, Trash2, Upload } from "lucide-react";
import { courses, totalHours } from "@/content/courses";
import {
  clearLearning,
  exportLearning,
  importLearning,
  previewImportLearning,
  saveNote,
  toggleComplete,
  useLearning,
  type ImportSummary,
} from "@/lib/learning-store";

export function CompletionToggle({ id, compact = false }: { id: string; compact?: boolean }) {
  const { data, ready, status } = useLearning();
  const completed = data.completed.includes(id);
  return <label className={`completion ${completed ? "checked" : ""} ${compact ? "compact" : ""}`}>
    <input type="checkbox" checked={completed} disabled={!ready || status === "invalid"} onChange={() => toggleComplete(id)} />
    <span>{completed ? "已完成" : "标记完成"}</span>
  </label>;
}

export function CourseNotebook({ id }: { id: string }) {
  const { data, ready, status } = useLearning();
  return <section className="notebook no-print" aria-labelledby="notebook-title">
    <div className="section-heading"><div><p className="eyebrow">MY NOTES / 我的课堂</p><h2 id="notebook-title">把下一步，留给自己。</h2></div><CompletionToggle id={id} /></div>
    <label className="field-label" htmlFor="course-note">本课笔记与待解决的问题</label>
    <textarea id="course-note" rows={6} maxLength={20000} value={data.notes[id] ?? ""} disabled={!ready || status === "invalid"} onChange={(event) => saveNote(id, event.target.value)} placeholder="记录自己的研究线索、课堂反馈与下一步行动。请勿填写敏感信息。" />
    <p className="fine-print" role="status">{!ready ? "正在读取本地记录…" : status === "available" ? "输入后自动保存在当前浏览器；不上传服务器。可在资源中心导出备份。" : status === "invalid" ? "本地记录格式无法识别，已停止覆盖。请在资源中心导出备份或清除后重新记录。" : "浏览器存储不可用，修改仅在当前页面会话中保留。请及时导出备份。"}</p>
    <div className="button-row note-export"><button className="button small" disabled={!ready} onClick={exportLearning}><Download size={15} aria-hidden="true" />导出当前记录</button></div>
  </section>;
}

export function LearningProgress({ compact = false }: { compact?: boolean }) {
  const { data, ready, status } = useLearning();
  const count = ready ? data.completed.length : 0;
  const hours = courses.filter((course) => data.completed.includes(course.id)).reduce((sum, course) => sum + course.hours, 0);
  return <div className={`learning-progress ${compact ? "small" : ""}`}>
    <div className="progress-heading"><span><HardDrive size={16} aria-hidden="true" />我的学习进度</span><strong>{count}<span> / {courses.length} 次课</span></strong></div>
    <progress value={count} max={courses.length} aria-label="已完成课程" />
    <p>{status === "invalid" ? "本地数据无法识别，请先导出备份。" : status === "unavailable" ? "本地存储不可用，请导出备份。" : `${ready ? hours : 0} / ${totalHours} 小时 · 仅保存在当前浏览器`}</p>
  </div>;
}

export function LocalRecords() {
  const { ready, status, data } = useLearning();
  const [confirming, setConfirming] = useState(false);
  const [message, setMessage] = useState("");
  const [pendingImport, setPendingImport] = useState<{ raw: string; summary: ImportSummary } | null>(null);
  const [importError, setImportError] = useState("");
  const fileInput = useRef<HTMLInputElement>(null);

  const handleFile = async (file: File) => {
    setImportError("");
    setMessage("");
    setPendingImport(null);
    const raw = await file.text();
    const result = previewImportLearning(raw);
    if (!result.ok) {
      setImportError(`无法导入：${result.error} 现有记录未被修改。`);
      return;
    }
    setPendingImport({ raw, summary: result.summary });
  };

  const confirmImport = () => {
    if (!pendingImport) return;
    const result = importLearning(pendingImport.raw);
    if (!result.ok) {
      setPendingImport(null);
      setImportError(`导入失败：${result.error ?? "未知错误"}`);
      return;
    }
    setPendingImport(null);
    setMessage(result.backedUp ? "已恢复本地记录；导入前的原记录已保存在浏览器备份中。" : "已恢复本地记录。");
  };

  return <section id="local-records" className="local-records no-print" aria-labelledby="records-title">
    <div className="section-heading"><div><p className="eyebrow">LOCAL ONLY / 本地记录</p><h2 id="records-title">你的记录，保留在你的浏览器。</h2></div><HardDrive size={28} aria-hidden="true" /></div>
    <p>进度、逐课笔记和来源许可登记不会上传服务器。更换浏览器、清理浏览器数据或使用隐私模式可能导致记录不可用，请主动导出备份；换设备时可导入此前导出的 JSON 恢复。</p>
    <LearningProgress />
    <p className="fine-print">{Object.values(data.notes).filter(Boolean).length} 篇课程笔记 · {data.sources.length} 条来源记录</p>
    {status === "invalid" && <p className="error-text" role="alert">检测到无法识别的本地记录，已停止覆盖。导出会包含原始存储备份，请备份后再清除。</p>}
    {status === "unavailable" && <p className="error-text" role="alert">当前浏览器无法持久保存数据。当前会话仍可使用，请及时导出。</p>}
    <div className="button-row">
      <button className="button primary" disabled={!ready} onClick={exportLearning}><Download size={17} aria-hidden="true" />导出本地 JSON</button>
      <button className="button subtle" disabled={!ready} onClick={() => fileInput.current?.click()}><Upload size={16} aria-hidden="true" />导入本地 JSON</button>
      <button className="button subtle danger" disabled={!ready} onClick={() => setConfirming(true)}><Trash2 size={16} aria-hidden="true" />清除本地数据</button>
    </div>
    <input ref={fileInput} type="file" accept=".json,application/json" aria-label="选择本地记录 JSON 文件" style={{ display: "none" }}
      onChange={(event) => { const file = event.target.files?.[0]; if (file) void handleFile(file); event.target.value = ""; }} />
    {importError && <p className="error-text" role="alert">{importError}</p>}
    {pendingImport && <div className="confirm-box" role="group" aria-label="确认导入本地记录">
      <p>即将恢复以下记录：<strong>{pendingImport.summary.completed} 次课已完成</strong>、<strong>{pendingImport.summary.notes} 篇笔记</strong>、<strong>{pendingImport.summary.sources} 条来源记录</strong>。</p>
      <p className="fine-print">导出时间：{pendingImport.summary.exportedAt ? new Date(pendingImport.summary.exportedAt).toLocaleString("zh-CN") : "未记录"}。确认后将覆盖当前浏览器中的进度、笔记与来源登记，导入前的原记录会先保存在浏览器备份中。</p>
      <div className="button-row"><button className="button primary" onClick={confirmImport}>确认覆盖恢复</button><button className="button" onClick={() => setPendingImport(null)}>取消导入</button></div>
    </div>}
    {confirming && <div className="confirm-box" role="group" aria-label="确认清除本地记录"><p>将清除本网站在当前浏览器保存的全部进度、笔记与来源记录。建议先导出备份。</p><div className="button-row"><button className="button danger" onClick={() => { const ok = clearLearning(); setConfirming(false); setMessage(ok ? "本网站的本地记录已清除。" : "清除失败：浏览器拒绝存储访问，原有记录尚未确认删除。"); }}>确认清除</button><button className="button" onClick={() => setConfirming(false)}>取消</button></div></div>}
    <p className="feedback" aria-live="polite">{message && <><Check size={15} aria-hidden="true" />{message}</>}</p>
  </section>;
}

export function PrintButton({ label = "打印" }: { label?: string }) { return <button className="button subtle no-print" onClick={() => window.print()}><Printer size={16} aria-hidden="true" />{label}</button>; }
