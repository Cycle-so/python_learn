#!/usr/bin/python3 
# -*- coding: utf-8 -*- 
# @Time : 2018/10/30 下午6:44 
# @Author : Mr.Lu
# @Site :  
# @File : chapter_list.py 
# @Software: PyCharm

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
# 索引取值
print("list1[0]:"+list1[0])
print("list2[2:4]:", list2[2:5])

# 更新下标元素-values
list1[0] = 'Baidu'
print(list1)

# 删除元素
del list1[0]
print(list1)
# 长度
print(len(list1))
# 组合
print(list1+list2)
# 定义重复元素列表
list3 = ['test']*3
print(list3)
# 迭代
for x in list1:
    print(x)

#  嵌套
list1[2] = list2
print(list1)
# max min
print(max(list2))
print(min(list2))
# append
list2.append(7)
print(list2[len(list2)-1])
# 检索重复
print(list2.count(7))
# 检索下标
print(list2.index(1))
# 插入数据
list2.insert(0,10)
print(list2)
# 移除 pop remove
list2.pop()
print(list2)
list2.remove(10)
print(list2)
# 反向 排序
list2.reverse()
print(list2)
list2.sort()
print(list2)
# 复制 清空列表
list4 = list2.copy()
print('list4:', list4)
list2.clear()
print("list2", list2)