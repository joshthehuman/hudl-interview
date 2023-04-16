h1. README

This repository contains four Python files for testing the login page of the Hudl website using Selenium and Pytest.

Files:

login_page.py: This file contains CSS selectors for all elements on the login page of the Hudl website.
test_data.py: This file contains global variables for the test methods, including the home page URL, valid and invalid credentials for logging in.
test_methods.py: This file contains methods for waiting for elements to appear on the page, logging in and out of the website, and verifying that all expected elements are present on the login page.
test_login.py: This file contains all test methods for testing the login page.
Instructions:

Install Selenium and Pytest: pip install selenium pytest
Download the appropriate version of chromedriver for your machine: https://chromedriver.chromium.org/downloads
Add chromedriver to your system PATH.
Run pytest test_login.py in the command line to run all tests.