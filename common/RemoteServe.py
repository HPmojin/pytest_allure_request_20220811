#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : RemoteServe.py
# @Time : 2022-08-12 13:12
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
'''
备份数据库
mysqldump -h127.0.0.1 -uroot -proot mydb > /usr/local/mysql8/mydbDataBackup/mydb_bak.sql
mysqldump -h127.0.0.1 -uroot -proot mydb > D:/mydb.sql
mysqldump -h127.0.0.1 -uroot -proot mydb > D:/mydb.sql
还原
mysql -h127.0.0.1 -uroot -proot mydb< /usr/local/mysql8/mydbDataBackup/mydb_bak.sql
mysql -h127.0.0.1 -uroot -proot mydb< D:/mydb.sql

'''

import paramiko

import os,time
from copy import deepcopy
from datetime import datetime
from common.logger import Logger



class RemoteServe:
    """远程服务器"""

    def __init__(self,ssh_server, db_info):

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
        try:
            # 进行SSH连接
            self.trans = paramiko.Transport((self.ssh_host, self.ssh_port))

            if self.ssh_pwd is None:
                self.trans.connect(
                    username=self.ssh_user,
                    pkey=paramiko.RSAKey.from_private_key_file(
                        self.private_key_file, self.private_password
                    ),
                )
            else:
                self.trans.connect(username=self.ssh_user , password=self.ssh_pwd ,)
            # 将sshclient的对象的transport指定为以上的trans
            self.ssh = paramiko.SSHClient()
            Logger.info("SSH客户端创建成功.")
            self.ssh._transport = self.trans
            # 创建SFTP客户端
            self.ftp_client = paramiko.SFTPClient.from_transport(self.trans)
            Logger.info("SFTP客户端创建成功.")
        except Exception as e:
            Logger.error('SSH远程服务链接失败！！（%s）'%e)
            raise

    def execute_cmd(self, cmd: str,docs):
        """
        :param cmd: 服务器下对应的命令
        """
        try:
            Logger.info(f"{docs}-输入命令: {cmd}")
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            error = stderr.read().decode()
            Logger.info(f"{docs}-输出结果: {stdout.read().decode()}")
            Logger.warning(f"{docs}-异常信息: {error}")
        except Exception as e:
            error=str(e)
            Logger.warning(f"{docs}-异常信息: {error}")
        return error
    def files_action(
        self, post: bool, local_path: str = os.getcwd(), remote_path: str = "/root",docs=''
    ):
        """
        :param post: 动作 为 True 就是上传， False就是下载
        :param local_path: 本地的文件路径， 默认当前脚本所在的工作目录
        :param remote_path: 服务器上的文件路径，默认在/root目录下
        """
        if post:  # 上传文件
            self.execute_cmd(f"mkdir {remote_path}",docs=f'创建{remote_path}目录') #传教要备份的保存目录
            remotepath=os.path.join(remote_path,os.path.split(local_path)[1])
            self.ftp_client.put(
                localpath=local_path,
                remotepath=remotepath,
            )
            Logger.info(
                f"{docs}-文件上传成功: {local_path} -> {self.ssh_host}:{remote_path}{os.path.split(local_path)[1]}"
            )
        else:  # 下载文件
            if not os.path.exists(local_path):
                os.mkdir(local_path)
            file_path = local_path + os.path.split(remote_path)[1]
            self.ftp_client.get(remotepath=remote_path, localpath=file_path)
            Logger.info(f"{docs}-文件下载成功: {self.ssh_host}:{remote_path} -> {file_path}")

    def ssh_close(self):
        """关闭连接"""
        self.trans.close()
        Logger.info("已关闭SSH连接...")



