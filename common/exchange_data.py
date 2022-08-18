#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/11 21:44
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : exchange_data.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import jsonpath,re,allure,json
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


    # @classmethod
    # def Extract_one(cls,response,josn_path):
    #     if josn_path!="" and eval(josn_path)!={}:
    #         return jsonpath.jsonpath(response, josn_path)[0]

    @classmethod
    def Extract_noe (csl,dic_data,josn_path):#提取参数return出去
        try:
            Extract_noe_v = ((jsonpath.jsonpath((dic_data), josn_path))[0])

        except Exception as e:
            Extract_noe_v = None
            Logger.error('提取参数出错！！（%s）' % e)

        return Extract_noe_v


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


            for func in re.findall('\\${(.*?)}', content):#${fk.random_int(min=1000,max=9999)   ${sdsd()}

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

    @classmethod
    def extra_pool_allure(cls):

        with allure.step('参数池数据：'):
            allure.attach(
                json.dumps(cls.extra_pool, ensure_ascii=False, indent=4),
                "附件内容",
                allure.attachment_type.JSON,
            )
    @classmethod
    def extra_allure(cls,extra):
        if extra=="":
            extra={}
        else:
            extra=eval(extra)

        with allure.step('提取参数路径：'):
            allure.attach(
                json.dumps((extra), ensure_ascii=False, indent=4),
                "附件内容",
                allure.attachment_type.JSON,
            )
