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

# remove() discard() 删除元素，差异在于当元素不存在时，remove报错，discard()不报错
re = set(("age", "name"))
re.remove("age")
print(re)
re.discard("name")
print(re)
# 随机删除元素
set2.pop()
print(set2)
# len()
print(len(set2))
# clear() 清除元素
set2.clear()
print(set2)
# x in s 判断元素是否存在集合
flag = {"name", "age"}
if "age" in flag:
    print(True)
else:
    print(False)
# copy() 拷贝集合 difference 返回差集的新集合 difference_update在原有集合上移除交集元素，保留差集的旧集合
# intersection 返回交集的新集合 intersection_update在原有集合上移除差集元素，保留并集的旧集合
x = {"a", "b", "c"}
y = {"c", "b", "e"}
z = {"e", "g", "c"}
result = x.intersection(y, z)
print(result)

# isdisjoint() 判断两个集合是否有相同元素，相同返回True; issubject()判断指定集合是否为该方法参数集合的子集。
# issuperset()	判断该方法的参数集合是否为指定集合的子集
# symmetric_difference()	返回两个集合中不重复的元素集合
# symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
# union()	返回两个集合的并集
