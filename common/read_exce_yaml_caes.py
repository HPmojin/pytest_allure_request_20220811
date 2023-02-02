#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest_allure_request_20220811
# @Time    : 2022/11/19 20:12
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : read_exce_yaml_caes.py
# @Software: PyCharm
# -------------------------------------------------------------------------------


from common.read_file import ReadFile
import os
from common.operation_excle import operation_excle
from common.logger import Logger
def get_yaml_all_caes(yaml_file):#获取yaml文件中的所有用例
    get_all_yaml = ReadFile.read_config(yaml_file)  # 获取存放yaml文件目录路径
    case_severity_list = ReadFile.read_config('$..case_severity')
    yaml_path_all = []  # 收集所有的yaml文件路径

    for i in os.listdir(get_all_yaml):
        if (i.endswith(('yaml'))):
            yaml_path_all.append(os.path.join(get_all_yaml, i))

    all_yaml_case = []  # 收集所有用例
    for one_caselist_path in yaml_path_all:
        title = one_caselist_path.split('/')[-1].split('.')[0]
        for one_case in ReadFile.get_case_data_yaml(one_caselist_path):
            (one_case.insert(0, title))  # .insert(0,title)
            if one_case[5] in case_severity_list:  # 筛选匹配的用例等级进行测试
                all_yaml_case.append(one_case)

    return all_yaml_case


def get_excle_all_caes(excle_file):#获取excle文件中的所有用例
    get_all_excle = ReadFile.read_config(excle_file)  # 获取存放excle文件目录路径
    excle_path_all = []  # 收集所有的excle文件路径

    for i in os.listdir(get_all_excle):
        if (i.endswith(('xlsx','xls'))):
            excle_path_all.append(os.path.join(get_all_excle, i))

    all_excle_case = []  # 收集所有用例
    for one_excle_path in excle_path_all:

        try:
            one_excle_case = operation_excle.read_excel(one_excle_path,
                                                        ReadFile.read_config('$..case_severity'))
        except Exception as e:
            Logger.warning('这个文件【%s】无法读取,原因:“%s”,关闭excle再试试…… '%(one_excle_path,e))
            one_excle_case=[]
        all_excle_case=all_excle_case+one_excle_case


    return all_excle_case

def get_yaml_excle_caes(cmdopt_env):# get_all_yaml_excle_caes  #获取yaml和excle用例，用例；yaml和excle累计所有
    #cmdopt_env='test'
    #Logger.error(cmdopt_env)
    test_case_type = (ReadFile.read_config('$.test_case_type.%s'%cmdopt_env))
    #test_case_type = (ReadFile.read_config('$.test_case_type' ))

    test_case_type = sorted(test_case_type, key=lambda test_case_type: test_case_type['order'], reverse=False)

    all_yaml_xlsx_caes = []
    for case_type in test_case_type:
        if case_type["read"]:
            if case_type['file'] == "yaml":
                all_yaml_xlsx_caes = all_yaml_xlsx_caes + get_yaml_all_caes(case_type['test_case'])
            elif case_type['file'] == "xlsx":
                all_yaml_xlsx_caes = all_yaml_xlsx_caes + get_excle_all_caes(case_type['test_case'])

    return all_yaml_xlsx_caes








