import pytest
from selenium import webdriver


@pytest.fixture()
def browser(request):
    path = 'C:\webdrivers\chrome'
    browser = webdriver.Chrome(path)

    # Close browser
    yield browser
    browser.quit()


