"use client";

import { useSyncExternalStore } from "react";
import { courses } from "@/content/courses";
import { downloadText } from "./download";

export const STORAGE_KEY = "ischolar-workbench:v1";
export const BACKUP_KEY = `${STORAGE_KEY}:backup`;
export interface SourceEntry {
  id: string;
  title: string;
  url: string;
  type: string;
  acquiredDate: string;
  license: "unknown" | "permitted" | "restricted";
  evidence: string;
  usage: string;
  labelNote: string;
  reviewer: string;
  reviewedDate: string;
}
export interface LearningData {
  version: 1;
  completed: string[];
  notes: Record<string, string>;
  sources: SourceEntry[];
  updatedAt: string | null;
}
interface Snapshot {
  data: LearningData;
  ready: boolean;
  status: "available" | "unavailable" | "invalid";
}
const emptyData: LearningData = { version: 1, completed: [], notes: {}, sources: [], updatedAt: null };
const serverSnapshot: Snapshot = { data: emptyData, ready: false, status: "available" };
let snapshot = serverSnapshot;
let initialized = false;
let rawBackup: string | null = null;
const listeners = new Set<() => void>();
const ids = new Set(courses.map((course) => course.id));

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}
function validSource(value: unknown): value is SourceEntry {
  if (!isRecord(value)) return false;
  return ["id", "title", "url", "type", "acquiredDate", "evidence", "usage", "labelNote", "reviewer", "reviewedDate"].every((key) => typeof value[key] === "string")
    && ["unknown", "permitted", "restricted"].includes(String(value.license));
}
function parseData(raw: string): LearningData {
  const value: unknown = JSON.parse(raw);
  if (!isRecord(value) || value.version !== 1 || !Array.isArray(value.completed)
    || !value.completed.every((id) => typeof id === "string" && ids.has(id))
    || !isRecord(value.notes) || !Object.entries(value.notes).every(([id, text]) => ids.has(id) && typeof text === "string")
    || !Array.isArray(value.sources) || !value.sources.every(validSource)
    || !(value.updatedAt === null || typeof value.updatedAt === "string")) throw new Error("Invalid learning data");
  return value as unknown as LearningData;
}
function readStorage() {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    rawBackup = raw;
    snapshot = { data: raw ? parseData(raw) : emptyData, ready: true, status: "available" };
  } catch (error) {
    snapshot = { data: snapshot.data, ready: true, status: error instanceof SyntaxError || rawBackup ? "invalid" : "unavailable" };
  }
}
function emit() { for (const listener of listeners) listener(); }
function subscribe(callback: () => void) {
  listeners.add(callback);
  const onStorage = (event: StorageEvent) => {
    if (event.key === STORAGE_KEY || event.key === null) { rawBackup = null; readStorage(); emit(); }
  };
  window.addEventListener("storage", onStorage);
  return () => { listeners.delete(callback); window.removeEventListener("storage", onStorage); };
}
function getSnapshot() {
  if (typeof window !== "undefined" && !initialized) { readStorage(); initialized = true; }
  return snapshot;
}
function update(change: (data: LearningData) => LearningData) {
  getSnapshot();
  if (snapshot.status === "invalid") return;
  const data: LearningData = { ...change(snapshot.data), version: 1, updatedAt: new Date().toISOString() };
  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    snapshot = { data, ready: true, status: "available" };
  } catch {
    snapshot = { data, ready: true, status: "unavailable" };
  }
  emit();
}

export function useLearning() {
  return useSyncExternalStore(subscribe, getSnapshot, () => serverSnapshot);
}
export function toggleComplete(id: string) {
  if (!ids.has(id)) return;
  update((data) => ({ ...data, completed: data.completed.includes(id) ? data.completed.filter((item) => item !== id) : [...data.completed, id] }));
}
export function saveNote(id: string, text: string) {
  if (ids.has(id)) update((data) => ({ ...data, notes: { ...data.notes, [id]: text } }));
}
export function saveSource(source: SourceEntry) {
  update((data) => ({ ...data, sources: [source, ...data.sources] }));
}
export function deleteSource(id: string) {
  update((data) => ({ ...data, sources: data.sources.filter((source) => source.id !== id) }));
}
export function clearLearning() {
  try {
    window.localStorage.removeItem(STORAGE_KEY);
    rawBackup = null;
    snapshot = { data: emptyData, ready: true, status: "available" };
  } catch {
    snapshot = { ...snapshot, status: "unavailable" };
    emit();
    return false;
  }
  emit();
  return true;
}
export function exportLearning() {
  getSnapshot();
  const exportData = { ...snapshot.data, exportedAt: new Date().toISOString(), ...(snapshot.status === "invalid" ? { unreadableStorageBackup: rawBackup } : {}) };
  downloadText(`ischolar-本地记录-${new Date().toISOString().slice(0, 10)}.json`, JSON.stringify(exportData, null, 2), "application/json;charset=utf-8");
}

