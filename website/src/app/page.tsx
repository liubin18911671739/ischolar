import Link from "next/link";
import { ArrowDown, ArrowRight, ArrowUpRight, BookOpenText, Database, FileCheck2, Layers3, LockKeyhole, NotebookPen, Sparkles } from "lucide-react";
import { courses, modules, moduleHours, topicHours, topics, totalHours, type TopicId } from "@/content/courses";
import { platformInformation, siteConfig } from "@/content/site";
import { LearningProgress } from "@/components/learning-tools";
import { ModelReminder, StatusTag, TextLink } from "@/components/ui";

const topicIcons = { "research-agent": BookOpenText, corpus: Database, creation: Sparkles, slides: Layers3, office: FileCheck2 };

export default function Home() {
  return <>
    <section className="hero">
      <div className="wrap hero-grid">
        <div className="hero-copy"><p className="eyebrow"><span className="live-dot" />iScholar 科研工作台 · 教师 AI 实践课程</p><h1>把 AI 用在<br />研究与课堂的<span>具体环节。</span></h1><p className="hero-description">基于本地优先的 Obsidian + Hermes（OpenCode / DeepSeek Harness）与双击即用的 iScholar 本地应用（Streamlit + FastAPI），围绕中阿区域国别、旅游管理与生态语料，完成可带回岗位继续使用的工作流。</p>
          <div className="button-row"><Link className="button primary" href="/calendar">查看课程日历<ArrowRight size={18} aria-hidden="true" /></Link><Link className="button" href="/resources">浏览资源<ArrowUpRight size={17} aria-hidden="true" /></Link></div>
          <div className="hero-metrics"><div><strong>{totalHours}<small>小时</small></strong><span>完整实践课程</span></div><div><strong>{courses.length}<small>次课</small></strong><span>每次 2 小时</span></div><div><strong>08<small>周</small></strong><span>每周两次</span></div></div>
        </div>
        <div className="hero-diagram" aria-label="课程流程：研究问题到证据与方法，再到课堂作品与复核。所有环节留下来源和人工判断。">
          <div className="diagram-caption"><span>THE PRACTICE MAP</span><span>01 — 16</span></div>
          <div className="diagram-stage"><span className="diagram-index">01</span><div><span className="stage-category">RESEARCH / 科研</span><h2>从一个好问题开始</h2><p>选题 · 文献 · 方法 · 语料</p></div><BookOpenText size={28} aria-hidden="true" /></div>
          <div className="diagram-connector"><span>留下证据与决策</span><ArrowDown size={18} aria-hidden="true" /></div>
          <div className="diagram-stage teal"><span className="diagram-index">02</span><div><span className="stage-category">TEACHING / 教学</span><h2>让知识被看见</h2><p>脚本 · 数字人 · 视频 · 课件</p></div><Layers3 size={28} aria-hidden="true" /></div>
          <div className="diagram-connector"><span>带着作品继续实践</span><ArrowDown size={18} aria-hidden="true" /></div>
          <div className="diagram-end"><FileCheck2 size={22} aria-hidden="true" /><div><strong>复核、归档、再次使用</strong><p>来源可回溯 · 内容可编辑 · 教师作判断</p></div></div>
          <div className="diagram-footnote">设计建议 / 不代表校内平台已部署</div>
        </div>
      </div>
    </section>
    <div className="wrap">
      <div className="home-notice"><LockKeyhole size={18} aria-hidden="true" /><p>无需账号。进度与笔记仅保存在当前浏览器。<Link href="/about">了解数据边界</Link></p><span>{siteConfig.disclaimer}</span></div>
      <section className="section-block" aria-labelledby="path-title">
        <div className="section-heading"><div><p className="eyebrow">CURRICULUM / 课程路径</p><h2 id="path-title">五个专题，一条实践路径。</h2></div><TextLink href="/calendar">查看 8 周安排</TextLink></div>
        <div className="curriculum-layout"><div className="topic-rows">{(Object.keys(topics) as TopicId[]).map((id, index) => { const topic = topics[id]; const Icon = topicIcons[id]; return <Link className="topic-row" key={id} href={topic.href}><span className="row-number">0{index + 1}</span><Icon size={24} aria-hidden="true" /><div><h3>{topic.label}</h3><p>{{ "research-agent": "Obsidian + Hermes · 研究问题到投稿复盘", corpus: "中阿文本 · 来源治理与可复现分析", creation: "脚本、图像、数字人与教学视频", slides: "信息结构、视觉表达与课堂迭代", office: "校内模型辅助办公、复核与成果展示" }[id]}</p></div><span className="topic-hours">{topicHours(id)}<small>h</small></span><ArrowUpRight size={18} aria-hidden="true" /></Link>; })}</div>
          <aside className="learning-aside" aria-label="个人学习进度"><NotebookPen size={30} aria-hidden="true" /><h3>为自己的任务<br />留下一份成果。</h3><p>标记课程进度，写下研究线索，随时导出本地记录。</p><LearningProgress compact /><TextLink href="/resources#local-records">管理本地记录</TextLink></aside></div>
        <div className="hours-breakdown">{(Object.keys(modules) as (keyof typeof modules)[]).map((id) => <div key={id} className={id}><span />{modules[id].label}{id === "office" ? "综合" : ""}<strong>{moduleHours(id)} 小时</strong></div>)}<p>按日历课次计算，各页使用同一份课程数据。</p></div>
      </section>
      <section className="section-block outcome-section" aria-labelledby="outcome-title"><div className="section-heading"><div><p className="eyebrow">TAKE IT FURTHER / 学习成果</p><h2 id="outcome-title">让每次练习，成为下一步的起点。</h2></div></div><div className="outcome-grid">{[{ n: "01", title: "一份研究证据包", text: "问题卡、综述矩阵、方法设计与可复现记录。" }, { n: "02", title: "一组教学资产", text: "脚本、授权素材、教学视频和可编辑课件。" }, { n: "03", title: "一套工作模板", text: "提示词、来源登记、人工复核与行动计划。" }].map((item) => <div key={item.n}><span>{item.n}</span><h3>{item.title}</h3><p>{item.text}</p></div>)}</div><TextLink href="/resources">从一份空白模板开始</TextLink></section>
      <section className="section-block" aria-labelledby="boundary-title"><div className="section-heading"><div><p className="eyebrow">BEFORE YOU START / 使用边界</p><h2 id="boundary-title">先确认环境，再选择工具。</h2></div><TextLink href="/office">办公与模型说明</TextLink></div><div className="status-list">{platformInformation.slice(0, 3).map((item) => <div key={item.title}><StatusTag status={item.status} /><h3>{item.title}</h3><p>{item.description}</p></div>)}</div><ModelReminder /></section>
    </div>
  </>;
}
