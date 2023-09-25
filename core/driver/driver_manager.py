from core.driver.driver_types.chrome_driver import ChromeDriver
from core.driver.driver_types.firefox_driver import FirefoxDriver
from core.driver.driver_types.remote_driver import RemoteDriver

class DriverManager():
    driver = None

    @classmethod 
    def init_driver(cls, config):
        driver_mapping = {
            "chrome": ChromeDriver(),
            "firefox": FirefoxDriver(),
            "remote": RemoteDriver()
        }

        cls.driver = driver_mapping[config.driver].create_driver(config)
    
    @classmethod
    def quit_driver(cls):
        cls.driver.quit()