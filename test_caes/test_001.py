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
from common.api_request import Api_Request
from common.read_exce_yaml_caes import get_yaml_excle_caes


#@allure.epic(ReadFile.read_config("$.project_name"))  # 项目名称
class Test():

    @pytest.mark.parametrize("case",get_yaml_excle_caes())
    @allure.step
    # def test_001(self,case,get_db):#,get_db
    def test_001(self, case,env_url):  # ,get_db
        # 需要执行sql查询断言时，参数中添加get_db
        # 不需要执行sql查询断言时，参数中去掉get_db


        response=(Api_Request.api_data(case,env_url))

        # 需要执行sql查询断言时，参数中添加get_db
        # 不需要执行sql查询断言时，参数中去掉get_db
        # assert AssertApi().assert_api(response,case,get_db)#,get_db
        assert AssertApi().assert_api(response, case)  # ,get_db



