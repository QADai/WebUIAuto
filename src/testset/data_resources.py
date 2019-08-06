# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
这个类用于从生成数据驱动需要的测试数据
"""
import sys

sys.path.append(r'.')
from src.utils.excel_util import ExcelReader
from configure.configure import *
from src.utils.log_util import log


def get_search_data(priority):
    log.info("读取excel的数据")
    test_data = ExcelReader(baidu_excel, 0)
    print(test_data.data)
    data_list = [(i['keyword'].decode('utf-8'),i['description'].decode('utf-8')) for i in test_data.data if i["priority"].decode('utf-8') in priority]
    return data_list



if __name__ == "__main__":
    print(get_search_data(["P1", "P2", "P3"]))
