from setup import *

from pytest_bdd import scenarios, scenario, when, given, then, parsers
from pytest_testrail.plugin import pytestrail

from helpers.seleniumHelper import selenium_click, check_element_exsist_by_xpath, selenium_type, \
    selenium_get_elements_by_xpath, selenuim_wait_loop, selenium_get_elements_count_by_xpath

from test.step_defs.search_engine.ebay_search_helper import search_for_product, check_search_results_count

scenarios('../../feature/ebay_search.feature')

@allure.description("""
open ebay site , \n
check that ebay site is open \n
search for product \n
check that there is more than one product \n 
""")
@scenario('../../feature/ebay_search.feature', "search for some keyword")
def test_search_for_some_keyword():
    pass


def setup_function(function):
    logging.info("setup function")


def teardown_function(function):
    logging.info("teardown function")


@given('browser is open on ebay website')
def check_browser_google_website():
    with allure.step('browser is open on ebay website'):
        check_element_exsist_by_xpath('ebay.logo')


# When Steps
@pytestrail.case('C1234', 'C5678')
@allure.issue('https://mycompamy.atlassian.net/browse/AAA-1679')
@when(parsers.parse('type a "{search_word}"'))
def type_keyword(search_word):
    with allure.step('type a ' + search_word):
        search_for_product(search_word)

@then('check there is more than one results')
def check_there_is_more_than_one_results():
    with allure.step('check there is more than one results'):
        check_search_results_count()



