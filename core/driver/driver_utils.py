from core.driver.driver_manager import DriverManager
from core.utilities.wait_utils import wait_until
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.const.constants import SELENPY_DEFAULT_TIMEOUT

class DriverUtils():
    @classmethod
    def get_driver(cls):
        return DriverManager.driver.get_webdriver()

    @classmethod
    def get_title(cls):
        return cls.get_driver().title

    @classmethod
    def maximize_window(cls):
        cls.get_driver().maximize_window()

    @classmethod
    def close_browser(cls):
        cls.get_driver().close()

    @classmethod
    def open_url(cls, url):
        cls.get_driver().get(url)

    @classmethod
    def select_main_window(cls):
        handles = cls.get_driver().window_handles
        cls.get_driver().switch_to.window(handles[0])

    @classmethod
    def wait_for_title_contains(cls, value, timeout=None):    
        wait_until(lambda: value in cls.get_title(), "Title '%s' did not display after after <TIMEOUT>." % value, timeout)
    
    @classmethod
    def wait_for_alert(cls, timeout=SELENPY_DEFAULT_TIMEOUT):
        WebDriverWait(cls.get_driver(), timeout).until(EC.alert_is_present())
    
    @classmethod
    def accept_alert(cls):
        cls.wait_for_alert()
        alert = cls.get_driver().switch_to.alert
        alert.accept()

    @classmethod
    def save_screenshot(cls, file):
        """
            :Usage:
                selenium.save_screenshot('screenshots/example.png')
        """
        cls.get_driver().save_screenshot(file)
    
    @classmethod
    def save_screenshot_as_png(cls):
        cls.get_driver().get_screenshot_as_png()

