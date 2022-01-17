from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure
import pytest
import logging


console_logger = logging.getLogger()
def setup_module():
    url = pytest.config_file.get("system", "url")
    browser_type = pytest.config_file.get("system", "browser")
    if browser_type == "Chrome":
        pytest.driver = webdriver.Chrome('webdriver_drivers/chromedriver_x64')
    elif browser_type == "firefox":
        pytest.driver = webdriver.Firefox(executable_path='webdriver_drivers/firefox')
    pytest.wait = WebDriverWait(pytest.driver, timeout=5, poll_frequency=0.3)
    pytest.driver.get(url)
    console_logger.info("start tests ---")



def teardown_module():
    console_logger.info("end tests ---")
    pytest.driver.close()


