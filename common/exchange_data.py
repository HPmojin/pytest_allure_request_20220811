#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/11 21:44
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : exchange_data.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import jsonpath,re
from string import Template
from common.logger import Logger
#https://blog.csdn.net/weixin_43865008/article/details/115492280
from faker import Faker

fk = Faker("zh_CN")
class ExchangeData():

    # 存放提取参数的池子
    extra_pool = {}

    @classmethod
    def Extract(cls,response,josn_path_dic):

        if josn_path_dic!="" and eval(josn_path_dic)!={}:
            for k, v in eval(josn_path_dic).items():
                try:
                    cls.extra_pool[k] = jsonpath.jsonpath(response, v)[0]
                except Exception as e:
                    cls.extra_pool[k]=None
                    Logger.error("提前参数异常！！！（%s）"%str(e))




    # re+Template  替换字符串中特定标识作为新值
    @classmethod
    def exec_func(cls,func: str) -> str:
        """执行函数(exec可以执行Python代码)
        :params func 字符的形式调用函数
        : return 返回的将是个str类型的结果
        """
        # 得到一个局部的变量字典，来修正exec函数中的变量，在其他函数内部使用不到的问题
        loc = locals()
        exec(f"result = {func}")
        return str(loc['result'])

    @classmethod
    def rep_expr(cls,content: str,return_type='srt'):
        """从请求参数的字符串中，使用正则的方法找出合适的字符串内容并进行替换
        :param content: 原始的字符串内容
        :param data: 提取的参数变量池
        return content： 替换表达式后的字符串
        """

        if content !="" :
            data=cls.extra_pool
            content = Template(content).safe_substitute(data)


            for func in re.findall('\\${(.*?)}', content):

                try:
                    content = content.replace('${%s}' % func, cls.exec_func(func))
                except Exception as e:
                    print(str(e))
        else:
            if content=="":
                content="{}"
            elif eval(content) =={}:
                content = content

        if return_type=="srt":
            content=(content)
        elif return_type=="dict" :
            content=eval(content)



        return content