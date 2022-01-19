import logging

from helpers.seleniumHelper import selenium_type, selenium_click, selenuim_wait_loop, \
    selenium_get_elements_count_by_xpath


def search_for_product(product_name):
    selenium_type('ebay.search.textbox', product_name)
    selenium_click('ebay.home.search.button')


def check_search_results_count():
    selenuim_wait_loop('ebay.search.result.elements')
    elements = selenium_get_elements_count_by_xpath('ebay.search.result.elements')
    count = len(elements)
    logging.info(("search results count is ") + str(count))
    assert count > 1