import type { Metadata } from "next";
import Link from "next/link";
import { ArrowUpRight, Check, HardDrive, ShieldCheck } from "lucide-react";
import { ExternalLink, ModelReminder, PageIntro, StatusTag } from "@/components/ui";
import { platformInformation, siteConfig, statusLabels, type InformationStatus } from "@/content/site";

export const metadata: Metadata = { title: "关于与安全" };
export default function AboutPage() {
  return <div className="wrap page-content about-page"><PageIntro eyebrow="ABOUT & SAFETY / 关于与安全" title="清楚的边界，让实践可以持续。"><p>{siteConfig.disclaimer} 本站提供静态课程与模板，不代理校内模型、不接收文件、不需要账号，也不包含学校内部资料。</p></PageIntro>
    <section className="privacy-intro"><HardDrive size={32} aria-hidden="true" /><div><h2>进度、笔记和登记，只在当前浏览器。</h2><p>这些记录通过浏览器 localStorage 保存，不发送到服务器。公开课程页可能由托管平台提供并产生日常访问日志，外部参考链接由对应网站提供服务；请勿在本地笔记中填写敏感内容。</p><Link className="text-link" href="/resources#local-records">导出备份或清除本地记录<ArrowUpRight size={16} aria-hidden="true" /></Link></div></section>
    <section className="section-block"><div className="section-heading"><h2>先分级，再决定如何使用资料。</h2></div><div className="data-levels">{[{ n: "01", title: "公开资料", text: "按来源许可使用，保留出处。公开可访问不意味着可以训练、商用或再分发。" }, { n: "02", title: "一般校内资料", text: "只在学校批准的服务和范围内使用，先确认数据保留、权限与脱敏要求。" }, { n: "03", title: "敏感与受限资料", text: "个人信息、未公开受限研究材料及涉密数据按学校制度处理，不输入未经批准的外部模型。" }].map((level) => <article key={level.n}><span>{level.n}</span><h3>{level.title}</h3><p>{level.text}</p></article>)}</div></section>
    <section className="section-block"><div className="section-heading"><h2>区分建议、实测和批准。</h2></div><div className="status-explainer">{(Object.keys(statusLabels) as InformationStatus["kind"][]).map((kind) => <div key={kind}><span className={`status-tag status-${kind}`}>{statusLabels[kind]}</span><p>{{ proposal: "课程设计与候选工具安排，不等于已完成部署或批准。", pending: "尚无充分确认依据，不能写成既成事实。", tested: "必须有测试任务、记录、日期及责任方，且不能超出测试范围。", confirmed: "必须保留确认依据、日期和责任方，不自动适用于其他用途。" }[kind]}</p></div>)}</div><div className="platform-information">{platformInformation.map((info) => <article key={info.title}><StatusTag status={info.status} /><h3>{info.title}</h3><p>{info.description}</p></article>)}</div></section>
    <section className="section-block ethics"><ShieldCheck size={30} aria-hidden="true" /><h2>研究诚信与生成内容复核</h2><ul>{["论文来源、DOI、页码、数据与引文逐条回到原始来源。", "保留模型、提示词、输入材料和人工修改；按学校与期刊要求说明 AI 辅助。", "肖像、声音、图片、字体、音乐和语料分别核对权利与使用范围。", "面向传播的生成合成内容，按适用规范处理显式与隐式标识。", "模型输出作为候选与草稿；研究、教学评价和正式办公发布由责任人决定。"].map((item) => <li key={item}><Check size={18} aria-hidden="true" /><span>{item}</span></li>)}</ul><ModelReminder /></section>
    <section className="reference-section"><h2>规范与反馈入口</h2><div><ExternalLink href="https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm">生成式人工智能服务管理暂行办法</ExternalLink><ExternalLink href="https://www.nrta.gov.cn/art/2025/3/14/art_113_70340.html">人工智能生成合成内容标识办法</ExternalLink></div><p>规范的具体适用范围和学校执行流程由责任部门确认。</p><h3>联系与反馈</h3>{siteConfig.contact.email ? <a className="text-link" href={`mailto:${siteConfig.contact.email}`}>{siteConfig.contact.email}</a> : <p className="contact-placeholder">{siteConfig.contact.label}。当前未提供在线反馈提交服务。</p>}</section>
  </div>;
}
