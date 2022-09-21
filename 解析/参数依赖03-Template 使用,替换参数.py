#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : 参数依赖03-Template 使用,替换参数.py
# @Time : 2022-08-09 09:42
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
from string import Template
import re
#Template 使用,替换参数

def num():
    return 6+10
def num2():
    return 6+13


d={'a':'apple','b':'banbana',}
content_srt="There ${a} and ${b},${num()} and ${num2()} "


def Templ_te(content_srt):
    content = (Template(content_srt).safe_substitute(d))
    print(content)
    for func in re.findall('\\${(.*?)}', content):


        loc = locals()
        # exec("sum()")
        exec(f"result = %s" % func)

        content = content.replace('${%s}' % func, str(loc['result']))

    return (content)


print(Templ_te(content_srt))

# srt_  = '{"member_id":#member_id#,"amount":2000}'
# member_id = "16"
# new_ss = eval(srt_ .replace("#member_id#", member_id))
#
# print(new_ss)
# print(new_ss['member_id'])


