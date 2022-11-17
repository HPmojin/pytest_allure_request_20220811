#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/11 20:28
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : read_exce_yaml_caes.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from common.read_file import ReadFile
import os
from common.operation_excle import operation_excle
def get_yaml_all_caes(yaml_file):#获取yaml文件中的所有用例
    get_all_yaml = ReadFile.read_config(yaml_file)  # 获取存放yaml文件目录路径
    yaml_path_all = []  # 收集所有的yaml文件路径
    for i in os.listdir(get_all_yaml):
        if (i.split('.')[-1] in ['yaml']):
            yaml_path_all.append(os.path.join(get_all_yaml, i))

    all_yaml_case = []  # 收集所有用例
    for one_caselist_path in yaml_path_all:
        title = one_caselist_path.split('/')[-1].split('.')[0]
        for one_case in ReadFile.get_case_data_yaml(one_caselist_path):
            (one_case.insert(0, title))  # .insert(0,title)
            all_yaml_case.append(one_case)

    return all_yaml_case

def get_yaml_excle_caes():#get_all_yaml_excle_caes  #获取yaml和excle用例，用例；yaml和excle累计所有
    test_case_type = (ReadFile.read_config('$.test_case_type'))

    test_case_type = sorted(test_case_type, key=lambda test_case_type: test_case_type['order'], reverse=False)
    all_yaml_xlsx_caes = []
    for case_type in test_case_type:
        if case_type["read"]:
            if case_type['file'] == "yaml":
                yaml_file = '$..test_case_yaml'
                all_yaml_xlsx_caes = all_yaml_xlsx_caes + get_yaml_all_caes(yaml_file)
            elif case_type['file'] == "xlsx":
                excle_all_case = operation_excle.read_excel(ReadFile.read_config('$..test_case_xlsx'),
                                                            ReadFile.read_config('$..case_severity'))
                all_yaml_xlsx_caes = all_yaml_xlsx_caes + excle_all_case
    return all_yaml_xlsx_caes




