import os
import json
import urllib.parse
from playwright.sync_api import sync_playwright
from lambdatest_playwright_driver import smartui_snapshot


USERNAME = os.getenv("LT_USERNAME", "<USERNAME>")
ACCESS_KEY = os.getenv("LT_ACCESS_KEY", "<ACCESS_KEY>")
GITHUB_URL = os.getenv("GITHUB_URL")

capabilities = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "LT:Options": {
        "platform": "Windows 10",
        "build": "Playwright SmartUI Build",
        "name": "Playwright SmartUI Test",
        "user": USERNAME,
        "accessKey": ACCESS_KEY,
        "network": True,
        "video": True,
        "console": True,
    },
}

if GITHUB_URL:
    capabilities["LT:Options"]["github"] = {"url": GITHUB_URL}

with sync_playwright() as p:
    encoded_capabilities = urllib.parse.quote(json.dumps(capabilities))
    ws_endpoint = f"wss://cdp.lambdatest.com/playwright?capabilities={json.dumps(capabilities)}"
    browser = p.chromium.connect(ws_endpoint)

    page = browser.new_page()
    page.goto("https://ipinfo.io/")

    options = {
        "ignoreDOM": {
            "xpath": ['//*[@id="__next"]/div/div/main/section[4]']
        }
    }

    # Add the following command to take a screenshot in SmartUI
    smartui_snapshot(page, "Ignore-ticker", options)

    browser.close()
