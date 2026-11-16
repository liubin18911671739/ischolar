import type { Metadata } from "next";
import { Header, Footer } from "@/components/site-shell";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "iScholar 科研与教学培训工作台", template: "%s · iScholar 科研与教学培训工作台" },
  description: "面向教师的 32 小时科研、教学与办公实践资源门户，提供课程日历、可编辑模板和浏览器本地学习记录。",
  icons: { icon: "/icon.svg" },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh-CN">
      <body><a className="skip-link" href="#main-content">跳至主要内容</a><Header /><main id="main-content">{children}</main><Footer /></body>
    </html>
  );
}
