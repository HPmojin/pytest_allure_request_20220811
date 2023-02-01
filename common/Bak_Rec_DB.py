#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : Bak_Rec_DB.py
# @Time : 2022-08-12 13:12
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
import os
from common.RemoteServe import RemoteServe

'''
操作备份恢复数据库
'''


class BakRecDB(RemoteServe):

    def __init__(self,
        host,
        port,
        username,
        password,
        mysql_info,
        sql_data_file,
        sql_upload_file,
        private_key_file = None,
        private_password = None):

        super().__init__(
                        host,
                        port,
                        username,
                        password,
                        private_key_file = private_key_file,
                        private_password = private_password)  # 需要调用父类中的init函数
        self.ssh_host=host
        self.ssh_port=port
        self.ssh_username=username
        self.ssh_password=password

        self.sql_data_file=sql_data_file #sql文件备份的文件夹
        self.sql_upload_file=sql_upload_file #本地初始化测试前要恢复测试数据库的sql文件
        self.private_key_file =private_key_file
        self.private_password =private_password



        self.msqyl_host=mysql_info['host']
        self.msqyl_port=mysql_info['port']
        self.msqyl_username=mysql_info['user']
        self.msqyl_password=mysql_info['password']
        self.msqyl_db_name=mysql_info['db_name']
        self.msqyl_charset=mysql_info.get('charset', 'utf8mb4')

        #链接数据库拼接
        self.Link_db=f'-h{self.msqyl_host} -u{self.msqyl_username} -p{self.msqyl_password} -P{self.msqyl_port} {self.msqyl_db_name}'

    def backups_sql(self):# 链接ssh远程访问，上传测试sql数据，备份当前数据库，导入测试sql库，
        # self.files_action(post=True, local_path='./config/mydb.sql',
        #                 remote_path='/mnt/backup_sql/', docs='本地sql')  # 上传本地sql文件到数据库服务器
        self.files_action(post=True, local_path=self.sql_upload_file,
                        remote_path=self.sql_data_file, docs='本地sql')  # 上传本地sql文件到数据库服务器

        #Logger.info(f'备份当前数据库：mysqldump {self.Link_db} > {self.sql_data_file}/{self.msqyl_db_name}_bak.sql')
        (self.execute_cmd(
            f'mysqldump {self.Link_db} > {self.sql_data_file}/{self.msqyl_db_name}_bak.sql', docs='备份当前数据库'))  # 备份当前数据库数据
        # mysqldump -h127.0.0.1 -uroot -proot -P3306 mydb>mydb_bak.sql
        #mysql -h127.0.0.1 -uroot -proot -P3306 mydb <mydb_bak.sql

        # mysqldump -h127.0.0.1 -uroot -p123456 -P3306 ar_metro >ar_myb.sql
        #mysql -h127.0.0.1 -uroot -p123456 -P3306 ar_metro <ar_myb.sql
        #Logger.info(f'恢复上传sql库数据：mysql {self.Link_db} < {self.sql_data_file}{os.path.split(self.sql_upload_file)[1]}')

        upload_sql_path = os.path.join(self.sql_data_file, os.path.split(self.sql_upload_file)[1])
        (self.execute_cmd(f'mysql {self.Link_db} < {upload_sql_path}', docs='恢复上传sql库数据'))  # 恢复上传数据库数据
        #self.ssh_close()

    def recovery_sql(self):##恢复测试前sql数据，关闭ssh链接
        #Logger.info(f'测试完成恢复备份sql数据：mysql {self.Link_db} < {self.sql_data_file}/{self.msqyl_db_name}_bak.sql')

        (self.execute_cmd(
            f'mysql {self.Link_db} < {self.sql_data_file}/{self.msqyl_db_name}_bak.sql', docs='测试完成恢复备份sql数据'))  # 恢复备份数据
        #self.ssh_close()

