#!/usr/bin/python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/7 下午7:45 
# @Author : Mr.Lu
# @Site :  
# @File : chapter_string.py 
# @Software: PyCharm

import math
import pickle

s = "hello string"
n = 1
# 用户易读
print(str(s))
# 程序易读
print(repr(s))
#字符靠左中右 ljust center rjust
print(repr(s).rjust(2),repr(s).rjust(3))
# 数字左侧加0
print(repr(n).zfill(5))

print(math.pi)

"""
open() 将会返回一个 file 对象，基本语法格式如下:
open(filename, mode)
filename：包含了你要访问的文件名称的字符串值。
mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
不同模式打开文件的完全列表：
模式	描述
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""
filePath = '/Users/workspace/items/python/test/prod.txt'
f = open(filePath, 'rb')
# #f2 = open(filePath,'w')
# # 0开头 1当前位置 2结尾
# #f.seek(2, 0)
# #print(f.tell())
str1 = f.read()
# #f2.write('python learn \n this is test')
print(str1)
# #print(f.tell())
# #print(f.readline()) # readlines()
f.close()
# #f2.close()

#
# data = {'name': '123', 'age': 123}
# f3 = open(filePath, 'wb')
# pickle.dump(str(data), f3)
# f3.close()


