import type { Locator, Page } from '@playwright/test';
import { Logger } from '../../utils/logger.js';

export interface LoginCredentials {
  email: string;
  password: string;
  acceptTerms?: boolean;
}

export class LoginPage {
  readonly page: Page;
  readonly logger: Logger;
  readonly baseUrl: string;

  constructor(page: Page, logger: Logger, baseUrl = 'https://app.conative.ai') {
    this.page = page;
    this.logger = logger;
    this.baseUrl = baseUrl;
  }

  private emailField(): Locator {
    return this.page
      .getByLabel(/email/i, { exact: false })
      .or(this.page.getByPlaceholder(/email/i))
      .or(this.page.locator('input[type="email"]'));
  }

  private passwordField(): Locator {
    return this.page
      .getByLabel(/password/i, { exact: false })
      .or(this.page.getByPlaceholder(/password/i))
      .or(this.page.locator('input[type="password"]'));
  }

  private termsCheckbox(): Locator {
    return this.page.getByRole('checkbox').filter({ hasText: /terms|service/i }).or(
      this.page.getByLabel(/terms of service|accept.*terms/i),
    );
  }

  private submitButton(): Locator {
    return this.page.getByRole('button', { name: /sign in|log in|continue/i }).first();
  }

  async goto(): Promise<void> {
    this.logger.step(`Navigate to ${this.baseUrl}/sign-in`);
    await this.page.goto(`${this.baseUrl}/sign-in`, { waitUntil: 'domcontentloaded' });
    await this.page.waitForLoadState('networkidle', { timeout: 20_000 }).catch(() => {
      this.logger.warn('Network idle did not complete within timeout; continuing with page load');
    });
  }

  async login({ email, password, acceptTerms = true }: LoginCredentials): Promise<void> {
    this.logger.step(`Enter email and password for sign-in`);
    await this.emailField().waitFor({ state: 'visible', timeout: 20_000 });
    await this.emailField().fill(email);
    await this.passwordField().waitFor({ state: 'visible', timeout: 20_000 });
    await this.passwordField().fill(password);

    if (acceptTerms) {
      this.logger.step('Accept terms of service checkbox');
      await this.termsCheckbox().waitFor({ state: 'visible', timeout: 20_000 }).catch(() => {
        this.logger.warn('Terms checkbox not found by default selector. Continuing with alternate form handling');
      });
      const terms = this.termsCheckbox();
      if (await terms.count()) {
        await terms.first().check({ force: true }).catch(async () => {
          await terms.first().click({ force: true });
        });
      }
    }

    this.logger.step('Click sign in button');
    await this.submitButton().waitFor({ state: 'visible', timeout: 20_000 });
    await this.submitButton().click();
  }
}
