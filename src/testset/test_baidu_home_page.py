# -*- encoding: utf-8 -*-
import pytest
import allure
import sys
sys.path.append(r'../../')
sys.path.append(r'../')
sys.path.append(r'.')
from src.utils.allure_attach import *
from src.pages.baidu.home_page import Home_Page
from src.testset.data_resources import *
from src.utils.define_assert import *

class SearchError(Exception):
    """Search keyword failed."""
    pass


class Test_Home_Page:
    def setup_class(self):
        log.info("类 ---> 启动浏览器")
        self.HP = Home_Page(current_using_browser)
        self.HP.open_baidu_page()

    def teardown_class(self):
        log.info("类 ---> 退出浏览器")
        self.HP.quit_browser()

    @pytest.fixture()
    def open_home_page(self):
        self.HP.open_baidu_page()


    @pytest.mark.run(order=1)
    @allure.feature('查询功能')
    @allure.severity("blocker")
    @allure.story("对不同关键词进行搜索")
    # @allure.testcase("用例描述在结果的用例参数中！")
    @pytest.mark.parametrize("key_word, TC_title", get_search_data(Run_TC_Priority))#参数化，从excel表格中根据不同的优先级
    def test_search(self, key_word, TC_title):
        """
       从excel表格中提取搜索的关键词，搜索并且坚持标题中是否包含相应的字符串
       """
        paras = vars()
        allure.attach("用例参数", "{0}".format(paras))
        self.HP.search(key_word)
        title_text = self.HP.title()

        screen_shot_path = img_path()
        Assert.contain(key_word, title_text, screen_shot_path, self.HP.browser)
        attach(screen_shot_path)


    @allure.feature('检查超链接')
    @allure.story('新闻连接')
    @allure.severity("Critical")
    def test_enter_news(self, open_home_page):
        """
        验证新闻连接
        """
        self.HP.open_link_news()
        title_text = self.HP.title()

        screen_shot_path = img_path()
        Assert.contain("百度新闻", title_text, screen_shot_path, self.HP.browser)
        attach(screen_shot_path)


    @allure.feature('检查超链接')
    @allure.story('hao123连接')
    @allure.severity("Critical")
    def test_enter_hao123(self, open_home_page):
        """
        验证hao123连接
        """
        self.HP.open_link_hao123()
        title_text = self.HP.title()

        screen_shot_path = img_path()
        Assert.contain("百度新闻", title_text, screen_shot_path, self.HP.browser)
        attach(screen_shot_path)


    @allure.feature('检查超链接')
    @allure.story('地图链接')
    @allure.severity("Critical")
    def test_enter_map(self, open_home_page):
        """
        验证地图链接
        """
        self.HP.open_link_map()
        title_text = self.HP.title()

        screen_shot_path = img_path()
        Assert.contain("百度地图1", title_text, screen_shot_path, self.HP.browser)


    @allure.feature('检查超链接')
    @allure.story('视频链接')
    @allure.severity("Critical")
    def test_enter_video(self, open_home_page):
        """
        验证视频链接
        """
        self.HP.open_link_video()
        title_text = self.HP.title()

        screen_shot_path = img_path()
        Assert.contain("百度视频", title_text, screen_shot_path, self.HP.browser)
        attach(screen_shot_path)


    @allure.feature('检查超链接')
    @allure.story('贴吧链接')
    @allure.severity("Critical")
    def test_enter_tieba(self, open_home_page):
        """
        验证贴吧链接
        """
        self.HP.open_link_tieba()
        title_text = self.HP.title()

        screen_shot_path = img_path()
        Assert.contain("百度贴吧", title_text, screen_shot_path, self.HP.browser)
        attach(screen_shot_path)


    @allure.feature('检查超链接')
    @allure.story('学术链接')
    @allure.severity("Critical")
    def test_enter_academic(self, open_home_page):
        """
        验证学术链接
        """
        self.HP.open_link_academic()
        title_text = self.HP.title()

        screen_shot_path = img_path()
        Assert.contain("百度学术", title_text, screen_shot_path, self.HP.browser)
        attach(screen_shot_path)


    @allure.feature('页面设置')
    @allure.story('负向查询功能')
    @allure.severity("Normal")
    def test_open_settings(self):
        log.info("log页面设置 ")


if __name__ == '__main__':
    # 使用如下的语句不能执行成功，通过命令行执行的
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
