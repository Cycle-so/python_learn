#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 14:30
# @Author  : Mr.Lu
# @Site    :
# @File    : chapter_iterator.py
# @Software: PyCharm

"""
迭代器 iterator
"""
import sys

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

#创建迭代对象
list = [1, 2, 3, 4]
it = iter(list)

for i in it:
    print(i, end="")

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
