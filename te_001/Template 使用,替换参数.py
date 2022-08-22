#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : Template 使用,替换参数.py
# @Time : 2022-08-09 09:42
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
from string import Template
#Template 使用,替换参数





d={'a':'apple','b':'banbana',}
print(Template("There ${a} and ${b}").substitute(d))




# srt_  = '{"member_id":#member_id#,"amount":2000}'
# member_id = "16"
# new_ss = eval(srt_ .replace("#member_id#", member_id))
#
# print(new_ss)
# print(new_ss['member_id'])


