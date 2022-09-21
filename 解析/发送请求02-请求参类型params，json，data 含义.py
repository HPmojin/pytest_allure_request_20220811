#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : 发送请求02-请求参类型params，json，data 含义.py
# @Time : 2022-08-18 10:00
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------

# 请求参类型params，json，data 含义理解
# 简单来说，params是用来发送查询字符串，而data、json是用来发送正文的。
# 这两种参数post方法都可以用，get方法只能发查询字符串，不能发送正文。

# params：会将参数key、value拼接在url后；类似这种：url?参数名=参数值&参数名1=参数值1
# json：表示使用application / json方式提交请求。接收方request.body的内容为’{“a”: 1, “b”: 2}'的这种形式；
# data：表示使用请求头content-type是from表单类型。，接收方request.body的内容为a = 1 & b = 2

# 这三种参数类型是后台开发编写接口是已经定义好的，接口请求来发送来的参数，服务端是如何解析的，如果不是按照服务端定义的方法，服务端解析不了，返回参数异常等等，
# 换句话来说 你找我要数据， 你要按我给你设定好的格式递交申请，我看到这个申请才能读懂 你要干什么，要什么数据，我才能给你返回你想要的数据，不然就给你说申请内容看不懂，也就是参数异常
# 那么这个时候 发送请求的时候就需要你传你参数的类型是什么
#比如：
# r=requests.request(url=url,method='post',json=data), json=body_data中的json就代表我是以表示表示使用application / json方式提交请求，参数为body_data
#那么如果接口参数类型（请求方法（get/post）和服务端决定的）需要是data类型来传参，写法data=body_data
#那么如果接口参数类型（请求方法（get/post）和服务端决定的）需要是params类型来传参，写法params=body_data

import requests
def login():
    url='http://127.0.0.1:8888/api/private/v1/login' # 登录
    body_data={
    "username": "admin",
    "password": "123456"
}
    r=requests.post(url=url,json=body_data)
    r=requests.request(url=url,method='post',json=body_data)
    # r = requests.request(url=url, method='post', data=body_data)
    # r = requests.request(url=url, method='get', params=body_data)
    #r=Session().request(url=url,method='post',files=files,headers=headers,json=data)
    print(r.text)

login()
