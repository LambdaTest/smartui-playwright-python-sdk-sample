# Installation Guide

## Python 3.13+ Users

If you're using Python 3.13 or later and encounter `greenlet` compilation errors, follow these steps:

### Step 1: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 2: Install Playwright Directly (Bypasses greenlet issue)

```bash
pip install playwright lambdatest-playwright-driver lambdatest-sdk-utils
```

### Step 3: Install Chromium Browser

```bash
python -m playwright install chromium
```

### Step 4: Verify Installation

```bash
python -c "import playwright; print('Playwright installed successfully')"
```

## Python 3.7-3.12 Users

You can use the standard requirements.txt:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
```

## Alternative: Use Python 3.12

If you continue to have issues with Python 3.13, consider using Python 3.12:

```bash
# Install Python 3.12 via Homebrew (macOS)
brew install python@3.12

# Create venv with Python 3.12
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
```

