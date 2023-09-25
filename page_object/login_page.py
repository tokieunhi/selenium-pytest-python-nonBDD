from core.element.element import Element
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self._login_button = Element((By.ID,'login'))
        self._username_textbox = Element((By.ID,'userName'))
        self._password_textbox = Element((By.ID, 'password'))
        self._error_message = Element((By.ID, 'name'))
    
    def login(self, account):
        self._username_textbox.enter(account.username)
        self._password_textbox.enter(account.password)
        self._login_button.click()
    
    def get_error_message(self):
        return self._error_message.get_text()