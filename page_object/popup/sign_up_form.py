from core.element.element import Element
from selenium.webdriver.common.by import By
from .base_page import BasePage


class SignUpForm(BasePage):
    def __init__(self):
        super().__init__()
        self._lnk_sign_in = Element((By.ID, "//a[contains(text(), 'SIGN IN')"))
        self._txt_email = Element((By.ID, 'email'))
        self._txt_password = Element((By.ID, 'password'))
        self._btn_sign_up = Element((By.XPATH, "//span[text()='SIGN UP']"))
        self._msg_error = Element((By.XPATH, "//div[contains(text(), 'ErrorText')"))

    def enter_email(self, email):
        self._txt_email.enter(email)

    def enter_password(self, password):
        self._txt_password.enter(password)

    def click_sign_up_btn(self):
        self._btn_sign_up.click()

    def create_account(self, account):
        self._txt_email.enter(account.email)
        self._txt_password.enter(account.password)
        self._btn_sign_up.click()

    def get_error_msg(self):
        return self._error_message.get_text()
