#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/16 21:01
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : te_09.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import os

path = r"C:\Users\huangpeng\Pictures\Camera Roll"

for root, dirs, files in os.walk(path):
    #print(root, dirs, files)
    print(dirs)
    #
    # print("root:", root)
    # print("dirs:", dirs)
    # print("files", files)
