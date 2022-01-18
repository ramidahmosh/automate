import time
from datetime import datetime
import logging
import unittest

import pytest_check
import pytest_check as check
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from setup import *
pytest_check.check_methods.set_stop_on_fail(False)


def check_elemnet_visible(elm):
    pytest.wait.until(EC.visibility_of_element_located((By.XPATH, pytest.locator_config.get('Locators', elm))))


def check_element_exsist_by_xpath(elm):
    try:
        logging.info("check if element " + elm + " exist")
        check_elemnet_visible(elm)
        return True
    except:
        logging.error("did not find  element " + elm )
        allure.attach("check element exist in gui ", "did not find it  " + elm)
        return False


def selenuim_take_screenshoot(name):
    allure.attach(pytest.driver.get_screenshot_as_png(), name + str(datetime.now()), attachment_type=allure.attachment_type.PNG)


def selenium_click(elm):
    try:
        logging.info("find and click on element " + elm)
        check_elemnet_visible(elm)
        pytest.driver.find_element_by_xpath(pytest.locator_config.get('Locators', elm)).click()

    except NoSuchElementException:
        allure.attach("selenium logging", "no such element " + elm + " cannot click on it !!")
        selenuim_take_screenshoot(elm)


def selenium_type(elm,str):
    try:
        logging.info("find and type " + str + " on element " + elm)
        check_elemnet_visible(elm)
        pytest.driver.find_element_by_xpath(pytest.locator_config.get('Locators', elm)).send_keys(str)

    except NoSuchElementException:
        allure.attach("selenium logging", "no such element " + elm + " cannot type on it !!")
        selenuim_take_screenshoot(elm)

def selenium_get_elements_by_xpath(elm):
    try:
        logging.info("get element " +elm + " by xpath")
        check_elemnet_visible(elm)
        return pytest.driver.find_element_by_xpath(elm)

    except NoSuchElementException:
        allure.attach("selenium logging", "no such element " + elm + " cannot type on it !!")
        selenuim_take_screenshoot(elm)


def selenium_get_element_text(elm):
    try:
        check_elemnet_visible(elm)
        text = pytest.driver.find_element_by_xpath(pytest.locator_config.get('Locators', elm)).text
        logging.info("element text is " + text)
        return text
    except NoSuchElementException:
        allure.attach("selenium logging", "no such element " + elm)
        selenuim_take_screenshoot(elm)
        return "did not see it"

def selenium_get_element_by_class(class_name):
    try:
        pytest.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, pytest.locator_config.get('Locators', class_name))))
        elements = pytest.driver.find_elements_by_class_name(pytest.locator_config.get('Locators', class_name))
        #logging.info("element text is " + text)
        return elements
    except NoSuchElementException:
        allure.attach("selenium logging", "no such element class" + class_name)
        selenuim_take_screenshoot(class_name)
        return "did not see it"

def check_is_in(elm1,elm2,msg):
    try:
        Checker().check_is_in(elm1, elm2, msg)
    except:
        check.is_in(elm1, elm2)  # , "is " + elm1 + " in " + elm2 + " has Fail check !!!!!!!")


def check_values(elm1, elm2, msg):
    try:
        Checker().check_values(elm1, elm2, msg)
    except:
        check.equal(elm1, elm2)  # , "comparing between given " + str(elm1) + "barcode and expected  " + str(elm2))


def check_values_not_empty(elm1, elm2, msg):
    try:
        Checker().check_values(elm1, elm2, msg)
    except:
        check.not_equal(elm1, elm2)  # , "comparing between given " + str(elm1) + "barcode and expected  " + str(elm2))


def click_Esc_keyborad():
    webdriver.ActionChains(pytest.driver).send_keys(Keys.ESCAPE).perform()


def selenuim_wait_loop(elm):
    for i in range(0, 5):
        if check_element_exsist_by_xpath_delete_me(elm):
            logging.info("found the element " + elm + " after " + str(i)+ " retries")
            time.sleep(1)
            return
    logging.info("did not find the element " + elm + " after 5 retries")


def check_element_exsist_by_xpath_delete_me(elm):
    try:
        logging.info("check if element " + elm + " exist")
        pytest.wait.until(
            (EC.visibility_of_element_located((By.XPATH, pytest.locator_config.get('Locators', elm)))) )
        return True
    except:
        logging.info("did not find  element " + elm )
        allure.attach("check element exist in gui ", "did not find it  " + elm)
        return False


def refresh_page():
    url = pytest.driver.current_url
    if url.find(":90") == -1:
        logging.info(" refresh shopping ui")
        # we are not in admin mode , it's shopping mode
        pytest.driver.refresh()
    else:
        # we are in admin mode
        logging.info(" refresh admin mode ui")
        pytest.driver.get("http://localhost")



class Checker(unittest.TestCase):
    def check_values(self, elm1, elm2, msg):
        with self.subTest("check-equal the values " + elm1 + " with " + elm2):
            with allure.step("check-equal the values " + elm1 + " with " + elm2):
                try:
                    self.assertEqual(elm1, elm2)
                    logging.info("compare between " + elm1 + "  == " + elm2 + " == > passed")
                    logging.info(msg)
                except:
                    logging.error(msg)
                    selenuim_take_screenshoot("check_equal_values failure")
                    raise

    def check_is_in(self, elm1, elm2, msg):
        with self.subTest("check-is-in value " + elm1 + " in " + elm2):
            with allure.step("check-is-in value " + elm1 + " in " + elm2):
                try:
                    self.assertIn(elm1, elm2)
                    logging.info(" value " + elm1 + "  is in  " + elm2 + "  ==> passed")
                    logging.info(msg)
                except:
                    logging.error(msg)
                    selenuim_take_screenshoot("check-is-in failure")
                    raise


