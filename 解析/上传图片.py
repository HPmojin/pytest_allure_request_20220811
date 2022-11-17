#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/11 20:28
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 上传图片.py
# @Software: PyCharm
#-------------------------------------------------------------------------------

import requests
from requests_toolbelt import MultipartEncoder
def hy_files():
    url='https://234*******n/upload' # 传图片
    headers={
        "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImEwYTBhMjBjLWYwZTctNDdhYi05NzgyLTAwMDBkMDY3MzMxMyJ9._oFwTF8s3U1-2zbDOtc2c7wRaEaJ44gIGAyoqhz1WML1ebQVjzwWzJN9zbd9nB0zFMOkWUTLiGY9J156V-pa7Q",
    }
    data = MultipartEncoder(
        fields={
            "file": ('1.jpg',
                             open('./config/1.jpg', 'rb'),
                             "image/jpeg"),

        }
    )
    headers["Content-Type"] = data.content_type
    r=requests.request(url=url,method='post',headers=headers,data=data)#,data=data
    print(r.text)

hy_files()
