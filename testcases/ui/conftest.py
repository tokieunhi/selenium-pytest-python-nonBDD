from core.driver.driver_manager import DriverManager
from core.driver.driver_utils import DriverUtils
from core.env_info.env_info import EnvironmentInfo
from core.utilities.file_utils import generate_screenshot_file_name
from allure_commons.types import AttachmentType
import allure
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if call.when == "call":
        if report.failed:
            screenshot_path = generate_screenshot_file_name()
            DriverUtils.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, attachment_type=AttachmentType.PNG)
           
@pytest.fixture(scope="function", autouse= True)
def setup_driver():
    DriverManager.init_driver(pytest.driver_conf)
    DriverUtils.maximize_window()
    DriverUtils.open_url(EnvironmentInfo.application_url)

    # Close all browsers when tests have been finished
    yield
    DriverManager.quit_driver()