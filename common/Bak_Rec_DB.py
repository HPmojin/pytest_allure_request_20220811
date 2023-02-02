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

    def __init__(self,ssh_server, db_info):



        super().__init__( ssh_server,db_info)  # 需要调用父类中的init函数
        self.ssh_host = ssh_server['host']
        self.ssh_port = ssh_server['port']
        self.ssh_user = ssh_server['username']
        self.ssh_pwd = ssh_server['password']
        self.private_key_file= ssh_server['private_key_file']
        self.private_password= ssh_server['private_passowrd']
        self.mysql_container=ssh_server['mysql_container']
        self.sql_data_file = ssh_server['sql_data_file']
        self.sql_upload_file = ssh_server['sql_upload_file']

        '''
            # 私有密钥文件路径
            private_key_file: ''
            # 私钥密码
            privat_passowrd: ''
            # 如果使用的docker容器部署mysql服务，需要传入mysql的容器id/name
            mysql_container:
            # 数据库备份文件导出的本地路径, 需要保证存在该文件夹下   ./backup_sqls/
            sql_data_file: /mnt/backup_sql/  #  /mnt/backup_sql/
            #上传本地已初始化好的数据库sql文件，恢复到测试数据库进行测试
            sql_upload_file: ./config/mydb.sql
        '''


        self.msqyl_host=db_info['host']
        self.msqyl_port=db_info['port']
        self.msqyl_username=db_info['user']
        self.msqyl_password=db_info['password']
        self.msqyl_db_name=db_info['db_name']
        self.msqyl_charset=db_info.get('charset', 'utf8mb4')

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

