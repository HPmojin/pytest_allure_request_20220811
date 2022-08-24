#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : logger_bak.py
# @Time : 2022-08-24 09:45
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------

import logging, time, os
from common.all_path import logPath

# 日志文件路径
LOG_PATH = logPath
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger():

    def __init__(self):
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


Logger = Logger().logger
# class Logger_Error():
#
#     def __init__(self):
#         self.logname = os.path.join(LOG_PATH, "{}-fail.log".format(time.strftime("%Y%m%d")))
#         self.logger = logging.getLogger("log")
#         self.logger.setLevel(logging.DEBUG)
#
#         self.formater = logging.Formatter(
#             '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
#
#         self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
#         self.console = logging.StreamHandler()
#         self.console.setLevel(logging.DEBUG)
#         self.filelogger.setLevel(logging.DEBUG)
#         self.filelogger.setFormatter(self.formater)
#         self.console.setFormatter(self.formater)
#         self.logger.addHandler(self.filelogger)
#         self.logger.addHandler(self.console)
#
# Logger_Error = Logger_Error().logger
if __name__ == '__main__':
    Logger.info("---测试开始---")
    Logger.debug("---测试结束---")
