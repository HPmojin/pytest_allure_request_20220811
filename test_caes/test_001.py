#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/18 20:38
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : test_001.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import pytest,allure

from common.assert_api import AssertApi
from common.operation_excle import operation_excle
from common.api_request import Api_Request
from common.read_file import ReadFile


Sheet=operation_excle.read_excel(ReadFile.read_config('$..test_case'), ReadFile.read_config('$..case_severity'))

class Test():

    @pytest.mark.parametrize("case",Sheet)
    def test_001(self,case,get_db):#,get_db
        # 需要执行sql查询断言时，参数中添加get_db
        # 不需要执行sql查询断言时，参数中去掉get_db

        response=(Api_Request.api_data(case))

        # 需要执行sql查询断言时，参数中添加get_db
        # 不需要执行sql查询断言时，参数中去掉get_db
        assert AssertApi().assert_api(response,case,get_db)#,get_db



