from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Selenium_Helper:

    def __init__(self, driver):
        self.driver = driver

    def webelement_type(self, locator, text):
        '''
        Types specified text input into specified locator
        '''
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def webelement_click(self, locator):
        '''
        Clicks element by locator
        '''
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator)).click()