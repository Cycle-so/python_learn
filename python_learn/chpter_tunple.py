#!/usr/bin/python3 
# -*- coding: utf-8 -*- 
# @Time : 2018/10/30 下午7:06 
# @Author : Mr.Lu
# @Site :  
# @File : chpter_tunple.py 
# @Software: PyCharm
# 创建元组
tup = ()
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

'''
修改元祖 元祖中的子元素不允许修改
#tup1[0] = 'error'
'''
tup1 = (1,2,3,4,5,6)
tup = tup1+tup2
print(tup)

#删除元祖
del tup1
#print(tup1)

#元祖运算符、方法和list基本一致
print(tup.__len__())
print(len(tup))
tup3 = ('test',)*3
print(tup3)

for x in tup3:
    print(x)

print(max(tup2))
print(min(tup))