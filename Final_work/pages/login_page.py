from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        if (
            self.browser.current_url
            == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        ):
            assert True
        else:
            assert False, "Login url is not correct"

    def should_be_login_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        except NoSuchElementException:
            assert False

    def should_be_register_form(self):
        try:
            self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        except NoSuchElementException:
            assert False
        assert True

    def register_new_user(self):
        login_page = LoginPage(
            self.browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        )
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "123456789"
        try:
            login_page.browser.find_element(
                *LoginPageLocators.REGISTRATION_EMAIL
            ).send_keys(email)
            login_page.browser.find_element(
                *LoginPageLocators.REGISTRATION_PASSWORD
            ).send_keys(password)
            login_page.browser.find_element(
                *LoginPageLocators.CONFIRM_PASSWORD
            ).send_keys(password)
            login_page.browser.find_element(
                *LoginPageLocators.REGISTRATION_BUTTON
            ).click()
        except NoSuchElementException:
            assert False
