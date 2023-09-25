from core.element.element import Element
from selenium.webdriver.common.by import By
from ..base_page import BasePage


class SignInForm(BasePage):
    def __init__(self):
        super().__init__()
        self._lnk_sign_up = Element((By.ID, "//a[contains(text(), 'SIGN UP')"))
        self._txt_email = Element((By.ID, 'email'))
        self._txt_password = Element((By.ID, 'password'))
        self._btn_sign_in = Element((By.XPATH, "//span[text()='SIGN IN']"))
        self._msg_error = Element((By.XPATH, "//div[contains(text(), 'ErrorText')"))

    def enter_email(self, email):
        self._txt_email.enter(email)

    def enter_password(self, password):
        self._txt_password.enter(password)

    def click_sign_in_btn(self):
        self._btn_sign_in.click()
        self.wait_for_loading()

    def login(self, account):
        self.enter_email(account.email)
        self.enter_password(account.password)
        self.click_sign_in_btn()

    def get_error_msg(self):
        return self._msg_error.get_text()
