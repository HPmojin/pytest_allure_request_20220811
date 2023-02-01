#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest_allure_request_SuiAnYun
# @Time    : 2022/11/9 10:33
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : hook.py
# @Software: PyCharm
# -------------------------------------------------------------------------------
from faker import Faker
import time
from common.logger import Logger
fk = Faker("zh_CN") # https://blog.csdn.net/weixin_43865008/article/details/115492280
import random
def uuid4():
    return fk.uuid4()

def Times():
    #fk.date_between_dates()
    #fk.date_object()
    return fk.date_between_dates()


def list_random_index(lists_s):
    #fk.date_between_dates()
    #fk.date_object()
    Logger.error(lists_s)
    Logger.error(type(lists_s))
    return random.randint(0,len(lists_s)-1)

def waits(t):

    time.sleep(t)
    Logger.warning('sleep %s s'%t)

    return 'sleep %s s'%t


def api_mame(singleBatch,stockId='',skuId=''):#singleBatch=False

    dic_data={
        "True":'verifySkuSingleBatch',
        "False":"listSkuBatch"

    }
    dic_data2={
        # "True":{"operationName":"listCommodityLabel",
        #         "variables":
        #             {"input":
        #                  {"batchIds":[stockId]#stockId=767749550510538753
        #                   }
        #              },
        #         "query":"query listCommodityLabel($input: CommodityLabelInput) {\n  listCommodityLabel(input: $input) {\n    id\n    type\n    typeDesc\n    name\n    categoryId\n    categoryName\n    remark\n    status\n  }\n}"},

        "False":{"operationName":"listSkuBatch",
                 "variables":
                     {"input":
                          {"skuId":int(skuId)
                           }
                      },
                 "query":"query listSkuBatch($input: SkuBatchInput) {\n  listSkuBatch(input: $input) {\n    stockId\n    commoditySkuName\n    commodityCategoryId\n    commoditySkuId\n    commoditySpuId\n    stock {\n      skuId\n      basicType\n      subType\n      basicQuantity\n      subQuantity\n    }\n    inStockTime\n    warehouseId\n    warehouseType\n    warehouseName\n    carNo\n    cabinetCode\n    shoppingCarNum\n    quantityUnitType\n    unitPrice\n    trailerCarNo\n    temporaryStatus\n    refundMarksStatus\n    unitConversion {\n      skuId\n      basicType\n      subType\n      basicTypeRatio\n      subTypeRatio\n    }\n    disable\n    guidePrice\n    guidePriceUnitId\n    saleMark\n    belongOwner\n  }\n}"}

    }

    return dic_data2[singleBatch]

# def api_mame3(api_ma):#singleBatch=False
#
#     dic_data={
#         "verifySkuSingleBatch":'VerifySkuSingleBatch',
#         "listSkuBatch":"SkuBatch"
#
#     }
#
#     return dic_data[api_ma]