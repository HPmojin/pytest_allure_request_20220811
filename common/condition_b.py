#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : condition_b.py
# @Time : 2022-08-12 14:57
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
#存放条件方法在Excel中调用执行
from common.logger import Logger
import pytest
from common.exchange_data import ExchangeData
from _pytest.outcomes import Skipped


class Condition():
    def skip_if(self,case):

        skip_if_srt=case[5]

        result_list=[]
        if skip_if_srt != "":
            if isinstance(skip_if_srt, bool):  # 判断运行后的结果是否为bool类型
                result_list.append(skip_if_srt)
            else:
                if skip_if_srt not in [None,"None"]:

                    skip_if_srt = (
                        ExchangeData.rep_expr(skip_if_srt, return_type="srt"))  # 请求入参中的变量在全局参数池中替换
                    Logger.info(skip_if_srt)
                    for sp in skip_if_srt.split(';'):#多个跳过条件判断
                        Logger.info(sp)
                        loc = locals()#获取本地的参数，

                        try:
                            exec("result = %s"%sp)  #exec执行字符串sp中的代码，以字符串执行
                        except:
                            loc['result']='exec("result = %s"%sp)执行出错'
                        Logger.info(loc['result'])

                        if isinstance(loc['result'],bool): #判断运行后的结果是否为bool类型

                            result_list.append(loc['result'])#如果是添加到结果列表中
                        else:#如果不是 布尔类型
                            if loc['result'].upper() =='False'.upper():# 如未字符串False，添加一个False到结果列表中
                                result_list.append(False)
                            elif loc['result'].upper() =='True'.upper():#如未字符串True，添加一个True到结果列表中
                                result_list.append(True)
                            else:
                                Logger.warning('输入了一个不认识的判断条件（%s），不做跳过，忽略这个条件继续执行；当前条件只能接受逻辑运算类型或False或True！！！'%(loc['result']))

            if not False in result_list:
                pass
            else:
                pytest.skip("跳过该条用例；\n原因：\n【%s】\n【%s】"%(case[5],skip_if_srt))#reason=
                #raise Skipped("跳过该条用例；原因：【%s】"%skip_srt)

    # import pytest
    # from _pytest.outcomes import Skipped
    # pytest.skip(reason='跳过test_skip_02')
    # raise Skipped("跳过用例")

