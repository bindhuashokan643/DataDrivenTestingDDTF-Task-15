import pytest
from selenium import webdriver
from config.config import BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()
