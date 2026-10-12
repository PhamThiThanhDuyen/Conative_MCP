export interface AppConfig {
  baseUrl: string;
  email?: string;
  password?: string;
  acceptTerms: boolean;
}

export function getAppConfig(): AppConfig {
  return {
    baseUrl: process.env.BASE_URL || 'https://app.conative.ai',
    email: process.env.TEST_EMAIL,
    password: process.env.TEST_PASSWORD,
    acceptTerms: (process.env.ACCEPT_TERMS || 'true').toLowerCase() === 'true',
  };
}
