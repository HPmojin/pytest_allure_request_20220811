#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : flask开发2个http接口.py
# @Time : 2022-08-11 16:45
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------

import flask, json
from flask import request
'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
pip3 install flask -i https://pypi.doubanio.com/simple

'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)

# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 的路径、请求方式
@server.route('/list/project', methods=['get'])#'get',
def Projectlist():
    '''
    http://127.0.0.1:5000/list/project?project=324324&name=234
    :return:
    '''
    proj= request.values.get('project')
    name= request.values.get('name')
    project={
        "msg": "查询成功",
        "status": 10000,
        "data":[{        "project":proj,
        "name": name}]
    }

    return json.dumps(project)



# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 的路径、请求方式


@server.route('/login',methods=['post']) #入参为json
def login():
    '''
    http://127.0.0.1:5000/login
    {
    "user_name":"mojin",
    "pwd":"123456"
    }
    :return:
    '''
    params = flask.request.json#当客户端没有传json类型或者没传时候，直接get就会报错。
    # params = flask.request.json #入参是字典时候用这个。
    if params:
        dic = {
            'user_name': params.get('user_name'),
            'pwd': params.get('pwd')
        }
        login_info={
            "data": {
                "id": 500,
                "rid": 0,
                "username": dic['user_name'],
                "pwd": '*********',
                "mobile": "12345678",
                "email": "adsfad@qq.com",
                "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE2NjAyMDcwNTksImV4cCI6MTY2MDI5MzQ1OX0.tt0dOAFrlwckl3yvz1n9r_GLSyaev4kkxzL3jJACYuM"
            },
            "meta": {
                "msg": "登录成功",
                "status": 200
            }
        }

        data = json.dumps(login_info)
        print("'/login',methods=['post']：%s；%s"%(str(dic),str(data)))
        return data
    else:
        #data = json.dumps({"result_code": 3002, "msg": "入参必须为json类型。"})
        data = ({"result_code": 3002, "msg": "入参必须为json类型。"})
        print("'/login',methods=['post']："+str(data))
        return data

if __name__ == '__main__':
    if __name__ == "__main__":
        server.run(host='0.0.0.0', port=5000, debug=True)
