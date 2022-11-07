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
from faker import Faker
from string import Template
from common.logger import Logger
from common.hook import uuid4,fk       #或  from common.hook import *
#from common.read_file import ReadFile

#
# fk = Faker("zh_CN") # https://blog.csdn.net/weixin_43865008/article/details/115492280

class ExchangeData():

    # 存放提取参数的池子
    extra_pool ={"token":''}





    @classmethod
    def Extract(cls,response,josn_path_dic):

        if josn_path_dic!="" and eval(josn_path_dic)!={}:
            for k, v in eval(josn_path_dic).items():
                try:
                    cls.extra_pool[k] = jsonpath.jsonpath(response, v)[0]
                except Exception as e:
                    cls.extra_pool[k]=""
                    #Logger.error("提前参数异常！！！（%s）"%str(e))


    # @classmethod
    # def Extract_one(cls,response,josn_path):
    #     if josn_path!="" and eval(josn_path)!={}:
    #         return jsonpath.jsonpath(response, josn_path)[0]

    @classmethod
    def Extract_noe (csl,dic_data,josn_path):#提取参数return出去
        try:
            Extract_noe_v = ((jsonpath.jsonpath((dic_data), josn_path))[0])

        except Exception as e:
            Extract_noe_v = josn_path
            #Extract_noe_v = None
            #Logger.error('提取参数出错！！（%s）' % e)

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
                #Logger.error(func)
                try:
                    content = content.replace('${%s}' % func, cls.exec_func(func))
                except Exception as e:
                    Logger.error(str(e))

        #后面两种写法

        #第一中
        # else: #如果为空，
        #     if content=="": #如果输入的空字符串格式，强制转为空字典，统一格式后面转字典
        #         content="{}" #强制转为空字典格式的字符串类型
        #     elif eval(content) =={}: #判断是否为空字典的格式的字符串，也就是 判断是否为  “{}”
        #         content = content
        #       #在这 content已经统一为字典格结构格式的字符串类型了
        #
        # if return_type=="srt":  #判断返回类型为字符串
        #     content=(content)  #直接赋值不用再转换类型
        # elif return_type=="dict" :  #判断返回类型为字典
        #     try:#尝试转为字典类型
        #         content = eval(content) #“{}”转成功了{} 则 ：“{}”  字典结构格式的字符串转为字典 eval()
        #     except Exception as e:#字符串类型转字典，抛异常的
        #         Logger.warning("Excle输入的字符串格式，不能转为字典类型!!!(%s)"%str(e))
        #         raise Exception("Excle输入的字符串格式，不能转为字典类型!!!(%s)"%str(e))

        #第二中
        else: #如果为空，
            pass  #如果为空，则content=content 或pass(这两种一样的性质)
        #判断返回类型
        if return_type=="srt":
            content=(content)
        elif return_type=="dict" :#如果返回为字典
            if  content=="":#判断是否为值
                content = "{}"#为空值赋值字符串类的空字典

            try:#尝试转为字典类型
                content = eval(content) #“{}”转成功了{}
            except Exception as e:#字符串格式转字典，抛异常的
                Logger.warning("Excle输入的字符串格式，不能转为字典类型， 请检查参数!!!(%s)"%str(e))
                raise Exception("Excle输入的字符串格式，不能转为字典类型，请检查参数!!!(%s)"%str(e))

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

    @classmethod
    def post_pytest_summary(cls,result_data_test):#添加测试概况数据到变量池
        from common.read_file import ReadFile
        cls.extra_pool.update(result_data_test)
        cls.extra_pool.update({"PROJECT_NAME":ReadFile.read_config("$.project_name")})
        Logger.info(cls.extra_pool)



    @classmethod
    def get_pytest_summary(cls):#读取report.html模板，替换变量后，返回完整的html 作为发送邮件内容
        file = open('./config/report.html', "r", encoding="utf-8")
        data = file.read()
        file.close()
        data = ExchangeData.rep_expr(data, return_type='srt')
        return data