#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : te_001.py
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
        "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE2NjAxMjEyMDYsImV4cCI6MTY2MDIwNzYwNn0.el8d3Wj4vgqqsC33Ypwc18kcEoScuu228hOKnU1Dozw"
    },
    "meta": {
        "msg": "登录成功",
        "status": 200
    }
}

# print(jsonpath.jsonpath(dic_data,"$.data.token")[0])
extract_data={}

josn_path_dic={"email": "$..email","token":"$.data.token","mobile":"$.data.mobile"}
for k,v in josn_path_dic.items():

    extract_data[k]=jsonpath.jsonpath(dic_data, v)[0]

print(extract_data)
# for k, v in josn_path_dic.items():
#
#     extract_data[k]=(jsonpath.jsonpath(dic_data, v)[0])
#
# print(extract_data)
