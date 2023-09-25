from core.element.element import Element
from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self):
        super().__init__()
        self._loading_spinner = Element((By.XPATH, "//omg[contains(@class, 'usePageLoading')]"))
        self._about_us_menu_item = Element((By.XPATH, "//a[text()='About us']"))
        self._whats_included_menu_item = Element((By.XPATH, "//a[text()='WHAT'S INCLUDED']"))
        self._our_cars_menu_item = Element((By.XPATH, "//a[text()='Our cars']"))
        self._the_journal_menu_item = Element((By.XPATH, "//a[text()='The Journal']"))
        self._download_menu_item = Element((By.XPATH, "//a[text()='Download']"))
        self._login_menu_item = Element((By.ID, "user-widget-2"))
        self._account_menu_item = Element((By.ID, "user-widget-2"))

    def wait_for_loading(self):
        self._loading_spinner.wait_for_invisibility()
        self._account_menu_item.wait_for_visibility()

    def go_to_login_form(self):
        self._login_menu_item.click()

    def get_error_message(self):
        return self._error_message.get_text()


