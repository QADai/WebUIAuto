# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""

import os
import logbook
from logbook import Logger, StderrHandler, FileHandler, TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler
from configure.configure import *

class logbook_use:
    def __init__(self):
        # 脚本日志
        self.run_log = Logger("script_log")

        # 日志存放路径
        self.LOG_DIR = log_path
        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

        def log_type(record, handler):
            log = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
                date=record.time,  # 日志时间
                level=record.level_name,  # 日志等级
                filename=os.path.split(record.filename)[-1],  # 文件名
                func_name=record.func_name,  # 函数名
                lineno=record.lineno,  # 行号
                msg=record.message)  # 日志内容
            return log

        # 日志打印到屏幕
        self.log_std = ColorizedStderrHandler(bubble=False)
        self.log_std.formatter = log_type

        # 日志打印到文件
        self.log_file = TimedRotatingFileHandler(os.path.join(self.LOG_DIR, '%s.log' % 'log'), date_format='%Y-%m-%d',
                                            bubble=True, encoding='utf-8')
        self.log_file.formatter = log_type

    def init_logger(self):
        logbook.set_datetime_format("local")
        self.run_log.handlers = []
        self.run_log.handlers.append(self.log_file)
        self.run_log.handlers.append(self.log_std)
        return self.run_log

def log_instance():
    logbook_test = logbook_use()
    log_obj = logbook_test.init_logger()
    return log_obj

log = log_instance()


