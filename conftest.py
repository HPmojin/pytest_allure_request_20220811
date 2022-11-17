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
from common.exchange_data import ExchangeData
import pytest
import pytest,time
from common.logger import Logger
from common.Bak_Rec_DB import BakRecDB
from common.read_file import ReadFile



#命令行传参addoption 在contetest.py添加命令行选项,命令行传入参数”—cmdopt“, 用例如果需要用到从命令行传入的参数，就调用cmdopt函数：
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test", help=None)

@pytest.fixture(scope='session')
def cmdopt(pytestconfig):
    # 两种写法

    #global parameter_data
    parameter_data=(pytestconfig.getoption("--env"))
    return parameter_data
    # return pytestconfig.option.cmdopt

@pytest.fixture(scope='session')
def env_url(cmdopt):#读取数据源文件
    url = ReadFile.read_config('$..%s'%cmdopt)

    return url



@pytest.fixture(scope='session')  #读取数据库查询断言
def get_db():
    assert_db = ReadFile.read_config('$.Operations_db.assert_db')
    if assert_db:#判断是否查询数据库断言
        db=DB()
    else:
        db=None
    yield db
    db.close()




#备份恢复数据库
@pytest.fixture(scope='session',autouse=True)#False True   autouse=False 为True时开启数据库备份恢复功能，为False时不开启备份恢复功能
def ConnectingRemoteServices():
    #获取配置文件中的远程服务器和数据库参数
    host = ReadFile.read_config('$.database.host')
    ssh_port = ReadFile.read_config('$.database.ssh_server.port')
    ssh_user = ReadFile.read_config('$.database.ssh_server.username')
    ssh_pwd = ReadFile.read_config('$.database.ssh_server.password')
    sql_data_file = ReadFile.read_config('$.database.ssh_server.sql_data_file')

    backup_db = ReadFile.read_config('$.Operations_db.backup')

    if backup_db:
        BR = BakRecDB(host=host, port=ssh_port, username=ssh_user, password=ssh_pwd)  # 初始化链接服务器
        BR.backups_sql()  # 链接ssh远程访问，上传测试sql数据，备份当前数据库，导入测试sql库，

    yield

    recovery_db = ReadFile.read_config('$.Operations_db.recovery')
    if recovery_db:
        BR = BakRecDB(host=host, port=ssh_port, username=ssh_user, password=ssh_pwd)  # 初始化链接服务器
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
    Logger.info(f"用例总数: {_TOTAL}")
    Logger.success(f"通过用例: {_PASSED}")
    Logger.error(f"异常用例数: {_ERROR}")
    Logger.error(f"失败用例数: {_FAILED}")
    Logger.warning(f"跳过用例数: {_SKIPPED}")
    Logger.info(f"用例执行时长: {round(_TIMES, 2)} s")
    try:
        _RATE = _PASSED / _TOTAL * 100

        _SUCCESS_RATE=round(_RATE, 2)

    except ZeroDivisionError:
        _SUCCESS_RATE="0.00"
    Logger.info(f"用例成功率:{_SUCCESS_RATE}")
    result_data_test={
        "_TOTAL": f"{_TOTAL}",
        '_PASSED':f"{_PASSED}",
        "_ERROR": f" {_ERROR}",
        "_FAILED": f" {_FAILED}",
        "_SKIPPED": f" {_SKIPPED}",
        "_TIMES": f"{round(_TIMES, 2)} s",
        "_SUCCESS_RATE": f"{_SUCCESS_RATE}",
    }
    ExchangeData.post_pytest_summary(result_data_test)#测试结果添加到变量池
    with open("result.txt", "w") as fp:#测试结果保存到本地result.txt
        fp.write("_TOTAL=%s" % _TOTAL + "\n")
        fp.write("_PASSED=%s" % _PASSED + "\n")
        fp.write("_FAILED=%s" % _FAILED + "\n")
        fp.write("_ERROR=%s" % _ERROR + "\n")
        fp.write("_SKIPPED=%s" % _SKIPPED + "\n")
        fp.write("_SUCCESS_RATE=%.2f%%" % _SUCCESS_RATE + "\n")
        fp.write("_TIMES=%.2fs" % _TIMES)

