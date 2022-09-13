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