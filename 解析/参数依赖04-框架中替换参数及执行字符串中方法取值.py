#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : 参数依赖04-框架中替换参数及执行字符串中方法取值.py
# @Time : 2022-08-09 09:55
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
import re
from string import Template

from faker import Faker

fk = Faker("zh_CN")

# re+Template  替换字符串中特定标识作为新值
def exec_func(func: str) -> str:
    """执行函数(exec可以执行Python代码)
    :params func 字符的形式调用函数
    : return 返回的将是个str类型的结果
    """
    # 得到一个局部的变量字典，来修正exec函数中的变量，在其他函数内部使用不到的问题
    loc = locals()
    exec(f"result = {func}")
    return str(loc['result'])

def a_b():

    return 45

def rep_expr(content: str, data: dict) -> str:
    """从请求参数的字符串中，使用正则的方法找出合适的字符串内容并进行替换
    :param content: 原始的字符串内容
    :param data: 提取的参数变量池
    return content： 替换表达式后的字符串
    """
    content = Template(content).safe_substitute(data)
    print(content)

    for func in re.findall('\\${(.*?)}', content):
        print(func)
        try:
            content = content.replace('${%s}' % func, exec_func(func))
        except Exception as e:
            print(str(e))
    return content



Parameter_pool={'email': 'adsfad@qq.com', 'token': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE2NjAxMjEyMDYsImV4cCI6MTY2MDIwNzYwNn0.el8d3Wj4vgqqsC33Ypwc18kcEoScuu228hOKnU1Dozw', 'mobile': '12345678'}


dic_te={"username":"huangpeng","token":'${token}',"uuid":"${a_b()}","email":'${email}',"name":'${fk.user_name()}'}
# dic_te2={
# 	"goods_name": "商品_${fk.random_int(min=1000,max=9999)}",
# 	"goods_cat": "1,2,3",
# 	"goods_price": 20,
# 	"goods_number": 30,
# 	"goods_weight": 40,
# 	"goods_introduce": "abc",
# 	"attrs": [{
# 			"attr_id": 15,
# 			"attr_value": "dderd"
# 		},
# 		{
# 			"attr_id": 15,
# 			"attr_value": "324"
# 		}
# 	]
# }


print(rep_expr(str(dic_te), Parameter_pool))
