import pytest
from conftest import browser_setup, BaseUrl, Username, Password
from pages.login_page import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_Login:
    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.login(Username, Password)

    def teardown_class(self):
        self.driver.quit()
