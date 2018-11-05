#!/usr/bin/python3 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/5 下午7:04 
# @Author : Mr.Lu
# @Site :  
# @File : chapter_set.py 
# @Software: PyCharm

"""
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
# 创建格式
set1 = {'name', 1, 'voi'}
set()
set2 = {x for x in 'abracadabra' if x not in 'abc'}

print(set2)

# add() 集合添加元素，如元素已存在则忽视
set1.add('age')
set1.add(1)
print(set1)

# update 添加元素、可以是元祖、列表、字典 元素支持多个，使用'，'分隔
set2.update([1, 2])
print(set2)

#