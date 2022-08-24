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
    def test_001(self,case,get_db):
        allure.dynamic.title(case[1])
        allure.dynamic.story(case[-1])
        del case[-1]
        allure.dynamic.severity(ReadFile.read_config('$..cor_rel_case_severity')[case[4]])

        response=(Api_Request.api_data(case))

        AssertApi().assert_sql(response, case,get_db)
        assert AssertApi().assert_api(response,case)

    # @pytest.mark.parametrize("case",Sheet1)
    # def test_002(self,case,get_db):
    #     allure.dynamic.title(case[1])
    #     allure.dynamic.severity(ReadFile.read_config('$..cor_rel_case_severity')[case[4]])
    #
    #     response=(Api_Request.api_data(case))
    #
    #     AssertApi().assert_sql(response, case,get_db)
    #     assert AssertApi().assert_api(response,case)
