#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : 参数依赖01-jsonpath提取参数.py
# @Time : 2022-08-08 15:52
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
import jsonpath
#使用 jsonpath
dic_data={
    "data": {
        "id": 500,
        "rid": 0,
        "username": "admin",
        "mobile": "12345678",
        "email": "adsfad@qq.com",
        "token": "228hOKnU1Dozw"
    },
    "token": "Bea",
    "meta": {
        "msg": "登录成功",
        "status": 200,
        "token": "eyJhbGciOiJIUz"
    }
}

print(jsonpath.jsonpath(dic_data,"$..token.[2]"))
# extract_data={}
#
# josn_path_dic={"email": "$..email","token":"$.data.token","mobile":"$.data.mobile"}
# for k,v in josn_path_dic.items():
#
#     extract_data[k]=jsonpath.jsonpath(dic_data, v)[0]
#
# print(extract_data)
# for k, v in josn_path_dic.items():
#
#     extract_data[k]=(jsonpath.jsonpath(dic_data, v)[0])
#
# print(extract_data)
