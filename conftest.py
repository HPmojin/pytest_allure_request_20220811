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

@pytest.fixture(scope='session')
def get_db():

    db=DB()
    yield db
    db.close()





#备份恢复数据库
@pytest.fixture(scope='session',autouse=False)#False True
def BakRecDB():
    from common.Bak_Rec_DB import BakRecDB
    # BakRecDB().backups_sql()
    # BakRecDB().recovery_sql()
    BakRecDB().backups_sql()
    yield
    BakRecDB().recovery_sql()


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
