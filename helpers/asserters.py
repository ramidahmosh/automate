import logging
import unittest

import allure
import pytest_check as check

from helpers.seleniumHelper import selenuim_take_screenshoot


def check_is_in(elm1, elm2, msg):
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
        check.not_equal(elm1, elm2)
    except:
        check.not_equal(elm1, elm2)  # , "comparing between given " + str(elm1) + "barcode and expected  " + str(elm2))


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