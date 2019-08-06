# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
from src.base.browser import *
from src.base.browser_engine import *


class Home_Page:
    _main_url = "https://www.baidu.com/"
    _input_key = ("id", "kw")
    _btn_search = ("id", "su")

    def __init__(self, browser='chrome'):
        self.driver = Webdriver_Opts(browser)
        self.browser = SeleniumDriver(self.driver.get_webdriver_instance())

    def quit_browser(self):
        self.browser.kill()
        log.info("退出webdriver")

    def open_baidu_page(self):
        self.browser.open(self._main_url, "")

    def search(self, key_word):
        self.browser.element_send_keys(self._input_key[1], key_word, self._input_key[0])
        sleep(1)
        self.browser.element_click(self._btn_search[1], self._btn_search[0])
        sleep(2)

    def title(self):
        sleep(2)
        return self.browser.get_title()

    def open_link_news(self):
        self.browser.element_click("新闻", "link")

    def open_link_hao123(self):
        self.browser.element_click("hao123", "link")

    def open_link_map(self):
        self.browser.element_click("地图", "link")

    def open_link_video(self):
        self.browser.element_click("视频", "link")

    def open_link_tieba(self):
        self.browser.element_click("贴吧", "link")

    def open_link_academic(self):
        self.browser.element_click("学术", "link")

    def move_to_link(self, text_name, click_element):
        self.browser.move_element(text_name, "link")
        self.browser.element_click(click_element, "link")

    def move_to_setting_option(self, option):
        self.move_to_link("设置", option)

    def move_to_more_product(self, option):
        self.move_to_link("更多产品", option)


if __name__ == "__main__":
    x = Home_Page()
    x.open_baidu_page()
    # x.move_to_setting_option("高级搜索")
    sleep(3)
    # print(x.title())
    x.open_link_tieba()
    x.quit_browser()
