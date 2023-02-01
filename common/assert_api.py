#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/8/18 20:47
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : assert_api.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from common.exchange_data import ExchangeData
from common.logger import Logger
import jsonpath,allure,json
class AssertApi():
    re_sql_data={}

    def assert_api(self,response,case,get_db=None):
        self.assert_sql( case,get_db)
        #AssertApi().assert_sql( case,get_db)
        expectlist=case[-1] #断言内容提取
        result_all=[]#多个断言结果列表 True False
        result_dic_list=[]
        if type(response) !=dict:
            response={"response":response}
        Logger.info(response)
        self.re_sql_data.update(response)
        Logger.info(self.re_sql_data)

        #后置提取参数
        extra = case[-3]  # 后置提取参数到参数池中
        ExchangeData.extra_allure(extra)#显示提取参数路径
        ExchangeData.Extract(self.re_sql_data,extra)
        ExchangeData.extra_pool_allure()  # 显示参数池数
        Logger.info('提取参数路径：%s' % extra)
        Logger.info('参数池：%s' % ExchangeData.extra_pool)
        Logger.info('断言内容：%s' % expectlist)
        if expectlist != "" and expectlist != "{}":

            n = 1

            expectlist = ExchangeData.rep_expr(expectlist, return_type='dict')
            Logger.info('变量引用后的断言内容：%s' % expectlist)
            for expect_jsonpath in (expectlist):
                # Logger.info((jsonpath.jsonpath(response, k)[0]))
                # Logger.info(v)
                # actual_results=(jsonpath.jsonpath(response, k)[0])#实际结果
                #k = ExchangeData.rep_expr(k, return_type='srt')

                #Logger.warning(v)
                expect_change=[]
                for i in expect_jsonpath:

                    real_i = (ExchangeData.Extract_noe(self.re_sql_data,i))
                    expect_change.append(real_i)
                #real_v = (ExchangeData.Extract_noe(self.re_sql_data, v))
                #Expected Actual AssertType 期望 实际  断言类型

                Expected_js,AssertType_js,Actual_js,date_type_js=expect_jsonpath #带jsonpath 期望 断言类型  实际 数量类型
                Expected_ch, AssertType_ch,Actual_ch,date_type_ch =expect_change #jsonpath提取值后的 期望 断言类型  实际 数量类型


                loc = locals()
                msg=''
                try:

                    if date_type_ch=='str':
                        exec(f"asser_results = '{Expected_ch}' {AssertType_ch} '{Actual_ch}'")
                    elif date_type_ch=='int':
                        exec(f"asser_results = {Expected_ch} {AssertType_ch} {Actual_ch}")
                    else:
                        raise "没有定义，这样”%s“的数据类型，当前定义了[str,int]"%date_type_ch
                    result=(loc['asser_results'])
                except Exception as e:
                    Logger.error("断言异常：%s（请检查数据类型……）"%e)
                    result = False
                    msg="[%s]"%e
                    #raise "断言异常：%s"%e





                #result = (real_v == real_k)
                result_dic={
                        "提取路径": [Expected_js,Actual_js],
                        "预期结果": Expected_ch,
                        "断言类型": AssertType_ch,
                        "实际结果": Actual_ch,
                        "测试结果": '%s %s'%(result,msg)
                        }
                result_all.append(result)
                result_dic_list.append(result_dic)

                n += 1
        else:
            Logger.warning('没有写断言……')
            result_all = [False]
            result_dic_list.append({"result":"没有添加断言,无断言用例标记失败，请添加断言判断用例",})

        with allure.step('断言：%s'%(False not in result_all)):
            for result_dic in result_dic_list:
                allure.attach(
                    json.dumps(result_dic, ensure_ascii=False, indent=4),
                    "断言：%s：" % (result_dic.get('测试结果',False)),
                    allure.attachment_type.JSON,
                )

        Logger.info(result_all)
        return False not in result_all


    def assert_sql(self, case,get_db=None):
        if get_db!=None:
            sql_srt=case[-2]
            if sql_srt!="":
                sql_srt = ExchangeData.rep_expr(sql_srt, return_type='srt')

                with allure.step('执行sql：%s' % (sql_srt)):
                    for n,sql in enumerate(sql_srt.split(";")):
                        Logger.info([n,sql])
                        data_sql_dic=get_db.execute_sql(sql)
                        Logger.info(data_sql_dic)
                        Logger.info(type(data_sql_dic))
                        #ExchangeData.extra_pool.update({"sql_%s_data"%n:data_sql_dic})
                        self.re_sql_data.update({"sql_%s_data"%n:data_sql_dic})
                        #Logger.info(ExchangeData.extra_pool)
                        allure.attach(
                            json.dumps({"sql_%s_data"%n:data_sql_dic}, ensure_ascii=False, indent=4),
                            sql,
                            allure.attachment_type.JSON,
                        )







