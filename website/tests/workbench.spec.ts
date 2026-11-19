import { expect, test } from "@playwright/test";
import { readFile } from "node:fs/promises";

const key = "ischolar-workbench:v1";

test("页面完整、无错误、移动端无横向溢出", async ({ page }, testInfo) => {
  const errors: string[] = [];
  page.on("pageerror", (error) => errors.push(error.message));
  page.on("console", (message) => { if (message.type() === "error") errors.push(message.text()); });
  const offsite: string[] = [];
  page.on("request", (request) => { if (!request.url().startsWith("http://127.0.0.1:3107") && !request.url().startsWith("blob:")) offsite.push(request.url()); });
  for (const path of ["/", "/calendar", "/research", "/corpus", "/creation", "/slides", "/office", "/resources", "/about", "/search", "/courses/01", "/courses/16"]) {
    const response = await page.goto(path);
    expect(response?.status()).toBe(200);
    await expect(page.getByRole("main").getByRole("heading", { level: 1 })).toBeVisible();
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), path).toBe(true);
  }
  expect(errors).toEqual([]);
  expect(offsite).toEqual([]);
  await page.goto("/");
  await page.screenshot({ path: testInfo.outputPath("home.png"), fullPage: true });
  if (testInfo.project.name === "desktop") {
    for (const width of [768, 1024]) {
      await page.setViewportSize({ width, height: 1024 });
      for (const path of ["/", "/calendar", "/resources", "/courses/01", "/research"]) {
        await page.goto(path);
        expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), `${width}px ${path}`).toBe(true);
      }
    }
  }
});

test("日历筛选、搜索、展开与视图切换", async ({ page }) => {
  await page.goto("/calendar");
  await expect(page.locator(".course-card")).toHaveCount(16);
  await expect(page.locator(".week-section")).toHaveCount(8);
  await page.getByRole("button", { name: /^教学/ }).click();
  await expect(page.locator(".course-card")).toHaveCount(6);
  await page.getByRole("button", { name: /^办公/ }).click();
  await expect(page.locator(".course-card")).toHaveCount(1);
  await page.getByRole("button", { name: /^全部课程/ }).click();
  await page.getByRole("searchbox", { name: "搜索课程", exact: true }).fill("文献");
  await expect(page.locator(".course-card")).toHaveCount(1);
  await page.locator(".course-details summary").click();
  await expect(page.locator(".detail-content")).toBeVisible();
  await page.getByRole("button", { name: "列表视图", exact: true }).click();
  await expect(page.locator(".calendar-list-item")).toHaveCount(1);
  await page.getByRole("searchbox", { name: "搜索课程", exact: true }).fill("找不到的课程xyz");
  await expect(page.getByRole("heading", { name: "没有找到符合条件的课程" })).toBeVisible();
  await page.getByRole("button", { name: "清空筛选" }).click();
  await expect(page.locator(".course-card")).toHaveCount(16);
});

test("笔记和进度刷新恢复、无输入外传、导出与清除", async ({ page }) => {
  const requests: string[] = [];
  page.on("request", (request) => { if (request.postData()?.includes("本地研究线索")) requests.push(request.url()); });
  await page.goto("/courses/01");
  await page.getByLabel("本课笔记与待解决的问题").fill("本地研究线索：核对中阿生态叙事材料。");
  await page.getByRole("checkbox", { name: "标记完成", exact: true }).check();
  await page.reload();
  await expect(page.getByLabel("本课笔记与待解决的问题")).toHaveValue("本地研究线索：核对中阿生态叙事材料。");
  await expect(page.getByRole("checkbox", { name: "已完成", exact: true })).toBeChecked();
  await page.goto("/resources");
  const downloadEvent = page.waitForEvent("download");
  await page.getByRole("button", { name: "导出本地 JSON" }).click();
  const download = await downloadEvent;
  const data = JSON.parse(await readFile((await download.path())!, "utf8"));
  expect(data.version).toBe(1);
  expect(data.completed).toEqual(["01"]);
  expect(data.notes["01"]).toContain("本地研究线索");
  await page.getByRole("button", { name: "清除本地数据" }).click();
  await page.getByRole("button", { name: "取消", exact: true }).click();
  expect(await page.evaluate((key) => localStorage.getItem(key), key)).not.toBeNull();
  await page.getByRole("button", { name: "清除本地数据" }).click();
  await page.getByRole("button", { name: "确认清除", exact: true }).click();
  expect(await page.evaluate((key) => localStorage.getItem(key), key)).toBeNull();
  await page.goto("/courses/01");
  await expect(page.getByLabel("本课笔记与待解决的问题")).toHaveValue("");
  expect(requests).toEqual([]);
});

