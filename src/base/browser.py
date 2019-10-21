# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import os
import collections
from time import sleep
from datetime import datetime
from traceback import print_stack

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from src.utils.log_util import log
from configure.configure import *


class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    def take_screen(self, resultMessage):
        """
        当测试失败的时候截图
        :param resultMessage: 测试结果信息
        """
        i = datetime.now()
        folder_name = str(i.year) + str(i.month) + str(i.day)
        screen_name = str(i.year) + str(i.month) + str(i.day) + str(i.hour) + str(i.minute) + str(i.second)

        dir_name = os.path.join(screen_path, folder_name)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        file_name = resultMessage + "_" + screen_name + ".png"
        destination = os.path.join(dir_name, file_name)
        self.driver.save_screenshot(destination)

    def capture_screen(self,img_path):
        """
        当测试失败的时候截图
        :param img_path: 完整路径
        """
        self.driver.save_screenshot(img_path)

    def get_by_type(self, locator_type):
        """
        返回查找位置的类型
        :param locator_type: str set by def which implement on SeleniumDriver class
        :return: tag type or False
        """
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        elif locator_type == 'partial_link':
            return By.PARTIAL_LINK_TEXT
        elif locator_type == 'tag':
            return By.TAG_NAME
        elif locator_type == 'text' or locator_type == 'partial_text':
            return By.XPATH
        else:
            log.info("Locator type" + locator_type + " not correct/supported")
            return False

    def open(self, test_server1_url, uri=''):
        """
        打开浏览器
        """
        self.driver.get(test_server1_url + uri)
        log.info('Open page with url %s' % test_server1_url + uri)

    def element_get(self, locator, locator_type='id', parent_element=None):
        """
        通过dom的方式查找单个元素
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param parent_element: parent_element 父节点
        :return: WebElement
        """
        element = parent_element
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            if locator_type == 'text':
                locator = '//*[text()="' + locator + '"]'
            elif locator_type == 'partial_text':
                locator = '//*[contains(text(),"' + locator + '"]'
            if element:
                element = parent_element.find_element(by_type, locator)
                log.info("child element is Found with locator: " + locator + " locator_type " + locator_type)
            else:
                element = self.driver.find_element(by_type, locator)
                log.info("Element Found with locator: " + locator + " locator_type " + locator_type)
        except:
            log.error("Element not found")
        return element

    def elements_get(self, locator, locator_type='id'):
        """
        通过dom的方式查找所有元素
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :return: WebElement array[]
        """
        elements = None
        try:
            locator_type = locator_type.lower()
            if locator_type == 'text':
                locator = '//*[text()="' + locator + '"]'
            elif locator_type == 'partial_text':
                locator = '//*[contains(text(),"' + locator + '"]'
            by_type = self.get_by_type(locator_type)

            elements = self.driver.find_elements(by_type, locator)
            log.info("Elements Found")
        except:
            log.info("Elements not found")
        return elements

    def element_attribute(self, attr_name, locator='', locator_type='id', element=None):
        """
        查找并且返回属性值
        :param attr_name: str from page class ex LoginPage
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param element: WebElement returned by method ex element_get
        :return: str attribute value
        """
        name = None
        if element is not None:
            try:
                name = element.get_attribute(attr_name)
                log.info("Element Found with attribute %s" % attr_name)
            except:
                log.info("Element Not Found with attribute %s" % attr_name)
        else:
            try:
                locator_type = locator_type.lower()
                if locator_type == 'text':
                    locator = '//*[text()="' + locator + '"]'
                elif locator_type == 'partial_text':
                    locator = '//*[contains(text(),"' + locator + '"]'
                by_type = self.get_by_type(locator_type)
                result = self.driver.find_element(by_type, locator)
                name = result.get_attribute(attr_name)
                log.info("Elements Found")
            except:
                log.info("Elements not found")
        return name

    def elements_get_in_dict(self, locator, locator_type='id'):
        """
        在dom树形结构中查找所有元素
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :return: WebElement dict{}
        """
        elements = {}
        try:
            if locator_type == 'text':
                locator = '//*[text()="' + locator + '"]'
            elif locator_type == 'partial_text':
                locator = '//*[contains(text(),"' + locator + '"]'
            by_type = self.get_by_type(locator_type.lower())
            elements = {element.get_attribute('href'): element for element in self.driver.find_elements(by_type, locator)}
        except:
            log.info('Elements not found')
        return elements

    def element_click(self, locator='', locator_type='id', web_element=None):
        """
        点击元素
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param web_element: WebElement returned by method ex element_get
        :return:
        """
        try:
            if web_element:
                web_element.click()
                log.info("Clicked on element")
            else:
                element = self.element_get(locator, locator_type)
                element.click()
                log.info("Clicked on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            log.info("Cannot click on the element with locator: " + locator + " locator_type: " + locator_type)


    def element_right_click(self, locator='', locator_type='id', web_element=None):
        """
        右键点击
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param web_element: WebElement returned by method ex element_get
        :return:
        """
        try:
            if web_element:
                ActionChains(self.driver).context_click(web_element).perform()
                log.info("Right clicked element with locator: " + locator + " locator_type: " + locator_type)
            else:
                web_element = self.element_get(locator, locator_type)
                ActionChains(self.driver).context_click(web_element).perform()
                log.info("Right clicked element with locator: " + locator + " locator_type: " + locator_type)
        except:
            log.info("Cannot click on the element with locator: " + locator + " locator_type: " + locator_type)


    def element_send_keys(self, locator, data, locator_type='id', element=None):
        """
        将值传入对应的组件
        :param locator: str from page class ex LoginPage
        :param data: value which send
        :param locator_type: str from page class ex LoginPage
        :param element: WebElement returned by method ex element_get
        :return:
        """
        try:
            if element is not None:
                element.clear()
                element.send_keys(data)
            else:
                element = self.element_get(locator, locator_type)
                element.clear()
                element.send_keys(data)
            log.info("Send data on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            log.info("Cannot send data on the element with locator: " + locator + " locator_type: " + locator_type)


    def elements_send_keys(self, locator=None, **kwargs):
        """
        依次将同样类型的值传给对应的组件
        :param locator: str from page class ex LoginPage
        :param kwargs: dict with path of locator and value
        :return: None
        """
        try:
            val = collections.OrderedDict(reversed(list(locals().items())))
            val.pop('self')
            val.pop('locator')
            for name_loc, data in val['kwargs'].items():
                self.element_send_keys(
                    locator=locator.replace('setting', name_loc),
                    locator_type='xpath', data=data)
        except:
            log.info("Send data on element with locator: "
                          + locator.replace('setting', kwargs) + " locator_type: xpath")

    def element_is_present(self, locator, locator_type='id'):
        """
        检查dom中是否存在元素
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :return: bool
        """
        try:
            if locator_type == 'text':
                locator = '//*[text()="' + locator + '"]'
            elif locator_type == 'partial_text':
                locator = '//*[contains(text(),"' + locator + '"]'
            element = self.element_wait_for(locator, locator_type)
            # element = self.element_get(locator, locator_type)
            if element is not None:
                return True
            else:
                log.info("Element not found")
                return False
        except:
            log.info("Element not found")
            return False

    def element_presence_check(self, locator, locator_type='id'):
        """
        查看web元素是否存在
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :return: bool
        """
        try:
            if locator_type == 'text':
                locator = '//*[text()="' + locator + '"]'
            elif locator_type == 'partial_text':
                locator = '//*[contains(text(),"' + locator + '"]'
            self.element_wait_for(locator, locator_type)
            elementList = self.elements_get(locator, locator_type)
            if len(elementList) > 0:
                log.info("Element is found")
                return True
            else:
                log.info("Element not found")
                return False
        except:
            log.info("Element not found")
            return False

    def element_wait_for(self, locator, locator_type='id', timeout=10, poll_frequency=0.5):
        """
        等到可以点击的元素出现
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param timeout: int timeout
        :param poll_frequency: int query per second to element
        :return: WebElement
        """
        element = None
        try:
            if locator_type == 'text':
                locator = '//*[text()="' + locator + '"]'
            elif locator_type == 'partial_text':
                locator = '//*[contains(text(),"' + locator + '"]'
            by_type = self.get_by_type(locator_type)
            log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            log.info("Element appeared on the web page")
        except:
            log.info("Element not appeared on the web page")
            print_stack()
        return element

    def element_visibility_wait_for(self, locator, locator_type='id', timeout=10, poll_frequency=0.5):
        """
        等到可见的元素出现
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param timeout: int timeout
        :param poll_frequency: int query per second to element
        :return: WebElement
        """
        element = None
        try:
            if locator_type == 'text':
                locator = '//*[text()="' + locator + '"]'
            elif locator_type == 'partial_text':
                locator = '//*[contains(text(),"' + locator + '"]'
            by_type = self.get_by_type(locator_type)
            log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            log.info("Element appeared on the web page")
        except:
            log.info("Element not appeared on the web page")
            print_stack()
        return element

    def element_is_displayed(self, locator="", locator_type="id", element=None):
        """
        检查元素出现，并且没有被隐藏
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param element: WebElement returned by method ex element_get
        :return: bool
        """
        is_displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.element_get(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                log.info("Element is displayed")
            else:
                log.info("Element not displayed")
            return is_displayed
        except:
            print("Element not found")
            return False

    def element_is_clickable(self, locator, locator_type='id', timeout=20, poll_frequency=0.5):
        """
        检查元素是否可以点击
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param timeout: int timeout
        :param poll_frequency: int query per second to element
        :return: WebElement
        """
        element = None
        try:
            if locator_type == 'text':
                locator = '//*[text()="' + locator + '"]'
            elif locator_type == 'partial_text':
                locator = '//*[contains(text(),"' + locator + '"]'
            by_type = self.get_by_type(locator_type)
            log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementClickInterceptedException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            log.info("Element is ready for click")
        except:
            log.info("Element is not clickable")
            print_stack()
        return element

    def element_get_text(self, locator="", locator_type="", element=None, info=""):
        """
        返回元素文本
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param element: WebElement returned by method ex element_get
        :param info:
        :return: str
        """
        try:
            if locator:
                element = self.element_get(locator, locator_type)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute('InnerText')
            if len(text) != 0:
                log.info("Getting text on element :: " + info)
                log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def get_url(self):
        """
        返回当前web页面的url
        :return: str
        """
        current_url = None
        try:
            current_url = self.driver.current_url
            log.info('Current URL is :: ' + current_url)
        except:
            log.error('Failed to get current URL ' + current_url)
            print_stack()
        return current_url

    def get_title(self):
        """
        得到当前页面的标题
        :return: WebElement
        """
        title = None
        try:
            title = self.driver.title
            log.info('Current title is :: ' + title)
        except:
            log.error('Failed to get title ' + title)
            print_stack()
        return title

    def open_new_tab(self, locator="", locator_type="id", timeout=10):
        """
        打开一个新的页面
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param timeout: int timeout
        :return: int open tabs count
        """
        handles_before = self.driver.window_handles
        self.element_click(locator=locator, locator_type=locator_type)
        handles_after = None
        try:
            WebDriverWait(self, timeout).until(lambda windows: len(handles_before) != len(self.driver.window_handles))
            handles_after = self.driver.window_handles
            log.info('New window is opened :: ' + self.get_title())
            return handles_after
        except:
            log.error('No new window opened')
        return handles_after

    def switch_window(self, window_number):
        """
        跳转到另外的窗口, 切换浏览器handle, 切换不同的tab页 方法：driver.switch_to.window(window_name)
        # 备注：从A页跳转到B页，句柄已经切换过去，但是焦点没有切过去，所以需要switch_to.window，把焦点也切过去，才可以在当前页进行操作。
        # 切换是思路，获取所有的句柄，因为返回是一个list，
        # 而且要切换的对象都是最后一个，可以使用[-1]直接切过去 # 例如： driver.switch_to.window(driver.window_handles[-1])
        :param window_number: int window tab number
        :return: bool
        """
        try:
            self.driver.switch_to_window(self.driver.window_handles[window_number])
            log.info('Switched on new windows :: ' + self.get_title())
            return True
        except:
            log.error('Can`t switched to the window :: ' + str(window_number))
            return False



    def element_clear(self, locator, locator_type='id'):
        """
        清除元素的值
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :return: None
        """
        try:
            element = self.element_get(locator, locator_type)
            element.clear()
            log.info("Cleared on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            log.info("Cannot clear on the element with locator: " + locator + " locator_type: " + locator_type)

    def element_clear_by_keys(self, locator, locator_type='id', attribute='value'):
        """
        通过sending Keys_BACKSPACE的方式清空域值
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param attribute: attribute by which determines how much keys sending
        :return: None
        """
        try:
            element = self.element_get(locator, locator_type)
            value = element.get_attribute(attribute)
            for i in range(len(value)):
                element.send_keys(Keys.BACKSPACE)
            log.info("Cleared on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            log.info("Cannot clear on the element with locator: " + locator + " locator_type: " + locator_type)

    def elements_clear(self, locator=None, attribute='value', **kwargs):
        """
        循环的清除所有元素的值
        :param locator: str from page class ex LoginPage
        :param attribute: see element_clear_by_keys func
        :param kwargs: dict with path of locator and value
        :return: None
        """
        try:
            val = collections.OrderedDict(reversed(list(locals().items())))
            val.pop('self')
            val.pop('locator')
            for name_loc, data in val['kwargs'].items():
                if data is True:
                    self.element_clear_by_keys(
                        locator=locator.replace('setting', name_loc),
                        locator_type='xpath', attribute=attribute)
        except:
            log.info("Cannot clear on the element with locator: " + locator.replace('setting', kwargs) + " locator_type: xpath")

    def make_maxwindow(self):
        # 最大化浏览器
        self.driver.maximize_window()

    def set_winsize(self, wide, hight):
        """
        设置窗口
        :param wide:
        :param hight:
        :return:
        """
        self.driver.set_window_size(wide, hight)

    def move_element(self, locator, locator_type='id'):
        # 移动到
        self.element_presence_check(locator, locator_type)
        element = self.element_get(locator, locator_type)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, locator, locator_type='id'):
        # 双击
        self.element_presence_check(locator, locator_type)
        element = self.element_get(locator, locator_type)
        ActionChains(self.driver).double_click(element).perform()

    def drag_and_drop(self, fangfa1, e1, fangfa2, e2):
        # 从e1到e2
        if self.element_is_displayed(element=e1) and self.element_is_displayed(e2):
            ActionChains(self.driver).drag_and_drop(e1, e2).perform()

    def close(self):
        # 关闭
        self.driver.close()

    def kill(self):
        # 退出
        self.driver.quit()

    def sublimit(self, locator, locator_type='id'):
        # 提交
        self.element_presence_check(locator, locator_type)
        element = self.element_get(locator, locator_type)
        element.submit()

    def f5(self):
        # 刷新
        self.driver.refresh()

    def forward(self):
        # 前进
        self.driver.forward()

    def execute_js(self, script):
        # 执行js
        self.driver.execute_script(script)

    def wait(self, ocator, locator_type='id'):
        # 等待
        self.driver.implicitly_wait((ocator, locator_type))

    def accpet_alert(self):
        # 允许
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_aleter(self):
        #焦点切换到弹窗。
        self.driver.switch_to.alert()

    def get_current_handle(self):
        return self.driver.current_window_handle

    def get_handle(self):
        return self.driver.window_handles

    def switch_to_frame(self, locator, locator_type='id'):
        # 切换
        self.element_presence_check(locator, locator_type)
        element = self.element_get(locator, locator_type)
        self.driver.switch_to.frame(element)

    def back_default_content(self):
        #返回最外层表单
        self.driver.switch_to_default_content()

    def back_to_parent_content(self):
        #返回上一级表单
        self.driver.switch_to_parent_content()

    def element_isSelected(self, locator, locator_type='id'):
        #判断元素是否被选中
        self.element_presence_check(locator,locator_type='id')
        element = self.element_get(locator,locator_type)
        return element.is_selected()

    def element_size(self, locator, locator_type='id'):
        #返回元素的大小, 返回值：{'width': 250, 'height': 30}
        self.element_presence_check(locator, locator_type='id')
        element = self.element_get(locator, locator_type)
        return  element.size

    def element_isEnabled(self, locator, locator_type='id'):
        # 判断元素是否被使用
        self.element_presence_check(locator, locator_type='id')
        element = self.element_get(locator, locator_type)
        return element.is_enabled()

    def delete_all_cookies(self):
        #删除浏览器所有的cookies
        self.driver.delete_all_cookies()

    def get_all_cookies(self):
        #返回当前会话中的cookies
        return self.driver.get_cookies()

    def delete_some_cookie(self, cookie_item):
        #删除指定的cookie
        self.driver.delete_cookie(cookie_item)

    def get_value_by_cookie_item(self, cookie_item):
        #根据cookie name 查找映射Value值
        return self.driver.get_cookies(cookie_item)

    def back_last_page(self):
        #返回上一页
        self.driver.back()

    def mouse_move_to_element(self, locator, locator_type='id'):
        #按下鼠标左键在一个元素上
        self.element_presence_check(locator, locator_type='id')
        element = self.element_get(locator, locator_type)
        ActionChains(self.driver).click_and_hold(element).perform()

    def ctrl_and_key(self, key_name,locator, locator_type='id'):
        #全选输入框的内容 是 a
        self.element_presence_check(locator, locator_type='id')
        element = self.element_get(locator, locator_type)
        element.send_keys(Keys.CONTROL, key_name)

    def press_key(self, key_name,locator, locator_type='id'):
        #回车代替点，制表键(Tab)，回退键（Esc）
        self.element_presence_check(locator, locator_type='id')
        element = self.element_get(locator, locator_type)
        if key_name == "enter":
            element.send_keys(Keys.ENTER)
        elif key_name == "tab":
            element.send_keys(Keys.TAB)
        elif key_name == "esc":
            element.send_keys(Keys.ESCAPE)

