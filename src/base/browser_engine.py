# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions

from src.utils.log_util import log
from configure.configure import *

class Webdriver_Opts(object):

    def __init__(self, browser, headless=False):
        '''browser parameters： chrome firefox remote_firefox remote_chrome ie edge safari'''
        self.browser = browser
        self.headless = headless

    def get_webdriver_instance(self):
        """
        返回webdriver实例
        """
        if self.browser == 'chrome':
            if self.headless is True:
                chrome_option = ChromeOptions()
                chrome_option.add_argument('--headless')
                driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_option)
            else:
                driver = webdriver.Chrome(executable_path=chrome_driver_path)

        elif self.browser == 'firefox':
            if self.headless is True:
                firefox_options = FirefoxOptions()
                firefox_options.set_headless()
                driver = webdriver.Firefox(options=firefox_options, executable_path=firfox_driver_path)
            else:
                driver = webdriver.Firefox(executable_path=firfox_driver_path)

        elif self.browser == 'remote_firefox':
                driver = webdriver.Remote(command_executor='http://' + '1' + ':4444/wd/hub',
                                          desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True, })

        elif self.browser == 'remote_chrome':
                driver = webdriver.Remote(command_executor='http://' + '2' + ':4444/wd/hub',
                                          desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True, })
        elif self.browser == 'ie':
            ie_options = IEOptions()
            driver = webdriver.Ie(ie_options = ie_options, executable_path= ie_driver_path)
        elif self.browser == 'edge':
            driver = webdriver.Edge()
        elif self.browser == 'safari':
            driver = webdriver.Safari()
        else:
            driver = None

        if self.browser not in ['chrome', 'firefox', 'remote_firefox', 'remote_chrome', 'ie', 'edge', 'safari']:
            log.info('Driver "%s" is not defined' % self.browser)
        else:
            log.info('Driver is set as for browser "%s". Headless is %s' % (self.browser, self.headless))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(load_page_timeout)
        return driver
