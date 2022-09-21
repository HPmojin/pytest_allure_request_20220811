#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/14 15:05
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 发送请求03-理解两种发送请求方法.py
# @Software: PyCharm
#-------------------------------------------------------------------------------

#理解这两种发送请求
# r = requests.post(url=url, files=files, headers=headers, json=data)
# r = requests.request(url=url, method='post', files=files, headers=headers, json=data)
# 理解这两种发送请求

class requests_all:

    def get_1(self,url='xxxx'):
        print('执行get_1方法,url=%s'%(url))

    def post_1(self,url='xxxx'):
        print('执行post_1方法,url=%s' % (url))

    def request_all(self,url='xxxx',met=None):
        if met=='get_1':
            self.get_1(url)
        elif met=='post_1':
            self.post_1(url)
requests_all=requests_all()
url='xxxx'

# r = requests.post(url=url, files=files, headers=headers, json=data)
# r = requests.request(url=url, method='post', files=files, headers=headers, json=data)
# 上面两个的区别 就类似下面两个的区别，
# requests_all.get_1(url)
# requests_all.request_all(url,met='get_1')

requests_all.post_1(url)#这是一个post_1方法

#这个里面是会根据met的值 调用他对应的方法，是一个已经封装好的方法
#或者你不用request_all方法，自己根据met的值 封装一个方法也是可以的
requests_all.request_all(url,met='post_1')

# r = requests.post(url=url, files=files, headers=headers, json=data)
# r = requests.request(url=url, method='post', files=files, headers=headers, json=data) 换句话说这个封装好的一个方法可以根据method找对应请求类型
