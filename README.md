# smartui-playwright-python-sdk
SmartUI SDK support for Playwright (Python)


This project demonstrates how to use playwright and LambdaTest together to run automated tests on the LambdaTest platform.

## Setup

First, clone this repository to your local machine.

```bash
git clone https://github.com/LambdaTest/smartui-playwright-python-sdk-sample.git
cd smartui-playwright-python-sdk-sample
```

Next, install the necessary dependencies:



```bash
npm install @lambdatest/smartui-cli
pip3 install -r requirements.txt
```

You'll need to set your LambdaTest username and access key as environment variables. They can be found on your LambdaTest profile.

```bash
export LT_USERNAME="Your LambdaTest Username"
export LT_ACCESS_KEY="Your LambdaTest Access Key"
```


## Running Tests

To run the test, execute:

```bash
npx smartui exec python3 SmartUI_SDK_LT_hub.py 
```

```bash
npx smartui exec python3 SmartUI_SDK_Ignore.py 
```

To run locally, run the following command

```bash
export PROJECT_TOKEN="123456#1234abcd-****-****-****-************"
npx smartui exec python3 SmartUI_SDK_local.py 
```