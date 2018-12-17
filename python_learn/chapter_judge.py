#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 14:28
# @Author  : Mr.Lu
# @Site    : 
# @File    : chapter_judge.py
# @Software: PyCharm
"""
条件判断 judge if elif else  == >= <= != > <
"""
flag = int(1)
if flag == 1 :
    print('flag values is 1')
else:
    print('flag values is not 1')

keywords = int(input('enter number'))
if keywords < 10:
    print('the keywords less than 10')
elif keywords > 10 & keywords < 100:
    print('the keywords is more than 10 and less than 100')
else:
    print('the keywords is eq 10 or more than 100')
