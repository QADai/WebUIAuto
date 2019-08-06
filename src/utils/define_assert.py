# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import sys
import time
import pytest
import pathlib
import allure
from src.utils.log_util import log
from configure.configure import *
from src.utils.take_screen import browser_instance
sys.path.append(r'.')
sys.path.append(r'../')
sys.path.append(r'../../')


def img_path():
    return os.path.join(screen_path, "Assure_Failed_" + time.strftime("%Y-%m-%d_%H_%M_%S") + ".png")


class Assertion_Failed(Exception):
    """Search keyword failed."""
    pass


class Assert:
    @classmethod
    def true(cls,value,img_path, browser_instance):
        try:
            assert value, "{}的值不是True".format(value)
        except Exception as msg:
            browser_instance.capture_screen(img_path)
            if pathlib.Path(img_path).exists():
                allure.attach("失败截图", open(img_path, "rb").read(), allure.attach_type.PNG)
            raise msg

    @classmethod
    def not_true(cls,value,img_path, browser_instance):
        try:
            assert not value, "{}的值是True".format(value)
        except Exception as msg:
            browser_instance.capture_screen(img_path)
            if pathlib.Path(img_path).exists():
                allure.attach("失败截图", open(img_path, "rb").read(), allure.attach_type.PNG)
            raise msg

    @classmethod
    def contain(cls, actual_value, expected_list, img_path, browser_instance):
        try:
            assert actual_value in expected_list,"{0}的值不在{1}中".format(actual_value, expected_list)
        except Exception as msg:
            browser_instance.capture_screen(img_path)
            if pathlib.Path(img_path).exists():
                allure.attach("失败截图", open(img_path, "rb").read(), allure.attach_type.PNG)
            raise msg

    @classmethod
    def equal(cls, actual, expect,img_path, browser_instance):
        try:
            assert actual == expect, "{0} 的值和{1}的值不相等".format(actual, expect)
        except Exception as msg:
            browser_instance.capture_screen(img_path)
            if pathlib.Path(img_path).exists():
                allure.attach("失败截图", open(img_path, "rb").read(), allure.attach_type.PNG)
            raise msg

    @classmethod
    def not_equal(cls, actual, expect,img_path, browser_instance):
        try:
            assert  actual != expect, "{0} 的值和{1}的值相等".format(actual, expect)
        except Exception as msg:
            browser_instance.capture_screen(img_path)
            if pathlib.Path(img_path).exists():
                allure.attach("失败截图", open(img_path, "rb").read(), allure.attach_type.PNG)
            raise msg



if __name__ == "__main__":
    Assert.not_equal(3,3)