#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest_allure_request_SuiAnYun
# @Time    : 2022/11/9 10:33
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : hook.py
# @Software: PyCharm
# -------------------------------------------------------------------------------
from faker import Faker
import time
from common.logger import Logger
fk = Faker("zh_CN") # https://blog.csdn.net/weixin_43865008/article/details/115492280
import random

def Times():
    #fk.date_between_dates()
    #fk.date_object()
    return fk.date_between_dates()


def list_random_index(lists_s):
    #fk.date_between_dates()
    #fk.date_object()
    Logger.error(lists_s)
    Logger.error(type(lists_s))
    return random.randint(0,len(lists_s)-1)

def waits(t):

    time.sleep(t)
    Logger.warning('sleep %s s'%t)

    return 'sleep %s s'%t
