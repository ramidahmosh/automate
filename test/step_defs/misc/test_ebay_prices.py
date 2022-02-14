import allure
from pytest_bdd import scenarios, scenario, given, when, then

from helpers.seleniumHelper import check_element_exsist_by_xpath, selenium_get_element_by_class, \
    wait_for_elemnet_visible
from setup import *

scenarios('../../feature/ebay_prices.feature')


@pytest.fixture(scope='function')
def context():
    return {}


@allure.description("""
browser is open on ebay website , \n
get highest and lowest price \n
print them \n
""")
@scenario('../../feature/ebay_prices.feature', "search for prices range")
def test_search_for_prices_range():
    pass


@given('browser is open on ebay website')
def check_browser_google_website():
    with allure.step('browser is open on ebay website'):
        check_element_exsist_by_xpath(pytest.locator_config.get('Locators', 'ebay.logo'))


@when('get highest and lowest price')
def test_ebay_high_low_proces(context):
    with allure.step('check ebay high low prices in main page'):
        wait_for_elemnet_visible(pytest.locator_config.get('Locators',"page.elements.prices"))
        element = selenium_get_element_by_class(pytest.locator_config.get('Locators',"page.price.element.class"))
        prices = []
        for i in element:
            # check if the price with pattern currency , cost
            if len(i.text.split(" ")) == 2:
                ils, cost = i.text.split(" ")
            else:
                if i.text.isnumeric():
                    cost = i.text()
            prices.append(float(cost.replace(",", "")))

        sorted_prices = sorted(prices, key=float)
        context['highest'] = str(sorted_prices[0])
        context['lowest'] = str(sorted_prices[-1])
        return context


@then('print them')
def print_results(context):
    with allure.step('print high low prices'):
        logging.info("low price is " + context['highest'])
        logging.info("highest price is " + context['lowest'])