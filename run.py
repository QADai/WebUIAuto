# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import os
import pytest
import subprocess
from time import sleep
from configure.configure import *


# 列表第一个参数为模块名称； 第二参数为测试类类名， 第三个参数为测试类中的函数, 暂时没有用到
test_sets = [
    [
        ["test_baidu_home_page", True], ["Test_Home_Page", True], [
        ["test_search", True],
        ["test_enter_news", True],
        ["test_enter_hao123", True],
        ["test_enter_map", True],
        ["test_enter_video", True],
        ["test_enter_tieba", True],
        ["test_enter_academic", True],
        ["test_open_settings", True]
        ]
    ]
]

def make_up_test_sets():
    test_func_sets = list()
    for module in test_sets:
        if module[0][1]:
            if module[1][1]:
                for test_func in module[2]:
                    if test_func[1]:
                        test_func_path = "src/tesset/" + module[0][0] + "::" + module[1][0] + "::" + test_func[0]
                        test_func_sets.append(test_func_path)
    return test_func_sets


def main():
    test_func_sets = make_up_test_sets()
    test_func_sets_str = " ".join(test_func_sets)
    pytest.main(["-s", "-v", test_func_sets_str])


def exec_test_run():
    subprocess.call(["pytest", "./src/testset", "--alluredir", "./result"])
    sleep(1)
    os.system("allure generate ./result -o ./report --clean")

if __name__ == "__main__":
    exec_test_run()
