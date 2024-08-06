const { test, expect } = require("@playwright/test");

test.describe("Chat Bot UI Tests", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("http://localhost:5000");
  });

  test('should display greeting message when "hello" is sent', async ({
    page,
  }) => {
    await page.fill("#user-input", "hello");
    await page.click("button");
    await page.waitForSelector("text=Hello! How can I assist you today?");
    const botMessage = await page
      .locator("text=Hello! How can I assist you today?")
      .textContent();
    expect(botMessage).toBe("Hello! How can I assist you today?");
  });

  test('should display help message when "help" is sent', async ({ page }) => {
    await page.fill("#user-input", "help");
    await page.click("button");
    await page.waitForSelector("text=Available commands: hello, help");
    const botMessage = await page
      .locator("text=Available commands: hello, help")
      .textContent();
    expect(botMessage).toBe("Available commands: hello, help");
  });

  test("should display default message for unknown command", async ({
    page,
  }) => {
    await page.fill("#user-input", "unknown");
    await page.click("button");
    await page.waitForSelector("text=I'm sorry, I didn't understand that.");
    const botMessage = await page
      .locator("text=I'm sorry, I didn't understand that.")
      .textContent();
    expect(botMessage).toBe("I'm sorry, I didn't understand that.");
  });
});
