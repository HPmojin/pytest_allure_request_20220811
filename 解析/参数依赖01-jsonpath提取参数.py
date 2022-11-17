#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : 参数依赖01-jsonpath提取参数.py
# @Time : 2022-08-08 15:52
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------
import jsonpath
import random
#使用 jsonpath
dic_data={
    "data": {
        "goods_id": 958,
        "cat_id": 3,
        "goods_name": "商品_9970",
        "goods_price": 20,
        "goods_number": 30,
        "goods_weight": 40,
        "goods_introduce": "null",
        "goods_big_logo": "",
        "goods_small_logo": "",
        "goods_state":  "null",
        "is_del": "0",
        "add_time": 1668662557,
        "upd_time": 1668662557,
        "delete_time":  "null",
        "hot_mumber": 0,
        "is_promote":  "null",
        "cat_one_id": 1,
        "cat_two_id": 2,
        "cat_three_id": 3,
        "goods_cat": "1,2,3",
        "pics": [],
        "attrs": [
            {
                "goods_id": 958,
                "attr_id": 15,
                "attr_value": "dderd",
                "add_price":  "null",
                "attr_name": "主观参数-品牌",
                "attr_sel": "only",
                "attr_write": "manual",
                "attr_vals": ""
            },
            {
                "goods_id": 958,
                "attr_id": 15,
                "attr_value": "324",
                "add_price":  "null",
                "attr_name": "主观参数-品牌",
                "attr_sel": "only",
                "attr_write": "manual",
                "attr_vals": ""
            }
        ]
    },
    "meta": {
        "msg": "获取成功",
        "status": 200
    }
}

jsonpath_v=jsonpath.jsonpath(dic_data,"$..status")#msg   "$..data..id"
print(jsonpath_v)
print(jsonpath_v[random.randint(0,len(jsonpath_v)-1)])



# extract_data={}
#
# josn_path_dic={"email": "$..email","token":"$.data.token","mobile":"$.data.mobile"}
# for k,v in josn_path_dic.items():
#
#     extract_data[k]=jsonpath.jsonpath(dic_data, v)[0]
#
# print(extract_data)
# for k, v in josn_path_dic.items():
#
#     extract_data[k]=(jsonpath.jsonpath(dic_data, v)[0])
#
# print(extract_data)