test("模板筛选、复制和 CSV 下载内容正确", async ({ page }) => {
  await page.goto("/resources");
  await page.getByLabel("关联课程").selectOption("08");
  await expect(page.locator(".resource-card")).toHaveCount(3);
  await page.getByLabel("关联课程").selectOption("all");
  await page.getByRole("searchbox", { name: "搜索模板" }).fill("语料元数据");
  await expect(page.locator(".resource-card")).toHaveCount(1);
  const card = page.locator(".resource-card");
  await card.getByRole("button", { name: "复制模板" }).click();
  await expect(card.locator(".feedback")).toHaveText("已复制模板正文");
  expect(await page.evaluate(() => navigator.clipboard.readText())).toContain("doc_id");
  const downloadEvent = page.waitForEvent("download");
  await card.getByRole("button", { name: "下载 CSV" }).click();
  const download = await downloadEvent;
  expect(download.suggestedFilename()).toBe("语料元数据表.csv");
  const contents = await readFile((await download.path())!, "utf8");
  expect(contents.charCodeAt(0)).toBe(0xfeff);
  expect(contents).toContain("允许用途");
  await page.getByRole("searchbox", { name: "搜索模板" }).fill("无匹配xyz");
  await expect(page.getByRole("heading", { name: "没有找到符合条件的模板" })).toBeVisible();
  await page.getByRole("button", { name: "清空筛选" }).click();
  await expect(page.locator(".resource-card")).toHaveCount(18);
});

test("来源许可记录本地保存、验证和导出", async ({ page }) => {
  await page.goto("/resources#source-registry");
  const form = page.locator(".registration-form form");
  await form.getByLabel("来源名称", { exact: false }).fill("生态材料演练");
  await form.getByLabel("来源链接", { exact: false }).fill("https://example.org/source");
  await form.getByLabel("许可状态").selectOption("permitted");
  await form.getByRole("button", { name: "保存到本地" }).click();
  await expect(page.locator(".source-registry>.feedback")).toContainText("请同时填写许可依据");
  await form.getByLabel("许可依据").fill("演练：已获书面许可");
  await form.getByLabel("允许用途与限制").fill("演练：仅内部教学展示");
  await form.getByLabel("人工复核人").fill("教师甲（演练）");
  await form.getByLabel("复核日期").fill("2026-10-19");
  await form.getByRole("button", { name: "保存到本地" }).click();
  await expect(page.locator(".source-entry")).toHaveCount(1);
  await page.reload();
  await expect(page.locator(".source-entry")).toContainText("生态材料演练");
  const downloadEvent = page.waitForEvent("download");
  await page.getByRole("button", { name: "导出本地 JSON" }).click();
  const data = JSON.parse(await readFile((await (await downloadEvent).path())!, "utf8"));
  expect(data.sources[0].usage).toBe("演练：仅内部教学展示");
  await page.getByRole("button", { name: "删除记录", exact: true }).click();
  await page.getByRole("button", { name: "确认删除", exact: true }).click();
  await expect(page.locator(".source-entry")).toHaveCount(0);
});

test("搜索课程和模板，打印展开课程内容", async ({ page }) => {
  await page.goto("/search");
  await page.getByRole("searchbox", { name: "搜索全部课程与模板" }).fill("语料");
  await expect(page.locator("#search-courses")).toBeVisible();
  await expect(page.locator("#search-resources")).toBeVisible();
  await page.getByRole("button", { name: "模板", exact: true }).click();
  await expect(page.locator("#search-courses")).toHaveCount(0);
  await page.getByRole("searchbox").fill("不存在xyz");
  await expect(page.getByRole("heading", { name: "没有找到相关内容" })).toBeVisible();
  await page.goto("/calendar");
  await expect(page.locator(".detail-content").first()).not.toBeVisible();
  await page.emulateMedia({ media: "print" });
  await expect(page.locator(".detail-content").first()).toBeVisible();
  await expect(page.locator(".site-header")).not.toBeVisible();
});

