#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : 参数依赖02-locals()获取本地变量 及exec()执行字符串中的代码.py
# @Time : 2022-08-11 11:43
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
#locals()获取本地变量  exec()执行字符串中的代码

x = 10
y = 30
z = 30
def sum():
    sum = x + y + z

    return (sum)

a='"None"!="None"'

loc = locals()

# exec("sum()")
exec(f"result = sum()")
exec(f"r = {a}")
#
print(loc['result'])
print(loc['r'])


# hello = 123
# hello2 = 646545656
# loc = locals()
# print(loc)
