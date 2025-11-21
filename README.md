# SmartUI SDK Sample for Playwright Python

Welcome to the SmartUI SDK sample for Playwright Python. This repository demonstrates how to integrate SmartUI visual regression testing with Playwright Python.

## Prerequisites

- Python 3.7 or higher
- Node.js (for SmartUI CLI)
- LambdaTest account credentials (for Cloud tests)
- Chrome browser (for Local tests)

## Repository Structure

```
smartui-playwright-python-sdk-sample/
├── SmartUI_SDK_LT_hub.py      # Cloud test
├── SmartUI_SDK_local.py        # Local test
├── SmartUI_SDK_Ignore.py       # Example with ignore options
├── requirements.txt             # Python dependencies
└── smartui-web.json             # SmartUI config (create with npx smartui config:create)
```

## Quick Start

### Local Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LambdaTest/smartui-playwright-python-sdk-sample
   cd smartui-playwright-python-sdk-sample
   ```

2. **Install dependencies** (recommended: use virtual environment):
   
   **For Python 3.13+** (if you encounter greenlet errors):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   npm install @lambdatest/smartui-cli
   pip install playwright lambdatest-playwright-driver lambdatest-sdk-utils
   python -m playwright install chromium
   ```
   
   **For Python 3.7-3.12**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   npm install @lambdatest/smartui-cli
   pip install -r requirements.txt
   python -m playwright install chromium
   ```

3. **Set your Project Token:**
   ```bash
   export PROJECT_TOKEN='your_project_token'
   ```

4. **Create SmartUI config:**
   ```bash
   npx smartui config:create smartui-web.json
   ```

5. **Run the test** (activate venv first if using one):
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate (if using venv)
   npx smartui exec python SmartUI_SDK_local.py
   ```

### Cloud Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LambdaTest/smartui-playwright-python-sdk-sample
   cd smartui-playwright-python-sdk-sample
   ```

2. **Install dependencies** (recommended: use virtual environment):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   npm install @lambdatest/smartui-cli
   pip install -r requirements.txt
   ```

3. **Set your credentials:**
   ```bash
   export LT_USERNAME='your_username'
   export LT_ACCESS_KEY='your_access_key'
   export PROJECT_TOKEN='your_project_token'
   ```

4. **Create SmartUI config:**
   ```bash
   npx smartui config:create smartui-web.json
   ```

5. **Run the test** (activate venv first if using one):
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate (if using venv)
   npx smartui exec python SmartUI_SDK_LT_hub.py
   ```

## Dependencies

The project uses the following key dependencies (configured in `requirements.txt`):

- `playwright` - Playwright Python library
- `lambdatest-playwright-driver` - SmartUI SDK for Playwright Python
- `lambdatest-sdk-utils` - LambdaTest SDK utilities

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
