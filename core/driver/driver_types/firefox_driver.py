from core.driver.base_driver import BaseDriver
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service


class FirefoxDriver(BaseDriver):

    def create_driver(self, config):
        options = webdriver.FirefoxOptions()
        for arg in config.arguments:
            options.add_argument(arg)

        for key, value in config.capabilities.items():
            options.set_capability(key, value)

        self._driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                                         options=options)
        return self
