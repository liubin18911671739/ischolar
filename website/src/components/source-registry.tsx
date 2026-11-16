"use client";

import { useState } from "react";
import { Check, Link2, Trash2 } from "lucide-react";
import { deleteSource, saveSource, useLearning, type SourceEntry } from "@/lib/learning-store";

export function SourceRegistry() {
  const { data, ready, status } = useLearning();
  const [message, setMessage] = useState("");
  const [removing, setRemoving] = useState<string | null>(null);
  function submit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const form = event.currentTarget;
    const values = new FormData(form);
    const text = (key: string) => String(values.get(key) ?? "").trim();
    if (!text("title")) { setMessage("来源名称不能只包含空格。"); return; }
    const url = text("url");
    try { if (!["http:", "https:"].includes(new URL(url).protocol)) throw new Error(); }
    catch { setMessage("请填写以 http:// 或 https:// 开头的来源链接。"); return; }
    const license = text("license") as SourceEntry["license"];
    if (license !== "unknown" && (!text("evidence") || !text("usage"))) { setMessage("填写授权或限制状态时，请同时填写许可依据和允许用途。"); return; }
    if (text("reviewer") && !text("reviewedDate")) { setMessage("填写复核人后，请补充复核日期。"); return; }
    const entry: SourceEntry = {
      id: crypto.randomUUID(), title: text("title"), url, type: text("type"), acquiredDate: text("acquiredDate"), license,
      evidence: text("evidence"), usage: text("usage"), labelNote: text("labelNote"), reviewer: text("reviewer"), reviewedDate: text("reviewedDate"),
    };
    saveSource(entry);
    form.reset();
    setMessage("来源记录已加入本地列表。请在下方检查保存状态，并及时导出备份。");
  }
  return <section id="source-registry" className="source-registry no-print" aria-labelledby="sources-title">
    <div className="section-heading"><div><p className="eyebrow">SOURCE & LICENSE / 来源与许可</p><h2 id="sources-title">让素材的使用范围有据可查。</h2></div><Link2 size={26} aria-hidden="true" /></div>
    <p>分别登记语料、图片、字体、音乐、人像和声音。这里的记录由你填写，仅保存在当前浏览器，不代表学校已审核或批准。</p>
    <details className="registration-form" open={data.sources.length === 0}>
      <summary>新增来源与许可记录</summary>
      <form onSubmit={submit}>
        <fieldset disabled={!ready || status === "invalid"}>
          <legend className="sr-only">来源登记字段</legend>
          <div className="form-grid">
            <label>来源名称 <span>必填</span><input name="title" required maxLength={200} /></label>
            <label>来源链接 <span>必填</span><input name="url" type="url" required placeholder="https://" maxLength={2000} /></label>
            <label>素材类型<select name="type"><option>语料 / 文献</option><option>图片</option><option>视频</option><option>字体</option><option>音乐 / 声音</option><option>数字人 / 肖像</option><option>其他</option></select></label>
            <label>取得日期<input name="acquiredDate" type="date" /></label>
            <label>许可状态<select name="license"><option value="unknown">待核查</option><option value="permitted">有授权依据</option><option value="restricted">有限制</option></select></label>
            <label>许可依据<input name="evidence" maxLength={2000} placeholder="许可条款、授权文件位置或说明" /></label>
            <label className="wide">允许用途与限制<textarea name="usage" rows={2} maxLength={4000} placeholder="教学展示 / 再发布 / 训练许可等，请分别核对；未知项写待核查。" /></label>
            <label className="wide">生成合成内容标识说明<textarea name="labelNote" rows={2} maxLength={2000} placeholder="适用时填写显式标识位置和隐式标识复核情况。" /></label>
            <label>人工复核人<input name="reviewer" maxLength={100} /></label>
            <label>复核日期<input name="reviewedDate" type="date" /></label>
          </div>
          <button className="button primary" type="submit"><Check size={16} aria-hidden="true" />保存到本地</button>
        </fieldset>
      </form>
    </details>
    <p className="feedback" aria-live="polite">{message}</p>
    <p className={`fine-print ${status !== "available" ? "error-text" : ""}`} role="status">{!ready ? "正在读取本地记录…" : status === "available" ? "本地存储可用。来源记录与课程笔记可一并导出 JSON。" : status === "invalid" ? "无法识别已有本地数据，已暂停保存。请先导出备份或清除记录。" : "本地存储不可用，新记录仅在当前会话保留。请立即导出备份。"}</p>
    <div className="source-list">{data.sources.length === 0 ? <p className="fine-print">尚无登记记录。空白模板也可从上方下载后本地填写。</p> : data.sources.map((source) => <article className="source-entry" key={source.id}>
      <div className="source-entry-head"><h3>{source.title}</h3><span className="status-tag">{{ unknown: "待核查", permitted: "有授权依据", restricted: "有限制" }[source.license]}</span></div>
      <p className="source-url">{source.url}</p><dl className="source-fields"><div><dt>素材类型</dt><dd>{source.type}</dd></div><div><dt>取得日期</dt><dd>{source.acquiredDate || "未填写"}</dd></div><div><dt>许可依据</dt><dd>{source.evidence || "待核查"}</dd></div><div><dt>允许用途与限制</dt><dd>{source.usage || "待核查"}</dd></div><div><dt>标识说明</dt><dd>{source.labelNote || "未填写"}</dd></div><div><dt>人工复核</dt><dd>{source.reviewer ? `${source.reviewer} / ${source.reviewedDate || "日期待补充"}` : "待复核"}</dd></div></dl>
      {removing === source.id ? <div className="button-row"><span>删除这条本地记录？</span><button className="button small danger" onClick={() => { deleteSource(source.id); setRemoving(null); }}>确认删除</button><button className="button small" onClick={() => setRemoving(null)}>取消</button></div> : <button className="button small subtle danger" disabled={status === "invalid"} onClick={() => setRemoving(source.id)}><Trash2 size={14} aria-hidden="true" />删除记录</button>}
    </article>)}</div>
  </section>;
}
