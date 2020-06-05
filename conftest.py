import pytest
from selenium import webdriver


@pytest.fixture()
def browser(request):
    path = r'C:/webdrivers/chrome/chromedriver.exe'
    browser = webdriver.Chrome(path)

    # Close browser
    yield browser
    browser.quit()


