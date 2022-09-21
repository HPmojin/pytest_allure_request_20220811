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

trans = paramiko.Transport((host, port))
trans.connect(username=username, password=password,)

ssh = paramiko.SSHClient()
ssh._transport = trans

stdin, stdout, stderr = ssh.exec_command("ls")

print(stdout.read().decode('utf-8'))



time.sleep(1)#报错https://blog.csdn.net/linpengzt/article/details/122043101
ssh.close()
trans.close()