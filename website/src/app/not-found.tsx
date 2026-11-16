import Link from "next/link";
import { ArrowLeft } from "lucide-react";
export default function NotFound() {
  return <div className="wrap page-content not-found"><p className="eyebrow">404 / 页面不存在</p><h1>这条学习路径暂未收录。</h1><p>请从课程日历或资源中心继续浏览。</p><div className="button-row"><Link className="button primary" href="/calendar"><ArrowLeft size={17} aria-hidden="true" />查看课程日历</Link><Link className="button" href="/resources">浏览资源</Link></div></div>;
}
