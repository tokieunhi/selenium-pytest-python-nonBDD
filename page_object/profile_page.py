from page_object.base_page import BasePage
from core.element.element import Element
from selenium.webdriver.common.by import By
from core.driver.driver_utils import DriverUtils


class ProfilePage(BasePage):
    def __init__(self):
        super().__init__()
        self._txt_email = Element((By.ID, 'email'))

    def delete_button(self, book_name):
        delete_button_xpath = '//span[ .=\'%s\']/ancestor::div[@role=\'row\']//span[@title=\'Delete\']' % book_name
        return Element((By.XPATH, delete_button_xpath))

    def delete_book_by_name(self, book_name):
        self.delete_button(book_name).click()
        self.ok_button.click()
        DriverUtils.accept_alert()

    def navigate_to_profile_page(self):
        self.wait_for_loading()
        DriverUtils.open_url("https://www.staging.theout.com/profile")
        # self.navigate()

    def is_email_displayed(self):
        self.navigate_to_profile_page()
        self._txt_email.is_displayed()
