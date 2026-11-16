import type { Metadata } from "next";
import { PageIntro } from "@/components/ui";
import { SearchExplorer } from "@/components/search-explorer";

export const metadata: Metadata = { title: "搜索课程与模板" };
export default function SearchPage() {
  return <div className="wrap page-content"><PageIntro eyebrow="SEARCH / 内容搜索" title="找到这一次任务需要的内容。"><p>搜索课程名称、模块和模板标签。搜索在当前页面本地进行，不向服务器发送搜索词。</p></PageIntro><SearchExplorer /></div>;
}
