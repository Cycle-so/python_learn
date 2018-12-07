#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 14:28
# @Author  : Mr.Lu
# @Site    : 
# @File    : chapter_cycle.py
# @Software: PyCharm
"""
循环 for while
"""
lists = [1, 2, 3, 4, 5]
for x in lists:
    print(x)

flag = int(input("enter something here"))
while flag < 10:
    print('the number less than ten')
else:
    print('the number eq or more than ten')

for x in range(1, 10, 3):
    print(x)
