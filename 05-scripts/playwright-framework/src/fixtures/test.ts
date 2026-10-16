import { test as base, expect } from '@playwright/test';
import { Logger } from '../utils/logger.js';
import { getAppConfig, type AppConfig } from '../utils/test-data.js';

export type FrameworkFixtures = {
  logger: Logger;
  appConfig: AppConfig;
};

export const test = base.extend<FrameworkFixtures>({
  logger: async ({}, use) => {
    await use(new Logger());
  },
  appConfig: async ({}, use) => {
    await use(getAppConfig());
  },
});

export { expect };
