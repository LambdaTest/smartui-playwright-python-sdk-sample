from playwright.sync_api import sync_playwright
from lambdatest_playwright_driver import smartui_snapshot

def run(playwright):
    # Launch a local browser instance
    browser = playwright.chromium.launch(headless=False)  # Set headless to False to see the browser UI
    page = browser.new_page()

    try:
        # Navigate to the desired URL
        print("Navigating to URL")
        page.goto("https://www.lambdatest.com")

        # Use smartuiSnapshot to take a visual snapshot locally
        smartui_snapshot(page, "screenshot")
        print("Snapshot taken")
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the browser
        browser.close()
        print("Browser closed")

with sync_playwright() as playwright:
    run(playwright)
