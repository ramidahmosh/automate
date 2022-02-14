import pytest
import logging
from helpers.seleniumHelper import selenium_click


def setup_function():
    logging.info("setup function , check test init state")
    check_home_page()


def teardown_function():
    logging.info("end test, go to site initial state ")
    selenium_click(pytest.locator_config.get('Locators', 'ebay.logo.link'))
    check_home_page()


def check_home_page():
    url = pytest.driver.current_url
    logging.info("current url is " + url)
    try:
        assert url == pytest.config_file.get("system", "url")
    except:
        logging.error("url should be : " + pytest.config_file.get("system", "url") + " instead we have " + url)

"""
def teardown_session():
    logging.info("end tests")
"""
