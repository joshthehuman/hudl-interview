from selenium.webdriver.common.by import By
from helper.selenium_helper import Selenium_Helper

class LoginPage(Selenium_Helper):
    
    #Login Page Elements
    FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "[data-qa-id='email-input']")
    FORM_PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-qa-id='password-input']")
    FORM_LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-qa-id='login-btn']")

    def __init__(self, driver):
        super().__init__(driver)
    
    def login(self, username, password):
        self.webelement_type(self.FORM_EMAIL_FIELD, username)
        self.webelement_type(self.FORM_PASSWORD_FIELD, password)
        self.webelement_click(self.FORM_LOGIN_BUTTON)
   