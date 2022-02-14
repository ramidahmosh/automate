import logging

import pytest

from helpers.seleniumHelper import selenium_type, selenium_click, \
    selenium_get_elements_count_by_xpath, wait_for_elemnet_visible


def search_for_product(product_name):
    selenium_type(pytest.locator_config.get('Locators', 'ebay.search.textbox'), product_name)
    selenium_click(pytest.locator_config.get('Locators', 'ebay.home.search.button'))


def check_search_results_count():
    pytest.locator_config.get('Locators', 'ebay.search.result.elements')
    wait_for_elemnet_visible(pytest.locator_config.get('Locators', 'ebay.search.result.elements'))
    count = selenium_get_elements_count_by_xpath(pytest.locator_config.get('Locators', 'ebay.search.result.elements'))
    logging.info("search results count is " + str(count))
    assert count > 1