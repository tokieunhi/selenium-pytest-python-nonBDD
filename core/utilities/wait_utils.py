import time
from selenium.common.exceptions import StaleElementReferenceException
from core.const.constants import SELENPY_DEFAULT_TIMEOUT

def wait_until(condition, error=None, timeout=SELENPY_DEFAULT_TIMEOUT, polling=0.2):
    max_time = time.time() + timeout
    not_found = None
    while time.time() < max_time:
        try:
            if condition():
                return
        except StaleElementReferenceException as err:
            not_found = err
        else:
            not_found = None
        time.sleep(polling)
    raise RuntimeError(not_found or error)