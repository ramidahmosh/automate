# !/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import logging
import os
import shutil
from datetime import datetime
from setup import *


screenShoot_file = "/screenShoot"


# read config file from command line
def pytest_addoption(parser):
    parser.addoption("--config_file", action="store", default="config_local.properties",
                     help="'--config_file' - select config file to download (common or jenkins)")


def pytest_configure(config):
    # read config file from command line , default to config_local.properties
    os.environ["config_file"] = config.getoption('--config_file')
    print("using config file = " + config.getoption('--config_file') + " \n")
    conf_file = os.environ["config_file"]
    pytest.config_file = configparser.RawConfigParser()
    pytest.config_file.read(conf_file)

    pytest.locator_config = configparser.RawConfigParser()
    pytest.locator_config.read('locators.properties')
    print("  ==>finish loading locator file ")

    report_dir = pytest.config_file.get("system", "report")
    report_dir_old = pytest.config_file.get("system", "logfileold")

    # init the report files
    if not os.path.isdir(report_dir):
        os.mkdir(report_dir)
        if not os.path.isdir(report_dir + screenShoot_file):
            os.mkdir(report_dir + screenShoot_file)
        return

    if not os.path.isdir(report_dir_old):
        os.mkdir(report_dir_old)

    shutil.move(report_dir+"/", report_dir_old+"/" + report_dir + "-" + str(datetime.today()))
    os.mkdir(report_dir)
    os.mkdir(report_dir + screenShoot_file)


class AllureLoggingHandler(logging.Handler):
    def log(self, message):
        with allure.step('Log {}'.format(message)):
            pass

    def emit(self, record):
        self.log("({}) {}".format(record.levelname, record.getMessage()))


class AllureCatchLogs:
    def __init__(self):
        self.rootlogger = logging.getLogger()
        self.allurehandler = AllureLoggingHandler()

    def __enter__(self):
        if self.allurehandler not in self.rootlogger.handlers:
            self.rootlogger.addHandler(self.allurehandler)

    def __exit__(self, exc_type, exc_value, traceback):
        self.rootlogger.removeHandler(self.allurehandler)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup():
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown():
    with AllureCatchLogs():
        yield
