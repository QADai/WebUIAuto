# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import pytest
import sys
from datetime import datetime
sys.path.append(r'../../')
from configure.configure import *
from src.base.browser import *
from src.base.browser_engine import *

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            dirpng = screen_path
            if os.path.exists(dirpng) and os.path.isdir(dirpng):
                pass
            else:
                os.mkdir(dirpng)
            i = datetime.now()
            screen_name = str(i.year) + str(i.month) + str(i.day) + str(i.hour) + str(i.minute) + str(i.second)

            file_name = dirpng + report.nodeid.replace("::", "_") + screen_name +".png"
            file_name1 = r'./png/' + report.nodeid.replace("::", "_") + screen_name + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'οnclick="window.open(this.src)" align="right"/></div>' % file_name1
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


def _capture_screenshot(name):
    driver = Webdriver_Opts(current_using_browser)
    browser = SeleniumDriver(driver.get_webdriver_instance())
    browser.capture_screen(name)


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = Webdriver_Opts(current_using_browser)
    return driver
