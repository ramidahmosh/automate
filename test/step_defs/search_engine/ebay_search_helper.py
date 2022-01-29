import logging

from helpers.seleniumHelper import selenium_type, selenium_click, \
    selenium_get_elements_count_by_xpath, wait_for_elemnet_visible


def search_for_product(product_name):
    selenium_type('ebay.search.textbox', product_name)
    selenium_click('ebay.home.search.button')


def check_search_results_count():
    wait_for_elemnet_visible('ebay.search.result.elements')
    elements = selenium_get_elements_count_by_xpath('ebay.search.result.elements')
    count = len(elements)
    logging.info("search results count is " + str(count))
    assert count > 1