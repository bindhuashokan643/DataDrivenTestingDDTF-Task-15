import pytest
from pages.login_page import LoginPage
from utilities.excel_utils import get_test_data, update_result
from utilities.logger import setup_logger
from utilities.screenshot import take_screenshot
from config.config import EXCEL_PATH

logger = setup_logger()

@pytest.mark.parametrize("testid,username,password,tester", get_test_data(EXCEL_PATH))
def test_login(driver, testid, username, password, tester):
    page = LoginPage(driver)
    logger.info(f"Running test {testid} with user {username}")
    page.login(username, password)
    result = "Passed" if page.is_login_successful() else "Failed"
    update_result(EXCEL_PATH, testid, result)
    if result == "Failed":
        take_screenshot(driver, testid)
    logger.info(f"Test {testid} result: {result}")
    assert result == "Passed"
