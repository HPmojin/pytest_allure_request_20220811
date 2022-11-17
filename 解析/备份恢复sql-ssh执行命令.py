#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/9/13 20:39
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 备份恢复sql-ssh执行命令.py
# @Software: PyCharm
#-------------------------------------------------------------------------------

#pip3 install paramiko

#https://www.cnblogs.com/honey-badger/p/8424638.html
import paramiko
import time

host='192.168.1.183'
port=22
username='root'
password='root'

trans = paramiko.Transport((host, port))  # 实例化一个transport对象
trans.connect(username=username, password=password,)#连接transport

ssh = paramiko.SSHClient()#创建ssh客户端client对象
ssh._transport = trans  ## 将sshclient的对象的transport指定为以上的trans

stdin, stdout, stderr = ssh.exec_command("ls")#执行命令

print(stdout.read().decode('utf-8')) #打印

time.sleep(1)#报错https://blog.csdn.net/linpengzt/article/details/122043101
ssh.close()#ssh  ssh
trans.close() # close   transport