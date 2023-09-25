import pytest
from core.driver.driver_configuration import DriverConfig
from core.env_info.env_info import EnvironmentInfo

def pytest_addoption(parser):
    parser.addoption("--conf-file", action="store",
                     help="Driver configuration file. Default is resources/test_configuration/driver_conf.json",
                     metavar="")
    parser.addoption("--browser", action="store",
                     help="Browser Type. Default is chrome_local",
                     metavar="")
    parser.addoption("--test-env", action="store",
                     help="Test environment. Default is qa",
                     metavar="")
    
def pytest_configure(config):
    pytest.conf_file = config.getoption("--conf-file", "resources/test_configuration/driver_conf.json", True)
    pytest.browser = config.getoption("--browser", "chrome_local", True)
    pytest.test_env = config.getoption("--test-env", "staging", True)
    pytest.driver_conf = DriverConfig.get_driver_config(pytest.browser, pytest.conf_file)

@pytest.fixture(scope='session', autouse=True)
def get_environement_info():
    EnvironmentInfo.get_environment_info("resources/test_configuration/env_conf.json",pytest.test_env )

