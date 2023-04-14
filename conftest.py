import pytest
from selenium import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

BaseUrl = "https://www.hudl.com/login"
Username = "admin"
Password = "testing"


@pytest.fixture(scope="class")
def browser_setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detatch", True)
    request.driver = webdriver.Chrome(ChromeDriverManager().install())
