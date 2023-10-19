# test_item.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.fixture
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_cart_button(browser):
    browser.get(link)
    assert browser.find_element(By.ID, "add_to_basket_form")
    time.sleep(15)
