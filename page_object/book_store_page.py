from core.element.element import Element
from selenium.webdriver.common.by import By
from .base_page import BasePage

class BookStorePage(BasePage):
    def __init__(self):
        super().__init__()
        self._login_button = Element((By.ID,'login'))
    
    def book_link(self, book_name):
        book_link_xpath = '//a[.=\'%s\']' % book_name
        return Element((By.XPATH, book_link_xpath))
    
    def go_to_login_page(self):
        self._login_button.click()
    
    def wait_for_page_load(self):
        self._username_label.wait_for_visibility()