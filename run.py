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

def run():
    try:
        shutil.rmtree('./target')
    except:
        pass

    pytest.main(['./test_caes','-vs',"--alluredir","target/allure-results"])
    allure_html = 'allure generate ./target/allure-results -o ./target/allure-report --clean'  # 生成allure的html报告

    subprocess.call(allure_html, shell=True)  # 生成allure的html报告



if __name__ == '__main__':
    run()
