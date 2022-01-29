from helpers.seleniumHelper import check_element_exsist_by_xpath, selenium_get_element_by_class, \
    wait_for_elemnet_visible
from setup import *


def test_ebay_high_low_proces():
    wait_for_elemnet_visible("page.elements.prices")
    element = selenium_get_element_by_class("page.price.element.class")
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
    logging.info("low price is " + str(sorted_prices[0]))
    logging.info("highest price is " + str(sorted_prices[-1]))