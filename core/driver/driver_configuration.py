import json
from core.const import constants
from core.utilities.file_utils import get_full_path


class DriverConfig():

    @classmethod
    def get_driver_config(cls, browser, config_file):
        print(get_full_path(config_file))
        with open(get_full_path(config_file)) as f:
            data = json.load(f)
            item = data[browser]
            config = DriverConfig(browser,
                                  item[constants.REMOTE_HOST_KEY],
                                  item[constants.DRIVER_KEY],
                                  item[constants.CAPABILITIES_KEY],
                                  item[constants.ARGUMENTS_KEY])
        return config

    def __init__(self, driver_key, host, driver, capabilities, arguments):
        self._host = host
        self._driver = driver
        self._capabilities = capabilities
        self._arguments =  arguments

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, value):
        self._driver = value

    @property
    def capabilities(self):
        return self._capabilities

    @capabilities.setter
    def capabilities(self, value):
        self._capabilities = value
    
    @property
    def arguments(self):
        return self._arguments

    @arguments.setter
    def arguments(self, value):
        self.arguments = value

