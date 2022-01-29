from selenium import webdriver
import allure
import pytest
import logging
import pytest_bdd

#firefox_driver = 'webdriver_drivers/firefox'
#chrome_driver = 'webdriver_drivers/chromedriver_x64'
from helpers.seleniumHelper import selenium_click


@pytest.fixture(scope="session", autouse=True)
def setup_module():
    url = pytest.driver.current_url
    logging.info("current url is " + url)
    try:
        assert url == pytest.config_file.get("system", "url")
    except :
        logging.error("url should be :" + "https://www.ebay.com/" +" instead we have " + url)

    #url = pytest.config_file.get("system", "url")
    #browser_type = pytest.config_file.get("system", "browser")
    #browser_driver_path = pytest.config_file.get("system", "driver_path")
    #if browser_type == "Chrome":
    #    pytest.driver = webdriver.Chrome(browser_driver_path)
    #elif browser_type == "firefox":
    #    pytest.driver = webdriver.Firefox(executable_path=browser_driver_path)
    #explicit wait
    #pytest.wait = WebDriverWait(pytest.driver, timeout=10, poll_frequency=1)

    #pytest.driver.implicitly_wait(5)

    #pytest.driver.get(url)
    #logging.info("start tests ---")


def teardown_module():
    logging.info("end tests --- , go to site initial state ")
    selenium_click("ebay.logo.link")
    #pytest.driver.close()


