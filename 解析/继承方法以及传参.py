#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/9/8 20:56
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 继承方法以及传参.py
# @Software: PyCharm
#-------------------------------------------------------------------------------

class A(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def fuMethod_A(self):
        return (f'fuMethod_A方法中的age值：{self.age}')


class B(A):
    def __init__(self, name, age):
        super().__init__(name, age)  # 需要调用父类中的init函数
        self.name = name
        self.age = age

    def fuMethod_B(self):
        print (f'fuMethod_B方法中的name值：{self.name}')
        print(self.fuMethod_A())


b = B("immuable", 18)
print(b.age, b.name)
# 子类继承父类时 ：通过实例化对象调用父类方法，但这种情况下，子类的同名方法就会覆盖 父类同名方法（奖励讲的是方法，不涉及属性）。属性见例子1或例子3
b.fuMethod_B()



# #重写父类属性方法
# class Father():
#     def __init__(self):
#         self.a = 'aaa'
#
#     def action_F(self):
#         print('调用父类的方法')
#         print(self.a)
#
#
# class Son(Father):
#     def __init__(self,a):
#         self.a = a
#
#     def action_S(self):
#         print('子类重写父类的方法')
#
#
# son = Son('asdhjkashj')  # 子类Son继承父类Father的所有属性和方法
# son.action_F()  # 子类Son调用自身的action方法而不是父类的action方法
# print(son.a)