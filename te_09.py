#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/16 21:01
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : te_09.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import openpyxl
# import jsonpath
# r={'data': None, 'meta': {'msg': '参数错误', 'status': 400}}
# print(jsonpath.jsonpath(r, "$..msg")[0])
# print(jsonpath.jsonpath(r, "$..status")[0])

from common.read_file import ReadFile

print(ReadFile.read_config('$..cor_rel_case_severity'))