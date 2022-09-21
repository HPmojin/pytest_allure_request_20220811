#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : 发送请求04-封装请求参数转化的理解.py
# @Time : 2022-08-18 09:41
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
#封装请求参数转化的理解

# from requests import Session
import requests
class Api_Request():
    def api_request(self,url, method, parametric_key, body_data=None,header=None,  file=None) :
        ###################################################################################
        #body_data，请求参数在传进来是必须要为一个字典格式
        if parametric_key=="params":
            parametric={"params":body_data}
        elif parametric_key=="data":
            parametric={"data":body_data}
        elif parametric_key=="json":
            parametric={"json":body_data}
        else:
            raise ValueError("“parametric_key”的可选关键字为params, json, data")
        # 这里判断了参数类型，也就是说，发送请求是传来的请求参数是params还是json还是 data
        # 是json那要转为{'json': {'username': 'admin', 'password': '123456'}}
        # 是params那要转为{'params': {'username': 'admin', 'password': '123456'}}
        # 是data那要转为{'data': {'username': 'admin', 'password': '123456'}}
        ###################################################################################
        try:
            print(parametric)
            ###################################################################################
            # 再然后
            # {'json': {'username': 'admin', 'password': '123456'}}字典格式转为json=body_data也就是json={'username': 'admin', 'password': '123456'}
            # 转化方法就是**parametric，字典解包为赋值形式json={}，json={'username': 'admin', 'password': '123456'}
            # res = requests.request(method=method, url=url, files=file, headers=header, **parametric)
            # 字典** 和 列表* 解包理解，参考 https://blog.csdn.net/weixin_42468475/article/details/105505230
            ###################################################################################
            res = requests.request(method=method, url=url, files=file, headers=header, **parametric)
            response=res.json()
        except Exception as e:
            raise '请求发送失败：%s'%(e)
        return response
if __name__ == '__main__':
    Api_Request=Api_Request()
    url = 'http://127.0.0.1:8888/api/private/v1/login'  # 登录
    body_data = {'username': 'admin', 'password': '123456'}
    method="post"
    parametric_key='json'
    a=Api_Request.api_request(url,method,parametric_key,body_data)
    print(a)





