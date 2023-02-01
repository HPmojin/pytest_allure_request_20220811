# _*_coding:utf-8 _*_
# @Time　　:2021/6/19 22:50
# @Author : mojin
# @Email : 397135766@qq.com
# @File　　  :all_path.py
# @Software  :PyCharm
import os

base_path = os.path.dirname(os.path.dirname(__file__))

appPath = os.path.join(base_path, 'app')
dataPath = os.path.join(base_path, 'data')
configPath = os.path.join(base_path, 'config')
logPath = os.path.join(base_path,  'logs')
picturePath = os.path.join(base_path, 'png')
reportsPath = os.path.join(base_path, 'target', 'allure-report')
screenPath = os.path.join(base_path,  'screencap')
targetPath=os.path.join(base_path, 'target')
Start_server_bat=os.path.join(base_path, 'config',"Start_server.bat")
images_Path=os.path.join(base_path, 'config',"png") #./config/png
