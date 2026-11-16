import AxeBuilder from "@axe-core/playwright";
import { expect, test } from "@playwright/test";

const allRoutes = [
  "/", "/calendar", "/research", "/corpus", "/creation", "/slides", "/office",
  "/resources", "/about", "/search",
  ...Array.from({ length: 16 }, (_, index) => `/courses/${String(index + 1).padStart(2, "0")}`),
];
const engineRoutes = ["/", "/calendar", "/research", "/resources", "/about", "/search", "/courses/01"];
const wcag22aa = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"];

test("WCAG 2.2 AA automated accessibility audit", async ({ page }, testInfo) => {
  const routes = ["desktop", "mobile"].includes(testInfo.project.name) ? allRoutes : engineRoutes;
  const findings: Array<{ route: string; violations: Array<{ id: string; impact: string | undefined; help: string; targets: string[] }> }> = [];

  for (const route of routes) {
    await page.goto(route);
    const result = await new AxeBuilder({ page })
      .withTags(wcag22aa)
      .options({ rules: { "target-size": { enabled: true } } })
      .analyze();
    if (result.violations.length) {
      findings.push({
        route,
        violations: result.violations.map((violation) => ({
          id: violation.id,
          impact: violation.impact ?? "unknown",
          help: violation.help,
          targets: violation.nodes.map((node) => node.target.join(" ")),
        })),
      });
    }
  }

  expect(findings, JSON.stringify(findings, null, 2)).toEqual([]);
});
