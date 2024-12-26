Overview

This project contains a Python script (qa_selenium_test.py) that uses Selenium to automate a test case for the Selenium Playground Table Search Demo. The script:

Navigates to the table search demo page.

Locates the search box.

Inputs the text "New York" to filter the table.

Validates that exactly 5 table rows are displayed as a result of the search.

The test is structured using the pytest framework for robust and maintainable test execution.

Prerequisites

1. Python Environment

Ensure Python 3.10 or later is installed on your machine.

Install Selenium:

pip install selenium

Install Pytest:

pip install pytest

2. Chrome Browser and ChromeDriver

Browser: Ensure Google Chrome is installed. You can check your Chrome version by navigating to chrome://settings/help in Chrome.

ChromeDriver: Download the version of ChromeDriver that matches your Chrome version from ChromeDriver Downloads. Place the chromedriver.exe in an accessible directory (e.g., C:\Drivers\).

File Structure

qa_selenium_test.py: The Python test script.

requirements.txt (optional): Contains dependencies like selenium and pytest.

How to Run the Script

Step 1: Update the Script with ChromeDriver Path

In qa_selenium_test.py, update the path to your ChromeDriver executable:

service = Service("C:\\Drivers\\chromedriver.exe")

Step 2: Execute the Test

Run the test using pytest:

pytest qa_selenium_test.py

Expected Outcome

The script will open a browser, navigate to the demo page, input "New York" in the search box, and validate that 5 rows are displayed.

If successful, the test will pass. If not, an assertion error will provide details.

Notes

Ensure that your Chrome and ChromeDriver versions are compatible to avoid SessionNotCreatedException errors.

If you encounter issues, verify your Python, Selenium, and browser setup.
