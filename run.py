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


    # EmailServe.zip_report('./target/allure-report', 'allure-report.zip') #压缩打包测试报告
    # file_path='allure-report.zip' #生成压缩包路径
    # setting = ReadFile.read_config('$.email') #获取邮件相关信息
    # EmailServe.send_email(setting,file_path) #发送邮件


if __name__ == '__main__':
    run()
