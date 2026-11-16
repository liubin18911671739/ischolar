# Repository Guidelines

## Project Structure

This repository is a Chinese-language teaching resource portal built with Next.js, React, TypeScript, and Tailwind CSS. Application routes and page styles live in `src/app/`; reusable UI lives in `src/components/`; course, guide, site, and resource content is maintained in `src/content/`; browser storage and download helpers are in `src/lib/`. `public/` contains static assets, `scripts/validate-content.ts` checks content consistency, `tests/` contains Playwright scenarios, and `docs/` holds content, deployment, and verification guidance.

## Development and Validation

Use Node.js 22 (or compatible Node.js 24) and install dependencies with `npm ci`. Common commands:

- `npm run dev` starts the local development server.
- `npm run check` runs ESLint, TypeScript, and content validation.
- `npm run test:content` checks course and resource consistency.
- `npm run test:e2e` runs Playwright browser scenarios (install Chromium first with `npx playwright install chromium`).
- `npm run build` validates and builds the production site; `npm run start` serves that build.

Run `npm run check` and `npm run build` after changes. Run end-to-end tests when modifying user flows, responsive behavior, downloads, or browser storage.

## Code and Content Conventions

Use TypeScript and follow the existing ESLint configuration. Use two spaces for indentation, semicolons, and the established double-quote style. Name React components and component files in PascalCase where practical; use lowercase route directories and descriptive kebab-case utility names. Keep content data in its corresponding `src/content/*.ts` module rather than duplicating totals or labels in page components. Preserve stable course and resource IDs; update related content and validation rules together. See `docs/CONTENT_GUIDE.md` before changing course, resource, platform-status, or browser-storage content.

## Testing and Review

Playwright tests are in `tests/` and use the `*.spec.ts` naming pattern. Add coverage for changed behavior and verify desktop and mobile layouts where relevant. Do not treat proposed or pending tools as tested or institutionally approved; status claims need scoped evidence, date, and responsible party.

## Commits and Pull Requests

The available Git history does not establish a commit-message convention. Use a concise imperative summary, such as `Improve resource search filters`. Pull requests should explain the user-visible change, list validation commands and results, link related work when applicable, and include screenshots for visual changes.

## Next.js Documentation

Before writing or changing application code, read the relevant guide in `node_modules/next/dist/docs/`. This project uses Next.js 16; verify APIs and conventions against the installed version rather than relying on older Next.js patterns.
