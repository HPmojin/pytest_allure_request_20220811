#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/18 20:47
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : assert_api.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from common.exchange_data import ExchangeData
from common.logger import Logger
import jsonpath,allure,json
class AssertApi():

    def assert_api(self,response,case):
        expect=case[-1]
        result_all=[]
        result_dic_list=[]
        if expect != "":
            n = 1
            for k, v in eval(expect).items():
                # Logger.info((jsonpath.jsonpath(response, k)[0]))
                # Logger.info(v)
                # actual_results=(jsonpath.jsonpath(response, k)[0])#实际结果
                actual_results = ExchangeData.Extract_noe(response,k)
                result = (v == actual_results)
                result_dic={
                        "提取路径": k,
                        "实际结果": actual_results,
                        "预期结果": v,
                        "测试结果": result
                        }
                result_all.append(result)
                result_dic_list.append(result_dic)

                n += 1
        else:
            Logger.warning('没有写断言……')
            result_all = [False]
            result_dic_list.append({"result":"没有添加断言,无断言用例标记失败，请添加断言判断用例",})

        with allure.step('断言：%s'%(False not in result_all)):
            for result_dic in result_dic_list:
                allure.attach(
                    json.dumps(result_dic, ensure_ascii=False, indent=4),
                    "断言：%s：" % (result_dic.get('测试结果',False)),
                    allure.attachment_type.JSON,
                )

        Logger.info(result_all)
        return False not in result_all





