#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/11 20:28
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : jsonpath提取参数.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from common.operation_excle import operation_excle
from common.api_request import Api_Request

case_list=operation_excle.read_excel('./data/case_data.xlsx', ["P1","P2","P3","P4"])#[[],[],[],]
for case in case_list:

    (Api_Request.api_data(case))

