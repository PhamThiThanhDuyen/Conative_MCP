import { expect, test } from '../src/fixtures/test.js';

test.describe('Framework smoke checks', () => {
  test('home page loads and shows expected hero content', async ({ page, logger }) => {
    logger.step('Open Playwright landing page');
    await page.goto('https://playwright.dev');

    await expect(page.locator('h1')).toContainText('Playwright', { timeout: 15_000 });
    logger.step('Smoke test completed successfully');
  });
});
