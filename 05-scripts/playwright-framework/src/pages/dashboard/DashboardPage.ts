import type { Page } from '@playwright/test';
import { expect } from '@playwright/test';
import { Logger } from '../../utils/logger.js';

export class DashboardPage {
  readonly page: Page;
  readonly logger: Logger;

  constructor(page: Page, logger: Logger) {
    this.page = page;
    this.logger = logger;
  }

  async waitForDashboardVisible(): Promise<void> {
    this.logger.step('Verify dashboard is displayed');
    await expect(this.page.getByRole('heading', { name: /dashboard/i })).toBeVisible({ timeout: 30_000 });
  }
}
