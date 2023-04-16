from selenium import webdriver
from selenium.webdriver.common.by import By
from testmethods import login, logout, url_wait, locator_wait, page_verification
from testdata import homePage, valid_username, valid_password, invalid_cred


# Verify a user is able to log in with a valid Username + Password
def test_valid_login():
    # Webdriver
    driver = webdriver.Chrome()

    # Login with valid credentials
    login(driver, valid_username, valid_password, False)

    # Check resulting page is homePage
    url_wait(driver, homePage)
    assert driver.current_url == homePage

    # Close the browser
    driver.quit()

# Verify a user is not able to log in with invalid credentials
def test_invalid_login():
    # Webdriver
    driver = webdriver.Chrome()

    # Login with invalid credentials
    login(driver, invalid_cred, invalid_cred, False)

    # Wait for the error display element to be visible on the page
    ERROR_DISPLAY = (By.CSS_SELECTOR, "[data-qa-id='error-display']")
    locator_wait(driver, ERROR_DISPLAY)

    # Check that the error display element is visible on the page
    assert driver.find_element(*ERROR_DISPLAY).is_displayed()

    # Close the browser
    driver.quit()

# Verify usernames are not case sensitive
def test_case_sensitivity():
    # Webdriver
    driver = webdriver.Chrome()

    # Login with valid credentials
    login(driver, valid_username.upper(), valid_password, False)

    # Check resulting page is homePage
    url_wait(driver, homePage)
    assert driver.current_url == homePage

    # Close the browser
    driver.quit()

# Verify all elements appear on the login page correctly
def test_page_verification():
    page_verification()

