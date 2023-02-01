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
from shutil import copy
from common.read_file import ReadFile
from common.send_email import EmailServe
from common.all_path import targetPath,Start_server_bat
from common.exchange_data import ExchangeData

def run():

    setting = ReadFile.read_config('$.email') #获取邮件相关配置信息
    try:
        shutil.rmtree('./target') #删除allure历史数据
    except:
        pass

    pytest.main(['./test_caes','-vs',"--env=test","--alluredir","target/allure-results"])#pytest测试框架主程序运行
    allure_html = 'allure generate ./target/allure-results -o ./target/allure-report --clean'  # 生成allure的html报告
    subprocess.call(allure_html, shell=True)  # 生成allure的html报告

    copy(Start_server_bat, targetPath) #拷贝 启动服务器脚本(config/Start_server.bat)，由config目录拷贝到target目录下进行压缩打包发送邮件

    Files_path='./target'#压缩打包的目录
    #EmailServe.send_email(setting,Files_path,ExchangeData.get_pytest_summary()) #发送邮件


if __name__ == '__main__':
    run()
