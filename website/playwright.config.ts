import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./tests", fullyParallel: true, retries: 0, workers: 2,
  reporter: [["list"], ["html", { open: "never" }]],
  use: { baseURL: "http://127.0.0.1:3107", trace: "retain-on-failure", screenshot: "only-on-failure" },
  projects: [
    { name: "desktop", testMatch: ["**/workbench.spec.ts", "**/accessibility.spec.ts"], use: { ...devices["Desktop Chrome"], viewport: { width: 1440, height: 1000 }, permissions: ["clipboard-read", "clipboard-write"] } },
    { name: "mobile", testMatch: ["**/workbench.spec.ts", "**/accessibility.spec.ts"], use: { ...devices["Pixel 7"], viewport: { width: 390, height: 844 }, permissions: ["clipboard-read", "clipboard-write"] } },
    { name: "firefox", testMatch: ["**/cross-browser.spec.ts", "**/accessibility.spec.ts"], use: { ...devices["Desktop Firefox"], viewport: { width: 1440, height: 1000 } } },
    { name: "webkit", testMatch: ["**/cross-browser.spec.ts", "**/accessibility.spec.ts"], use: { ...devices["Desktop Safari"], viewport: { width: 1440, height: 1000 } } },
    { name: "mobile-webkit", testMatch: ["**/cross-browser.spec.ts", "**/accessibility.spec.ts"], use: { ...devices["iPhone 13"] } },
  ],
  webServer: { command: "npm run start -- --hostname 127.0.0.1 --port 3107", url: "http://127.0.0.1:3107", reuseExistingServer: false, timeout: 60000 },
});
