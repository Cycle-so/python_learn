#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 14:17
# @Author  : Mr.Lu
# @Site    : 
# @File    : chapter_series.py
# @Software: PyCharm

# Fibonacci series: 斐波纳契数列^^^^两个元素的总和确定了下一个数
a, b = 0, 1
while b < 100:
    print(b, end=",")
    a, b = b, a+b