test("本地记录可导出后导入恢复，非法文件不覆盖现有记录", async ({ page }) => {
  await page.goto("/courses/01");
  await page.getByLabel("本课笔记与待解决的问题").fill("导入恢复测试笔记");
  await page.getByRole("checkbox", { name: "标记完成", exact: true }).check();
  await page.goto("/resources");
  const downloadEvent = page.waitForEvent("download");
  await page.getByRole("button", { name: "导出本地 JSON" }).click();
  const exported = await readFile((await (await downloadEvent).path())!, "utf8");

  await page.getByRole("button", { name: "清除本地数据" }).click();
  await page.getByRole("button", { name: "确认清除", exact: true }).click();
  await page.goto("/courses/01");
  await expect(page.getByLabel("本课笔记与待解决的问题")).toHaveValue("");

  await page.goto("/resources");
  await page.getByLabel("选择本地记录 JSON 文件").setInputFiles({ name: "bad.json", mimeType: "application/json", buffer: Buffer.from("{bad", "utf8") });
  await expect(page.locator("#local-records").getByText("无法导入")).toBeVisible();
  await page.goto("/courses/01");
  await expect(page.getByLabel("本课笔记与待解决的问题")).toHaveValue("");

  await page.goto("/resources");
  await page.getByLabel("选择本地记录 JSON 文件").setInputFiles({ name: "records.json", mimeType: "application/json", buffer: Buffer.from(exported, "utf8") });
  const preview = page.getByRole("group", { name: "确认导入本地记录" });
  await expect(preview).toBeVisible();
  await expect(preview).toContainText("1 次课已完成");
  await page.getByRole("button", { name: "确认覆盖恢复" }).click();
  await expect(page.locator("#local-records .feedback")).toContainText("已恢复本地记录");

  await page.goto("/courses/01");
  await expect(page.getByLabel("本课笔记与待解决的问题")).toHaveValue("导入恢复测试笔记");
  await expect(page.getByRole("checkbox", { name: "已完成", exact: true })).toBeChecked();
});

test("损坏的本地记录不会被覆盖，能够导出原始备份", async ({ page }) => {
  await page.addInitScript((key) => { if (!localStorage.getItem(key)) localStorage.setItem(key, "{invalid json"); }, key);
  await page.goto("/courses/01");
  await expect(page.getByLabel("本课笔记与待解决的问题")).toBeDisabled();
  await page.goto("/resources");
  const downloadEvent = page.waitForEvent("download");
  await page.getByRole("button", { name: "导出本地 JSON" }).click();
  const data = JSON.parse(await readFile((await (await downloadEvent).path())!, "utf8"));
  expect(data.unreadableStorageBackup).toBe("{invalid json");
  expect(await page.evaluate((key) => localStorage.getItem(key), key)).toBe("{invalid json");
});

test("存储被禁用时保留当前会话并允许导出", async ({ page }) => {
  await page.addInitScript(() => { Storage.prototype.getItem = () => { throw new DOMException("Blocked", "SecurityError"); }; Storage.prototype.setItem = () => { throw new DOMException("Blocked", "SecurityError"); }; });
  await page.goto("/courses/01");
  await page.getByLabel("本课笔记与待解决的问题").fill("会话内记录");
  await expect(page.locator(".notebook [role=status]")).toContainText("浏览器存储不可用");
  const downloadEvent = page.waitForEvent("download");
  await page.getByRole("button", { name: "导出当前记录" }).click();
  const data = JSON.parse(await readFile((await (await downloadEvent).path())!, "utf8"));
  expect(data.notes["01"]).toBe("会话内记录");
});

test("404 与移动导航键盘入口", async ({ page }, testInfo) => {
  const response = await page.goto("/courses/99");
  expect(response?.status()).toBe(404);
  await expect(page.getByRole("heading", { name: "这条学习路径暂未收录。" })).toBeVisible();
  await page.goto("/");
  await page.keyboard.press("Tab");
  await expect(page.getByRole("link", { name: "跳至主要内容" })).toBeFocused();
  if (testInfo.project.name === "mobile") {
    await page.getByRole("button", { name: "展开导航" }).click();
    await page.getByRole("navigation", { name: "主导航" }).getByRole("link", { name: "课程日历" }).click();
    await expect(page).toHaveURL(/calendar$/);
    await expect(page.getByRole("button", { name: "展开导航" })).toBeVisible();
  }
});
