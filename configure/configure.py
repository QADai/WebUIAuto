# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import os

#文件夹路径
base_path = os.path.dirname(os.path.dirname(__file__))
log_path =  os.path.join(base_path, "logs")
screen_path = os.path.join(base_path, "screenshot")
report_path = os.path.join(base_path, "report")
result_path = os.path.join(base_path, "result")
TC_path = os.path.join(base_path, "testdata")
tools_path = os.path.join(base_path, "tools")

#驱动文件路径
chrome_driver_path = os.path.join(tools_path, "chromedriver.exe")
# ie_driver_path = os.path.join(tools_path,"IEDriverServer.exe")
ie_driver_path = os.path.join(tools_path,"nuget.exe")
phantomjs_driver_path = os.path.join(tools_path,"phantomjs.exe")
#geckodriver是火狐浏览器的驱动程序，当您的浏览器出现脚本运行时出现脚本不兼容
firfox_driver_path = os.path.join(tools_path,"geckodriver.exe")
#y用于上传文件脚本
autoit_path = os.path.join(tools_path,"upfile.au3")

#服务器信息
test_server1_url = "https://www.baidu.com"
server1_username = "username1"
server1_password = "password"


#测试数据路径
phoneexcel = os.path.join(TC_path, 'phone.xlsx')
baidu_excel = os.path.join(TC_path, "baidu.xlsx")

#常用数字参数
load_page_timeout = 60

# 当前测试用的浏览器名称
current_using_browser = "chrome"

#用例优先级规则,设置方式为一个列表 一共分三个级别P1，P2，P3,e.g. ['P1', 'P2', 'P3']
Run_TC_Priority = ['P1', 'P2']