# SmartUI SDK Sample for Playwright Python

Welcome to the SmartUI SDK sample for Playwright Python. This repository demonstrates how to integrate SmartUI visual regression testing with Playwright Python.

## Repository Structure

```
smartui-playwright-python-sdk-sample/
├── SmartUI_SDK_LT_hub.py      # Cloud test
├── SmartUI_SDK_local.py        # Local test
├── SmartUI_SDK_Ignore.py       # Example with ignore options
├── requirements.txt             # Python dependencies
└── smartui-web.json             # SmartUI config (create with npx smartui config:create)
```

## 1. Prerequisites and Environment Setup

### Prerequisites

- Python 3.7 or higher
- Node.js (for SmartUI CLI)
- LambdaTest account credentials (for Cloud tests)
- Chrome browser (for Local tests)

### Environment Setup

**For Cloud:**
```bash
export LT_USERNAME='your_username'
export LT_ACCESS_KEY='your_access_key'
export PROJECT_TOKEN='your_project_token'
```

**For Local:**
```bash
export PROJECT_TOKEN='your_project_token'
```

## 2. Initial Setup and Dependencies

### Clone the Repository

```bash
git clone https://github.com/LambdaTest/smartui-playwright-python-sdk-sample
cd smartui-playwright-python-sdk-sample
```

### Install Dependencies

**Recommended: Use a virtual environment** (recommended to avoid dependency conflicts):

**For Python 3.13+** (if you encounter greenlet errors):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
npm install @lambdatest/smartui-cli
pip install playwright lambdatest-playwright-driver lambdatest-sdk-utils
python -m playwright install chromium  # Local only
```

**For Python 3.7-3.12**:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
npm install @lambdatest/smartui-cli
pip install -r requirements.txt
python -m playwright install chromium  # Local only
```

**Dependencies included:**
- `playwright` - Playwright Python library
- `lambdatest-playwright-driver` - SmartUI SDK for Playwright Python
- `lambdatest-sdk-utils` - LambdaTest SDK utilities

### Create SmartUI Configuration

```bash
npx smartui config:create smartui-web.json
```

## 3. Steps to Integrate Screenshot Commands into Codebase

The SmartUI screenshot function is already implemented in the repository.

**Cloud Test** (`SmartUI_SDK_LT_hub.py`):
```python
from lambdatest_playwright_driver import smartui_snapshot

page.goto("https://www.lambdatest.com")
smartui_snapshot(page, "screenshot")
```

**Local Test** (`SmartUI_SDK_local.py`):
```python
from lambdatest_playwright_driver import smartui_snapshot

page.goto("https://www.lambdatest.com")
smartui_snapshot(page, "screenshot")
```

**Note**: The code is already configured and ready to use. You can modify the URL and screenshot name if needed.

## 4. Execution and Commands

**If using a virtual environment**, activate it first:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Local Execution

```bash
npx smartui exec python SmartUI_SDK_local.py
```

### Cloud Execution

```bash
npx smartui exec python SmartUI_SDK_LT_hub.py
```

## Test Files

### Cloud Test (`SmartUI_SDK_LT_hub.py`)

- Connects to LambdaTest Cloud using CDP (Chrome DevTools Protocol)
- Reads credentials from environment variables (`LT_USERNAME`, `LT_ACCESS_KEY`)
- Takes screenshot with name: `screenshot`

### Local Test (`SmartUI_SDK_local.py`)

- Runs Playwright locally using Chromium
- Requires Chrome browser installed
- Takes screenshot with name: `screenshot`

### Ignore Example (`SmartUI_SDK_Ignore.py`)

- Demonstrates how to use ignore options in SmartUI snapshots
- Shows how to exclude specific DOM elements from visual comparison

## View Results

After running the tests, visit your SmartUI project dashboard to view the captured screenshots and compare them with baseline builds.

## More Information

For detailed onboarding instructions, see the [SmartUI Playwright Python Onboarding Guide](https://www.lambdatest.com/support/docs/smartui-onboarding-playwright-python/).
