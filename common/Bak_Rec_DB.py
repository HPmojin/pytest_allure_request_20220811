#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : Bak_Rec_DB.py
# @Time : 2022-08-12 13:12
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
from common.read_file import ReadFile
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
        private_key_file = None,
        private_password = None,):

        super().__init__(host,
                        port,
                        username,
                        password,
                        private_key_file = private_key_file,
                        private_password = private_password,)  # 需要调用父类中的init函数


    def backups_sql(self):# 链接ssh远程访问，上传测试sql数据，备份当前数据库，导入测试sql库，
        self.files_action(post=True, local_path='./config/mydb.sql',
                        remote_path='/mnt/backup_sql/', docs='本地sql')  # 上传本地sql文件到数据库服务器

        (self.execute_cmd(
            'mysqldump -h127.0.0.1 -uroot -proot mydb > /usr/local/mysql8/mydbDataBackup/mydb_bak.sql', docs='备份当前数据库'))  # 备份当前数据库数据

        (self.execute_cmd('mysql -h127.0.0.1 -uroot -proot mydb < /mnt/backup_sql/mydb.sql', docs='恢复上传sql库数据'))  # 恢复上传数据库数据
        self.ssh_close()



    def recovery_sql(self):##恢复测试前sql数据，关闭ssh链接
        (self.execute_cmd(
            'mysql -h127.0.0.1 -uroot -proot mydb < /usr/local/mysql8/mydbDataBackup/mydb_bak.sql', docs='恢复备份sql数据'))  # 恢复备份数据
        self.ssh_close()

