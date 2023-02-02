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
import pytest,random,os
import pytest,time
from common.logger import Logger
from common.Bak_Rec_DB import BakRecDB
from common.read_file import ReadFile
from common.read_exce_yaml_caes import get_yaml_excle_caes


cmdopt_env=''

#命令行传参addoption 在contetest.py添加命令行选项,命令行传入参数”—cmdopt“, 用例如果需要用到从命令行传入的参数，就调用cmdopt函数：
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test", help=None)

@pytest.fixture(scope='session',autouse=True)
def Acmdopt(pytestconfig):
    # 两种写法

    global  Acmdopt_env

    Acmdopt_env=pytestconfig.getoption("--env")

    os.environ["Acmdopt_env"] = Acmdopt_env  # 写入系统变量

    return Acmdopt_env
    # return pytestconfig.option.cmdopt

@pytest.fixture(scope='session',autouse=True)
def env_url(Acmdopt):#读取数据源文件
    url = ReadFile.read_config('$.server.%s'%Acmdopt)#  $..test
    Logger.warning('执行环境为：【%s】 %s' %(Acmdopt_env,url))

    return [url,Acmdopt]



@pytest.fixture(scope='session')  #读取数据库查询断言
def get_db(Acmdopt):
    assert_db = ReadFile.read_config('$.Operations_db.assert_db')
    db_info = dict(ReadFile.read_config('$.database.%s'%Acmdopt))
    if assert_db:#判断是否查询数据库断言
        db=DB(db_info)
    else:
        db=None

    yield db

    if assert_db:#判断是否查询数据库断言
        db.close()




#备份恢复数据库
@pytest.fixture(scope='session',autouse=True)#False True   autouse=False 为True时开启数据库备份恢复功能，为False时不开启备份恢复功能
def ConnectingRemoteServices(Acmdopt):
    #获取配置文件中的远程服务器和数据库参数
    ssh_server = dict(ReadFile.read_config('$.ssh_server.%s'%Acmdopt))
    db_info = dict(ReadFile.read_config('$.database.%s'%Acmdopt))

    backup_db = ReadFile.read_config('$.Operations_db.backup')

    if backup_db:
        BR = BakRecDB(ssh_server,db_info)  # 初始化链接服务器
        BR.backups_sql()  # 链接ssh远程访问，上传测试sql数据，备份当前数据库，导入测试sql库，
        BR.ssh_close()

    yield

    recovery_db = ReadFile.read_config('$.Operations_db.recovery')
    if recovery_db:
        BR = BakRecDB(ssh_server,db_info)  # 初始化链接服务器
        BR.recovery_sql()  # 恢复测试前sql数据，关闭ssh链接
        BR.ssh_close()


##@pytest.fixture(scope='session')#False True   autouse=False
def read_cases(Acmdopt):
    global data
    data=get_yaml_excle_caes(Acmdopt)
    Logger.info(data)

    return data
#cmdopt_env='test'

#@pytest.fixture(params=get_yaml_excle_caes(os.getenv("Acmdopt_env")))
def cases(request,Acmdopt):
    """用例数据，测试方法参数入参该方法名 cases即可，实现同样的参数化
    目前来看相较于@pytest.mark.parametrize 更简洁。

    """
    Logger.info(request.param)
    return request.param


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
#
# def pytest_itemcollected(item):#要不要这个函数都行 不用需要再用例的历史中看 ，  使用这个函数 所有执行全部显示处理
#     item._nodeid = str(random.randint(1, 1000)) + '_' + item . _nodeid