export interface ImportSummary {
  completed: number;
  notes: number;
  sources: number;
  exportedAt: string | null;
  updatedAt: string | null;
}

type ImportValidation =
  | { ok: true; data: LearningData; summary: ImportSummary }
  | { ok: false; error: string };

function validateImport(raw: string): ImportValidation {
  let value: unknown;
  try {
    value = JSON.parse(raw);
  } catch {
    return { ok: false, error: "文件不是有效的 JSON，无法解析。" };
  }
  if (!isRecord(value)) return { ok: false, error: "文件内容必须是一个 JSON 对象。" };
  if (value.version !== 1) {
    return { ok: false, error: `不支持的记录版本：${String(value.version ?? "缺失")}。当前仅支持 version 1。` };
  }
  if (!Array.isArray(value.completed)) return { ok: false, error: "缺少 completed 字段或格式不正确。" };
  const invalidCompleted = value.completed.filter((id) => typeof id !== "string" || !ids.has(id));
  if (invalidCompleted.length) {
    return { ok: false, error: `completed 中包含无法识别的课程 ID：${invalidCompleted.slice(0, 3).join("、")}。` };
  }
  if (!isRecord(value.notes)) return { ok: false, error: "缺少 notes 字段或格式不正确。" };
  const invalidNotes = Object.entries(value.notes).filter(([id, text]) => !ids.has(id) || typeof text !== "string");
  if (invalidNotes.length) {
    return { ok: false, error: `notes 中包含无法识别的课程 ID 或非文本内容：${invalidNotes.slice(0, 3).map(([id]) => id).join("、")}。` };
  }
  if (!Array.isArray(value.sources) || !value.sources.every(validSource)) {
    return { ok: false, error: "sources 字段格式不正确，可能来自其他版本或已损坏。" };
  }
  if (!(value.updatedAt === null || typeof value.updatedAt === "string")) {
    return { ok: false, error: "updatedAt 字段格式不正确。" };
  }
  const data: LearningData = {
    version: 1,
    completed: value.completed as string[],
    notes: value.notes as Record<string, string>,
    sources: value.sources as SourceEntry[],
    updatedAt: value.updatedAt as string | null,
  };
  return {
    ok: true,
    data,
    summary: {
      completed: data.completed.length,
      notes: Object.values(data.notes).filter(Boolean).length,
      sources: data.sources.length,
      exportedAt: typeof value.exportedAt === "string" ? value.exportedAt : null,
      updatedAt: data.updatedAt,
    },
  };
}

export function previewImportLearning(raw: string): ImportValidation {
  return validateImport(raw);
}

export function importLearning(raw: string): { ok: boolean; error?: string; backedUp?: boolean } {
  const result = validateImport(raw);
  if (!result.ok) return { ok: false, error: result.error };
  getSnapshot();
  let backedUp = false;
  try {
    if (typeof window !== "undefined") {
      const current = window.localStorage.getItem(STORAGE_KEY);
      if (current) {
        window.localStorage.setItem(BACKUP_KEY, current);
        backedUp = true;
      }
      const next: LearningData = { ...result.data, version: 1, updatedAt: new Date().toISOString() };
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
      rawBackup = null;
      snapshot = { data: next, ready: true, status: "available" };
      emit();
      return { ok: true, backedUp };
    }
  } catch {
    snapshot = { ...snapshot, status: "unavailable" };
    emit();
    return { ok: false, error: "浏览器拒绝访问本地存储，无法写入导入记录。" };
  }
  return { ok: false, error: "当前环境不支持导入。" };
}
