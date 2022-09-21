#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/24 21:06
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : conftest.py
# @Software: PyCharm
#-------------------------------------------------------------------------------

from common.db import DB

import pytest
import pytest,time
from common.logger import Logger
from common.Bak_Rec_DB import BakRecDB
from common.read_file import ReadFile

@pytest.fixture(scope='session')
def get_db():

    db=DB()
    yield db
    db.close()





#备份恢复数据库
@pytest.fixture(scope='session',autouse=False)#False True
def BakRecDB():
    #获取配置文件中的远程服务器和数据库参数
    host = ReadFile.read_config('$.database.host')
    ssh_port = ReadFile.read_config('$.database.ssh_server.port')
    ssh_user = ReadFile.read_config('$.database.ssh_server.username')
    ssh_pwd = ReadFile.read_config('$.database.ssh_server.password')
    sql_data_file = ReadFile.read_config('$.database.ssh_server.sql_data_file')


    BR=BakRecDB(host=host, port=ssh_port, username=ssh_user, password=ssh_pwd) #初始化链接服务器
    BR.backups_sql()  # 链接ssh远程访问，上传测试sql数据，备份当前数据库，导入测试sql库，
    yield
    BR.recovery_sql()  # 恢复测试前sql数据，关闭ssh链接


def pytest_terminal_summary(terminalreporter):
    """
    收集测试结果
    """

    _PASSED = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    _ERROR = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    _FAILED = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    _SKIPPED = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    _TOTAL = terminalreporter._numcollected
    _TIMES = time.time() - terminalreporter._sessionstarttime
    Logger.error(f"用例总数: {_TOTAL}")
    Logger.error(f"异常用例数: {_ERROR}")
    Logger.error(f"失败用例数: {_FAILED}")
    Logger.warning(f"跳过用例数: {_SKIPPED}")
    Logger.info("用例执行时长: %.2f" % _TIMES + " s")

    try:
        _RATE = _PASSED / _TOTAL * 100
        Logger.info("用例成功率: %.2f" % _RATE + " %")
    except ZeroDivisionError:
        Logger.info("用例成功率: 0.00 %")
