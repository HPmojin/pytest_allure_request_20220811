#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : loggers.py
# @Time : 2022-08-24 09:30
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
import logging,time, os
from loguru import logger as Logger
from common.all_path import logPath

# 日志文件路径
LOG_PATH = logPath
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

class PropogateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)


logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
Logger.add(logname)
Logger.add(PropogateHandler(), format="{time:YYYY-MM-DD HH:mm:ss}|{message}", enqueue=True,)#enqueue=True, serialize=True

#参考文档
# https://blog.csdn.net/qq_33528044/article/details/109122327
# https://blog.csdn.net/qishuzdh/article/details/125430850
