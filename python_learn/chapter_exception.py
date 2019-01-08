#!/usr/bin/python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/8 下午2:16 
# @Author : Mr.Lu
# @Site :  
# @File : chapter_exception.py 
# @Software: PyCharm

"""
异常捕获、抛出
"""
#处理
while True:
        try:
            x = int(input("Please enter a number: "))
            print(x)
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")

#抛出
while True:
        try:
            x = int(input("Please enter a number: "))
            print(x)
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")
            raise

# 定义函数
def temp_convert(var):
    try:
        print(var)
        return int(var)
    except (ValueError) as Argument:
        print ("参数没有包含数字\n", Argument)

# 调用函数
temp_convert('1');