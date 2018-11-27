#!/usr/bin/python3 
# -*- coding: utf-8 -*- 
# @Time : 2018/10/31 下午7:08 
# @Author : Mr.Lu
# @Site :  
# @File : chapter_homework.py
# @Software: PyCharm

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
            print('%d*%d=%d' % (j, i, i*j), end=' ')
    print()

'''
/Users/workspace/items/python/python_learn/venv/bin/python /Users/workspace/items/python/python_learn/chapter_homework.py
1*1=1 
1*2=2 2*2=4 
1*3=3 2*3=6 3*3=9 
1*4=4 2*4=8 3*4=12 4*4=16 
1*5=5 2*5=10 3*5=15 4*5=20 5*5=25 
1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36 
1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49 
1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64 
1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81 
'''
# 用户信息crud系统
user = []
while True:
    flag = int(input("请选择要进行的操作，1-新增，2-删除 ，3-查询 4-退出"))
    if flag == 1:
        userId =input("请输入学号：")
        userName = input("请输入姓名：")
        direone = {'userId': userId, 'userName': userName}
        user.append(direone)
        print('新增成功')
    elif flag == 2:
        del_id = input("请输入需要删除的学生学号：")
        del_name = input("请输入需要删除的学生姓名：")
        direone = {'userId': del_id, 'userName': del_name}
        pos = user.index(direone)
        del user[pos]
        print('已删除')
    elif flag == 3:
        print(user)
    else:
        print('bye!')
        break
'''
请选择要进行的操作，1-新增，2-删除 ，3-查询 4-退出1
请输入学号：123
请输入姓名：abc
新增成功
请选择要进行的操作，1-新增，2-删除 ，3-查询 4-退出1
请输入学号：345
请输入姓名：qwe
新增成功
请选择要进行的操作，1-新增，2-删除 ，3-查询 4-退出3
[{'userId': '123', 'userName': 'abc'}, {'userId': '345', 'userName': 'qwe'}]
请选择要进行的操作，1-新增，2-删除 ，3-查询 4-退出2
请输入需要删除的学生学号：345
请输入需要删除的学生姓名：qwe
已删除
请选择要进行的操作，1-新增，2-删除 ，3-查询 4-退出3
[{'userId': '123', 'userName': 'abc'}]
请选择要进行的操作，1-新增，2-删除 ，3-查询 4-退出4
bye!
'''
