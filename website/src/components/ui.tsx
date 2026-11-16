import Link from "next/link";
import { ArrowRight, ArrowUpRight, Info } from "lucide-react";
import { modules, type ModuleId } from "@/content/courses";
import { siteConfig, statusLabels, type InformationStatus } from "@/content/site";

export function PageIntro({ eyebrow, title, children }: { eyebrow: string; title: string; children: React.ReactNode }) {
  return <div className="page-intro"><p className="eyebrow">{eyebrow}</p><h1>{title}</h1><div className="intro-copy">{children}</div></div>;
}
export function ModuleTag({ module }: { module: ModuleId }) { return <span className={`module-tag ${module}`}>{modules[module].label}</span>; }
export function StatusTag({ status }: { status: InformationStatus }) { return <span className={`status-tag status-${status.kind}`}>{statusLabels[status.kind]}</span>; }
export function ModelReminder() { return <aside className="reminder" aria-label="模型使用提示"><Info size={18} aria-hidden="true" /><p>{siteConfig.modelReminder}</p></aside>; }
export function TextLink({ href, children }: { href: string; children: React.ReactNode }) { return <Link className="text-link" href={href}>{children}<ArrowRight size={16} aria-hidden="true" /></Link>; }
export function ExternalLink({ href, children }: { href: string; children: React.ReactNode }) { return <a className="external-link" href={href} target="_blank" rel="noopener noreferrer">{children}<ArrowUpRight size={14} aria-hidden="true" /><span className="sr-only">（新窗口打开）</span></a>; }
