import { expect, test } from '../src/fixtures/test.js';
import { LoginPage } from '../src/pages/auth/LoginPage.js';
import { DashboardPage } from '../src/pages/dashboard/DashboardPage.js';

test.describe('Conative sign-in flow', () => {
  test('signs in and opens the dashboard when credentials are configured', async ({ page, logger, appConfig }) => {
    const email = appConfig.email;
    const password = appConfig.password;

    test.skip(!email || !password, 'Set TEST_EMAIL and TEST_PASSWORD in the environment to run this login scenario.');

    const loginPage = new LoginPage(page, logger, appConfig.baseUrl);
    await loginPage.goto();
    await loginPage.login({ email, password, acceptTerms: appConfig.acceptTerms });

    const dashboardPage = new DashboardPage(page, logger);
    await dashboardPage.waitForDashboardVisible();

    await expect(page).toHaveURL(/dashboard|overview|home/i);
  });
});
