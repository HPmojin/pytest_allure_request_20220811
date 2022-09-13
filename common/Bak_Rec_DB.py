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

host = ReadFile.read_config('$.database.host')
ssh_port = ReadFile.read_config('$.database.ssh_server.port')
ssh_user = ReadFile.read_config('$.database.ssh_server.username')
ssh_pwd = ReadFile.read_config('$.database.ssh_server.password')
sql_data_file = ReadFile.read_config('$.database.ssh_server.sql_data_file')

RS = RemoteServe(host=host, port=ssh_port, username=ssh_user, password=ssh_pwd)

class BakRecDB():

    def backups_sql(self):
        RS.files_action(post=True, local_path='./config/mydb.sql',
                        remote_path='/mnt/backup_sql/', docs='本地sql')  # 上传本地sql文件到数据库服务器

        (RS.execute_cmd(
            'mysqldump -h127.0.0.1 -uroot -proot mydb > /usr/local/mysql8/mydbDataBackup/mydb_bak.sql', docs='备份当前数据库'))  # 备份当前数据库数据

        (RS.execute_cmd('mysql -h127.0.0.1 -uroot -proot mydb < /mnt/backup_sql/mydb.sql', docs='恢复上传sql库数据'))  # 恢复上传数据库数据 初始化数据库




    def recovery_sql(self):
        (RS.execute_cmd(
            'mysql -h127.0.0.1 -uroot -proot mydb < /usr/local/mysql8/mydbDataBackup/mydb_bak.sql', docs='恢复备份sql数据'))  # 恢复备份数据
        RS.ssh_close()

# BakRecDB().backups_sql()
# BakRecDB().recovery_sql()