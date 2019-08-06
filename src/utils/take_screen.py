# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import sys
import time
from src.utils.log_util import log
from functools import wraps
from configure.configure import *
from src.base.browser import *
from src.base.browser_engine import *

sys.path.append(r'.')


def browser_instance():
    driver = Webdriver_Opts(current_using_browser)
    browser = SeleniumDriver(driver.get_webdriver_instance())
    return browser


def take_screenshot(img_path):
    def deco_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                # 1/0
            except Exception as msg:
                # browser_instance().capture_screen(img_path)
                print(img_path)
                raise msg
            else:
                log.info(" %s 脚本运行正常" % (func.__name__))

        return wrapper

    return deco_func
