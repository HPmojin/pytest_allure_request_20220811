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
            "getOrderInfo": {
                "orderId": 20861,
                "customerInfo": {
                    "id": "1510",
                    "name": "测试认证3",
                    "alias": "",
                    "phone": "13688889966",
                    "type": "PERSONAL",
                    "customerContact": [{
                        "id": 0,
                        "name": "",
                        "phone": "",
                        "alias": "",
                        "contactUserId": None,
                        "userStatus": None,
                        "realNameAuth": False,
                        "realNameAuthStatus": "NOT_CERTIFICATED"
                    }],
                    "creditLine": 999.0,
                    "availableAmount": 999.0,
                    "overdueDay": None,
                    "creditPeriod": 1,
                    "creditPeriodStatusEnum": "ENABLE",
                    "signAgreement": 1,
                    "attribute": "EXTERNAL",
                    "realNameAuth": True,
                    "realNameAuthStatus": "UNDER_CERTIFICATION",
                    "creditConfigurationInfo": {
                        "maxCreditPeriod": 51,
                        "maxCreditLine": 1000000.55,
                        "overdueManagement": "UNLIMITED",
                        "overdueLimit": "UNLIMITED",
                        "salesTypePeriodLimit": "UNLIMITED",
                        "moderateSalesLimitDays": 0
                    }
                },
                "status": "UNPAID",
                "statusDesc": "待收银",
                "abnormalOrderStatus": "UNNECESSARY",
                "abnormalOrderStatusDesc": "无需确认",
                "paymentCode": "9758",
                "totalAmount": 30.0,
                "paidAmount": 0.0,
                "payableAmount": 20.0,
                "discountAmount": 10.0,
                "orderCode": "1675000483468514105",
                "orderTime": 1675000483483,
                "paymentTime": 0,
                "orderOperation": "乌6",
                "orderCommodities": [{
                    "commoditySkuName": "云南鲜核桃净75Kg/件",
                    "commoditySkuId": 154005,
                    "commoditySkuCount": 1,
                    "commoditySkuQuantity": 3.0,
                    "commoditySkuAmount": 30.0,
                    "orderCommodityDetails": [{
                        "quantity": 3.0,
                        "unitPrice": 10.0,
                        "enterTime": 1673532334706,
                        "warehouseName": "测试仓库1",
                        "skuTotalAmount": 30.0,
                        "toPickQuantity": 3.0,
                        "pickRecord": [],
                        "batchId": "830429641819389956",
                        "quantityUnitType": 1,
                        "convertQuantity": 0.0,
                        "convertQuantityUnitType": 0,
                        "labelIdList": [
                            "芒果"
                        ],
                        "guidePrice": ""
                    }],
                    "unitConversion": {
                        "skuId": 154005,
                        "basicType": 1,
                        "subType": 0,
                        "basicTypeRatio": 0.0,
                        "subTypeRatio": 0.0
                    }
                }],
                "orderPayments": [],
                "cashierName": "",
                "remark": "开单备注",
                "orderCancelHour": 24,
                "cashRemark": "",
                "prePaymentType": [
                    "CASH"
                ],
                "cancelOperation": "",
                "cancelTime": 0,
                "completeTime": 0,
                "cancelReason": "",
                "oldOrderPayments": None,
                "canEditPaymentMethod": False,
                "operateRecord": [{
                    "orderProcessType": "ORDER_PROCESS_BILL",
                    "operatorName": "乌6",
                    "operatorTime": 1675000483502
                }],
                "entryFinanceFlag": False,
                "contractInfo": None,
                "allowDebtSaleFlag": None
            }
        }
    }

jsonpath_v=jsonpath.jsonpath(dic_data,"$..orderCommodities..labelIdList[0]")#msg   "$..data..id"   $..orderCommodities..batchId
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
