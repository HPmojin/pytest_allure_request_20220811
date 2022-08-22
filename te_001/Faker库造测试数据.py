#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : Faker库造测试数据.py
# @Time : 2022-08-11 12:20
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------

#https://blog.csdn.net/weixin_43865008/article/details/115492280
from faker import Faker

fk = Faker("zh_CN")
print(fk.random_int(min=1000,max=9999))


print(fk.name())
