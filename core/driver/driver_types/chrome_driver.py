from core.driver.base_driver import BaseDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class ChromeDriver(BaseDriver):

    def create_driver(self, config):
        options = webdriver.ChromeOptions()
        print("in create_webdriver")
        for arg in config.arguments:
            options.add_argument(arg)

        for key, value in config.capabilities.items():
            options.set_capability(key, value)

        self._driver = webdriver.Chrome(service=Service(), options=options)
        return self
