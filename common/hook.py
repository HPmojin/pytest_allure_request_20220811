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
import requests
def uuid4():
    return fk.uuid4()

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


def get_file_url(url):

    re=requests.request('get',url=url)
    status_code=re.status_code

    data_dic={
        "文件地址": url,
        "文件地址请求响应码":f'{status_code}(响应码)',

    }
    return data_dic

# url='http://192.168.1.55:5188/SuiAnYun/轨道交通AR应急处置系统（遂安云）项目测试报告.pdf'
# #
# data=(get_file_url(url))
# print(str(data))
# n="响应码200" in str(data)
# print(n)
