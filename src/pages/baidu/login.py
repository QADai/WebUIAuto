# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
from home_page import *
from src.utils.log_util import log

class Login:
    _main_url = "https://www.baidu.com/"
    _login_enter = ("id","TANGRAM__PSP_10__footerULoginBtn")
    _login_link = ("link","登录")
    _username = ("id","TANGRAM__PSP_10__userName")
    _password = ("id", "TANGRAM__PSP_10__password")
    _login_submit = ("id","TANGRAM__PSP_10__submit")
    _logout_link = ("xpath", "//span[@class='user-name']")
    _login_user_display = ("id", "s_username_top")
    _logout = ("link", "退出")
    _logout_confirm = ("link", "确定")

    def __init__(self, browser='chrome'):
        self.driver = Webdriver_Opts(browser)
        self.browser = SeleniumDriver(self.driver.get_webdriver_instance())

    def click_element(self, element):
        self.browser.element_click(element[1], element[0])

    def input_key(self, element, data):
        self.browser.element_send_keys(element[1], data, element[0])

    def login(self, username, password):
        try:
            self.browser.open(self._main_url,"")
            self.click_element(self._login_link)
            self.click_element(self._login_enter)
            self.input_key(self._username, username)
            self.input_key(self._password, password)
            self.click_element(self._login_submit)
            if self.browser.element_is_present(username,"link"):
                log.info("登录成功")
            else:
                log.error("登陆失败")
        except Exception as e:
            log.error("没有进入登录界面,异常信息是："+ str(e))

    def logout(self):
        try:

            self.browser.move_element(self._login_user_display[1], self._login_user_display[0])
            sleep(2)
            self.click_element(self._logout)
            sleep(2)
            self.click_element(self._logout_confirm)
        except Exception as e:
            log.error("没有进入登录界面,异常信息是：" + str(e))


if __name__ =="__main__":
    y = Login()
    y.login()
    y.logout()



