#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/9/13 20:52
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 备份恢复sql-FTP上传文件.py
# @Software: PyCharm
#-------------------------------------------------------------------------------

import paramiko
import time

host='192.168.1.181'
port=22
username='root'
password='root'

trans = paramiko.Transport((host, port))  # 实例化一个transport对象
trans.connect(username=username, password=password,) #连接transport


ftp = paramiko.SFTPClient.from_transport(trans)  # 实例化一个ftp


# ftp.get('服务器文件路径', ' 本地文件路径')  # 下载文件
# ftp.put('本地文件路径', '服务器文件路径')  # 上传文件

ftp.put( '../config/mydb.sql', '/mnt/backup/mydb.sql')  # 上传文件
ftp.get('/mnt/backup/mydb.sql', 'mydb.sql')  # 下载文件


ftp.close()
trans.close()
