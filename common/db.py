#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : db.py
# @Time : 2022-08-12 13:08
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------

import psycopg2
import json,decimal
from datetime import datetime
from typing import Union

import pymysql
from common.logger import Logger
from psycopg2 import extras  # 不能少
from common.read_file import ReadFile
import datetime

class DB:



    def __init__(self ,db_info,):

        """
        初始化数据库连接，并指定查询的结果集以字典形式返回
        """
        self.charset='utf8mb4'
        self.db_type=db_info.get('db_type', 'mysql')

        try:
            if self.db_type=='mysql':
                self.connection = pymysql.connect(
                    **db_info['data'],
                    charset=self.charset,
                    cursorclass=pymysql.cursors.DictCursor
                )
            elif self.db_type=='postgresql':
                self.connection = psycopg2.connect( **db_info['data'],)
        except Exception as e:
            Logger.error("数据库链接失败！！（%s）"%e)
            #raise

    def execute_sql(self, sql: str) -> Union[dict, None]:
        """
        执行sql语句方法，查询所有结果的sql只会返回一条结果（
        比如说： 使用select * from cases , 结果将只会返回第一条数据    {'id': 1, 'name': 'updatehahaha', 'path': None, 'body': None, 'expected': '{"msg": "你好"}', 'api_id': 1, 'create_at': '2021-05-17 17:23:54', 'update_at': '2021-05-17 17:23:54'}

        ），支持select， delete， insert， update
        :param sql: sql语句
        :return: select 语句 如果有结果则会返回 对应结果字典，delete，insert，update 将返回None
        """
        if self.db_type=='mysql':
            with self.connection.cursor() as cursor:
                try:
                    Logger.info(sql)
                    cursor.execute(sql)
                    #print(cursor.fetchall()) #fetchone
                    result = cursor.fetchone()
                    if result==None:
                        result={}
                    Logger.info(result)
                except Exception as e:
                    Logger.error('数据库查询数据出错！！（%s）'%str(e))
                    #result={'error':str(e)}
                    result = {}
                cursor.close()

        elif self.db_type == 'postgresql':
                with self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                    try:
                        Logger.info(sql)
                        cursor.execute(sql)
                        # print(cursor.fetchall()) #fetchone
                        result = cursor.fetchall()
                        if result==[]:
                            result={}
                        else:
                            result=dict(result[0])
                        Logger.info(result)
                    except Exception as e:
                        Logger.error('数据库查询数据出错！！（%s）' % str(e))
                        # result={'error':str(e)}
                        result = {}

                    cursor.close()

        # 使用commit解决查询数据出现概率查错问题

        self.connection.commit()
        return self.verify(result)



    def verify(self, value):
        """验证结果能否被json.dumps序列化"""
        # 尝试变成字符串，解决datetime 无法被json 序列化问题
        try:
            json.dumps(value)
        except TypeError:# TypeError: Object of type datetime is not JSON serializable
            for k, v in value.items():
                if isinstance(v, decimal.Decimal):
                    value[k] = str(v)
                elif isinstance(v, datetime.datetime):
                    value[k] = str(v) #.split('.')[0]

        return value

    def close(self):
        """关闭数据库连接"""
        self.connection.close()

