#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : 发送请求01-get方法中url参数拼接和写到请求体中的理解.py
# @Time : 2022-08-12 14:09
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------


#################################################################################
#get方法中url参数拼接和写到请求体中的理解

'''
1.如get的请求参数拼接到了url上那么，他的请求参数body_data给为空，参数类型params，可以执行调用成功
url = 'http://www.kuaidi100.com/query?type=zhongtong&postid=73116039505988'
body_data={}

2.如get的请求参数没有在url上拼接，写到了body_data中，参数类型params，发送请求，可以执行调用成功
url = 'http://www.kuaidi100.com/query'
body_data = {
    "type": "zhongtong",
    "postid": 73116039505988
}

3.如get的请求参数拼接到了url上，而且也写到了body_data中，参数类型params，
实际上这里的参数已经重复写了，也就是写错了，但python可能为了容错，只读了url上的参数，没有取body_data中的参数，或者其他方法，可以执行调用成功
url = 'http://www.kuaidi100.com/query?type=zhongtong&postid=73116039505988'
body_data = {
    "type": "zhongtong",
    "postid": 73116039505988
}

'''

#################################################################################
#http://www.kuaidi100.com/query?type=zhongtong&postid=73116039505988
import requests
def requ_api_1():
    url = 'http://www.kuaidi100.com/query?type=zhongtong&postid=73116039505988'
    body_data={}
    r=requests.get(url=url,params=body_data)
    r=requests.request(url=url,method='get',params=body_data)
    # r = requests.request(url=url, method='post', data=body_data)
    # r = requests.request(url=url, method='get', params=body_data)
    #r=Session().request(url=url,method='post',files=files,headers=headers,json=data)
    print(r.text)

def requ_api_2():
    url='http://www.kuaidi100.com/query'
    body_data={
        "type":"zhongtong",
        "postid":73116039505988
    }
    r=requests.get(url=url,params=body_data)
    r=requests.request(url=url,method='get',params=body_data)
    # r = requests.request(url=url, method='post', data=body_data)
    # r = requests.request(url=url, method='get', params=body_data)
    #r=Session().request(url=url,method='post',files=files,headers=headers,json=data)
    print(r.text)

def requ_api_3():
    url='http://www.kuaidi100.com/query?type=zhongtong&postid=73116039505988'
    body_data={
        "type":"zhongtong",
        "postid":73116039505988
    }
    r=requests.get(url=url,params=body_data)
    r=requests.request(url=url,method='get',params=body_data)
    # r = requests.request(url=url, method='post', data=body_data)
    # r = requests.request(url=url, method='get', params=body_data)
    #r=Session().request(url=url,method='post',files=files,headers=headers,json=data)
    print(r.text)

requ_api_1()
requ_api_2()
requ_api_3()
