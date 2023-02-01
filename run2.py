#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/18 20:42
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : run.py
# @Software: PyCharm
#-------------------------------------------------------------------------------


import requests
from requests_toolbelt import MultipartEncoder
def hy_files():
    url='https://****************.com/_files/upload?accessType=2' # 传图片
    headers={
        "authorization": "kktJLMPhAtduLA0Jl5dXqull5LtuDGmM9saoDkA++meJ/XaV2KFYWFi4wLU5HHoIPcSCL/fGiMfit8sXwMRu5QUgHqeMcYOT2eoJDwqfLukzLN49oMJZusDgJ9RzhvpG",
        "peachauthversioncode": "9",
        "appversioncode": "9",
    }
    data = MultipartEncoder(
        fields={
            "file": ('1.jpg',
                             open('./config/1.jpg', 'rb'),
                             "image/jpeg")
        }
    )
    headers["Content-Type"] = data.content_type
    print(headers)
    print(data)
    r=requests.request(url=url,method='post',headers=headers,data=data)#,data=data
    print(r.text)

hy_files()



dic= {"$.data.pageOrder.records[0].orderId": '${order_id}',"$.data.pageOrder.records[0].statusDesc": "待收银"}
