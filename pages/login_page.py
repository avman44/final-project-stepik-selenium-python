from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.current_url, "\"login\" is not presented"

    def should_be_login_form(self):
        try:
            self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        except (NoSuchElementException):
            return False
        assert True, "Login form is not presented"

    def should_be_register_form(self):
        try:
            self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        except (NoSuchElementException):
            return False
        assert True, "Register form is not presented"