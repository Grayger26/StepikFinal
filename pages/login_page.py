from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from .locators import LoginPageLocators
import faker

f = faker.Faker()

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        get_url = self.browser.current_url
        assert get_url == "http://selenium1py.pythonanywhere.com/ru/accounts/login/", "Wrong url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email field is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password field is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_EMAIL), "Sign in email field is not present"
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_PASSWORD), "Sign in password field is not present"
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_BUTTON), "Sign in button is not present"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def register_new_user(self):
        email = f.email()
        password = "Olympus2023!"
        email_field = self.browser.find_element(*LoginPageLocators.SIGN_IN_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.SIGN_IN_PASSWORD)
        password_confirm = self.browser.find_element(*LoginPageLocators.SIGN_IN_PASSWORD_CONFIRM)
        reg_button = self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm.send_keys(password)
        reg_button.click()

