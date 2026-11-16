"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
import { ArrowUpRight, Menu, Search, X } from "lucide-react";
import { navigation, siteConfig } from "@/content/site";

export function Header() {
  const pathname = usePathname();
  const [open, setOpen] = useState(false);
  return <header className="site-header no-print">
    <div className="header-main wrap">
      <Link href="/" className="brand" onClick={() => setOpen(false)} aria-label="AI / iScholar 科研与教学培训工作台 RESEARCH · TEACHING · PRACTICE 首页">
        <span className="brand-mark" aria-hidden="true">AI<span> / </span></span>
        <span><strong>iScholar 科研与教学培训工作台</strong><small aria-hidden="true">RESEARCH · TEACHING · PRACTICE</small></span>
      </Link>
      <div className="header-actions">
        <Link href="/search" className="search-link" aria-label="搜索课程与模板" aria-current={pathname === "/search" ? "page" : undefined}><Search size={18} aria-hidden="true" /><span>搜索课程与模板</span></Link>
        <button className="icon-button mobile-menu" onClick={() => setOpen(!open)} aria-expanded={open} aria-controls="main-navigation" aria-label={open ? "收起导航" : "展开导航"}>{open ? <X size={22} /> : <Menu size={22} />}</button>
      </div>
    </div>
    <nav id="main-navigation" className={`site-nav ${open ? "is-open" : ""}`} aria-label="主导航">
      <div className="wrap nav-items">{navigation.map((item) => <Link key={item.href} href={item.href} onClick={() => setOpen(false)} aria-current={pathname === item.href || (item.href === "/calendar" && pathname.startsWith("/courses/")) ? "page" : undefined}>{item.label}</Link>)}</div>
    </nav>
  </header>;
}

export function Footer() {
  return <footer className="site-footer">
    <div className="wrap footer-grid"><div><strong>iScholar 科研与教学培训工作台</strong><p>从一份证据、一张脚本、一项真实任务开始。</p><p className="fine-print">{siteConfig.disclaimer}</p></div>
      <div><Link href="/about">数据边界与使用说明 <ArrowUpRight size={14} aria-hidden="true" /></Link><Link href="/resources#local-records">本地记录与导出 <ArrowUpRight size={14} aria-hidden="true" /></Link><p className="fine-print">不调用模型 API · 不收集本地笔记 · 无需账号</p></div>
    </div>
  </footer>;
}
