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


excle_data_list=operation_excle.read_excel(ReadFile.read_config('$..test_case'), ReadFile.read_config('$..case_severity'))
#excle_data_list=operation_excle.read_excel(ReadFile.read_config('$..cor_rel_case_severity'), ["P1", "P2", "P3", "P4"])

class Test():

    @pytest.mark.parametrize("case",excle_data_list)
    def test_001(self,case):
        allure.dynamic.title(case[1])
        allure.dynamic.severity(ReadFile.read_config('$..cor_rel_case_severity')[case[4]])

        response=(Api_Request.api_data(case))

        assert AssertApi().assert_api(response,case)
