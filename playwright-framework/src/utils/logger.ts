export class Logger {
  private readonly prefix = '[Automation]';

  info(message: string): void {
    console.log(`${this.prefix} INFO: ${message}`);
  }

  step(message: string): void {
    console.log(`${this.prefix} STEP: ${message}`);
  }

  warn(message: string): void {
    console.warn(`${this.prefix} WARN: ${message}`);
  }

  error(message: string): void {
    console.error(`${this.prefix} ERROR: ${message}`);
  }
}
