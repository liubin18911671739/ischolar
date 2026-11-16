import { expect, test } from "@playwright/test";

test("cross-browser routes, learning flows, and keyboard entry", async ({ page }, testInfo) => {
  for (const path of ["/", "/calendar", "/research", "/resources", "/about", "/search", "/courses/01", "/courses/16"]) {
    const response = await page.goto(path);
    expect(response?.status(), path).toBe(200);
    await expect(page.getByRole("main").getByRole("heading", { level: 1 }), path).toBeVisible();
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1), path).toBe(true);
  }
  if (!["mobile-webkit", "webkit"].includes(testInfo.project.name)) {
    await page.goto("/");
    await page.keyboard.press("Tab");
    await expect(page.getByRole("link", { name: "跳至主要内容" })).toBeFocused();
  }

  await page.goto("/calendar");
  await page.getByRole("button", { name: /^教学/ }).click();
  await expect(page.locator(".course-card")).toHaveCount(6);

  await page.goto("/courses/01");
  await page.getByLabel("本课笔记与待解决的问题").fill(`browser check ${testInfo.project.name}`);
  await page.reload();
  await expect(page.getByLabel("本课笔记与待解决的问题")).toHaveValue(`browser check ${testInfo.project.name}`);

  if (testInfo.project.name === "mobile-webkit") {
    await page.goto("/");
    await page.getByRole("button", { name: "展开导航" }).focus();
    await page.keyboard.press("Enter");
    await expect(page.getByRole("navigation", { name: "主导航" })).toBeVisible();
  }
});
