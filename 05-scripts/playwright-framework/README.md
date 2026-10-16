# Playwright End-to-End Automation Framework

This project is a reusable Playwright + TypeScript automation framework built from the requirements in `Framework_Prompts.txt`.

## Included features

- Playwright Test runner for browser automation
- Support for Chromium, Firefox, and WebKit
- TypeScript configuration for safer test authoring
- Smart selectors for labels, placeholders, and role-based access
- Structured logging with step-by-step tracing
- Screenshot and video capture on failure
- Parallel execution support
- Browser and environment configuration via `.env`
- Example smoke test and Conative sign-in flow test

## Quick start

1. Go to the framework folder:
   ```bash
   cd playwright-framework
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Install browser engines:
   ```bash
   npx playwright install --with-deps
   ```
4. Copy the example environment file and set test credentials locally. Keep `.env` out of version control; never commit real credentials:
   ```bash
   cp .env.example .env
   ```
5. Run the smoke test:
   ```bash
   npm test -- --project=chromium tests/smoke.spec.ts
   ```

## Run all tests

```bash
npm test
```

## Browser-specific runs

```bash
npm run test:chrome
npm run test:firefox
npm run test:webkit
```

## Environment variables

- `BASE_URL`: default app URL, usually `https://app.conative.ai`
- `TEST_EMAIL`: login email for the Conative login flow
- `TEST_PASSWORD`: login password for the Conative login flow
- `ACCEPT_TERMS`: set to `true` if the sign-in form requires accepting the terms checkbox

## Suggested test-writing pattern

When creating new tests, use these steps:

1. Start from a known page or URL.
2. Log each step clearly.
3. Use resilient locators based on label, placeholder, text, and role.
4. Check expected content with explicit assertions.
5. Capture screenshots and videos automatically when tests fail.

## Example test request

```text
Website: https://app.conative.ai/sign-in
Goal: Sign in, open the organization page, and verify the Dashboard page is visible.
Conditions: Terms must be accepted before submitting.
Success: Dashboard page heading is visible.
Watch for: slow page loads, invalid credentials, and missing form fields.
```

## Project structure

```text
playwright-framework/
├── src/
│   ├── fixtures/
│   ├── pages/
│   └── utils/
├── tests/
├── .env.example
├── playwright.config.ts
├── package.json
├── tsconfig.json
└── README.md
```
