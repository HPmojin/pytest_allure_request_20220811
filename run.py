#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/18 20:42
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : run.py
# @Software: PyCharm
#-------------------------------------------------------------------------------


import pytest,shutil,subprocess
from common.read_file import ReadFile
from common.send_email import EmailServe

def run():
    try:
        shutil.rmtree('./target')
        shutil.rmtree('allure-report.zip')
    except:
        pass

    pytest.main(['./test_caes','-vs',"--alluredir","target/allure-results"])
    allure_html = 'allure generate ./target/allure-results -o ./target/allure-report --clean'  # 生成allure的html报告

    subprocess.call(allure_html, shell=True)  # 生成allure的html报告

    cmd_server=r'cp config/Start_server.bat target'
    subprocess.call(cmd_server, shell=True)  # 启动服务器脚本，由config目录拷贝到target/allure-report目录下进行打包发送邮件

    setting = ReadFile.read_config('$.email') #获取邮件相关信息
    Files_path='./target'
    EmailServe.send_email(setting,Files_path) #发送邮件


if __name__ == '__main__':
    run()
