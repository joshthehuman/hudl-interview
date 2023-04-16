from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import *



def url_wait(driver, locator):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be(locator))

def locator_wait(driver, locator):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(locator))

def login(driver, username, password, checkbox: bool):
    # Open baseUrl
    baseUrl = "https://www.hudl.com/login"
    driver.get(baseUrl)

    # Login Page Locators
    email_field = driver.find_element(By.CSS_SELECTOR, FORM_EMAIL_FIELD)
    password_field = driver.find_element(By.CSS_SELECTOR, FORM_PASSWORD_FIELD)
    login_button = driver.find_element(By.CSS_SELECTOR, FORM_LOGIN_BUTTON)
    rememeber_me_checkbox = driver.find_element(By.CSS_SELECTOR, REMEMBER_ME_CHECKBOX)
    
    # If checkbox == True, check the 'Remember me' box
    if checkbox == False:
        # Enter valid/invalid username and password
        email_field.send_keys(username)
        password_field.send_keys(password)
    elif checkbox == True:
        if not rememeber_me_checkbox.is_selected():
            rememeber_me_checkbox.click()

    # Click login button
    login_button.click()

def logout(driver):
    # homePage
    baseUrl = "https://www.hudl.com/home"
    driver.get(baseUrl)

    # Homepage Locators
    LOGOUT_BUTTON = driver.find_element(By.CSS_SELECTOR, "[data-qa-id='webnav-usermenu-logout']")

    # Click Logout Button
    locator_wait(driver, LOGOUT_BUTTON)
    LOGOUT_BUTTON.click()

def page_verification():
    driver = webdriver.Chrome()
    
    baseUrl = "https://www.hudl.com/login"
    driver.get(baseUrl)

    # Assign variables to all elements on the page
    page_elements = {
        'signup_button': driver.find_element(By.CSS_SELECTOR, SIGN_UP_BUTTON),
        'hudl_logo': driver.find_element(By.CSS_SELECTOR, HUDL_LOGO),
        'email_label': driver.find_element(By.CSS_SELECTOR, FORM_EMAIL_LABEL),
        'email_field': driver.find_element(By.CSS_SELECTOR, FORM_EMAIL_FIELD),
        'password_label': driver.find_element(By.CSS_SELECTOR, FORM_PASSWORD_LABEL),
        'password_field': driver.find_element(By.CSS_SELECTOR, FORM_PASSWORD_FIELD),
        'login_button': driver.find_element(By.CSS_SELECTOR, FORM_LOGIN_BUTTON),
        'rememeber_me_label': driver.find_element(By.CSS_SELECTOR, REMEMBER_ME_LABEL),
        'rememeber_me_checkbox': driver.find_element(By.CSS_SELECTOR, REMEMBER_ME_CHECKBOX),
        'need_help_link': driver.find_element(By.CSS_SELECTOR, NEED_HELP_LINK),
        'org_login_link': driver.find_element(By.CSS_SELECTOR, ORG_LOGIN_LINK)
    }

    # Verify all elements appear on the page
    for element_name, element in page_elements.items():
        assert element.is_displayed(), f"{element_name} not found on the page."