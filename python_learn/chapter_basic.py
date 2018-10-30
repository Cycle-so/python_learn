#!/usr/bin/python3 
# -*- coding: utf-8 -*- 
# @Time : 2018/10/30 下午6:29 
# @Author : Mr.Lu
# @Site :  
# @File : chapter_basic.py 
# @Software: PyCharm

# input()
str = "hello world"
print(str)
# 字符输出格式化
print(str.format())
# 截取
print("{:.2f}".format(10.34343))
#  转换二进制
print("{:b}".format(100))
# 十六进制
print("{:x}".format(100))
print(str*3)
# this is single annotation
'''
this is multipart annotation
'''
char = 'this'
print(char)
print(char*2)
if 'h' in char:
    print(True)
else:
    print(False)
print("she name is %s %d years old" % ("corgi", 20))
# 首字符转换为大写
print(char.capitalize())
'''
居中
print(char.center())
'''
'''
计数
print(char.count())
'''
# 加解码
en = char.encode()
print(en)
#print(en.decode(encoding="UTF-8",errors="strict"))

if char.endswith('t'):
    print(True)
elif char.isalpha():
    print(True)