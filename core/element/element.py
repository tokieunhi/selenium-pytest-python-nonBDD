from core.driver.driver_manager import DriverManager
from core.const.constants import SELENPY_DEFAULT_TIMEOUT
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.utilities.wait_utils import wait_until
class Element():

    def __init__(self, by):
        self._element = None
        self._driver = DriverManager.driver.get_webdriver()
        self._by = by
    
    def wait_for_presence(self, timeout=SELENPY_DEFAULT_TIMEOUT):
        self._element = WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located((self._by[0] , self._by[1])))

    def wait_for_visibility(self, timeout=SELENPY_DEFAULT_TIMEOUT):
        self._element = WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located((self._by[0] , self._by[1])))

    def wait_for_invisibility(self, timeout=SELENPY_DEFAULT_TIMEOUT):
        self._element = WebDriverWait(self._driver, timeout).until(EC.invisibility_of_element((self._by[0] , self._by[1])))
    
    def wait_for_clickable(self, timeout=SELENPY_DEFAULT_TIMEOUT):
        self._element = WebDriverWait(self._driver, timeout).until(EC.element_to_be_clickable((self._by[0] , self._by[1])))
    
    def wait_for_enable(self, timeout=SELENPY_DEFAULT_TIMEOUT):
        wait_until(lambda: self.is_enabled(),
                   "Element was not enabled in <TIMEOUT>.",
                   timeout)
    
    def wait_for_text_contains(self, text, timeout=None):
        wait_until(lambda: text in self.get_text(),
                   "Element did not get text '%s' in <TIMEOUT>." % (text),
                   timeout)

    def is_enabled(self):
        self.wait_for_visibility()
        return self._element.is_enabled()
    
    def is_displayed(self):
        self.wait_for_presence()
        return self.element.is_displayed()
    
    def is_selected(self):
        self.wait_for_visibility()
        return self._element.is_selected()
    
    def exist_in_dom(self):
        return len(self._driver.find_elements(self._by[0] , self._by[1])) > 0

    def get_tag_name(self):
        self.wait_for_visibility()
        return self._element.tag_name
    
    def get_text(self):
        self.wait_for_visibility()
        return self._element.text
    
    def get_attribute(self, name):
        self.wait_for_visibility()
        return self._element.get_attribute(name)
    
    def get_property(self, name):
        self.wait_for_visibility()
        return self._element.get_property(name)
    
    def get_location(self):
        self.wait_for_visibility()
        return self._element.location
    
    def scroll_into_view(self):
        self.wait_for_visibility()
        self._driver.execute_script("arguments[0].scrollIntoView();", self._element)

    def click(self):
        self.scroll_into_view()
        self.wait_for_clickable()
        self._element.click()

    def clear(self):
        self.wait_for_visibility()
        self._element.clear()

    def enter(self, content):
        self.scroll_into_view()
        self._element.click()
        self._element.clear()
        self._element.send_keys(content)
    
    def save_screenshot(self, path):
        self.wait_for_visibility()
        self._element.screenshot(path)




    
    