#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest_allure_request_20220811
# @Time    : 2022/11/4 15:30
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : hook.py
# @Software: PyCharm 
# -------------------------------------------------------------------------------
from faker import Faker
fk = Faker("zh_CN") # https://blog.csdn.net/weixin_43865008/article/details/115492280


def uuid4():
    return fk.uuid4()





