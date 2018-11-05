#!/usr/bin/python3 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/1 下午6:34 
# @Author : Mr.Lu
# @Site :  
# @File : chapter_dictionary.py 
# @Software: PyCharm

'''
字典-可变容器模型，
键值对
'''
dictionary = {'name': 'lili', 'age': 12, 'address': '杭州'}

print(dictionary['name'])
print(dictionary)

# 赋值更新
dictionary['age'] = 18
dictionary['sex'] = 'Fale'
print(dictionary)

# 删除字典元素及其本身
del dictionary['address']
print(dictionary)
# dictionary.clear() # 清空字典
print(dictionary)
# del  dictionary  # 删除字典
print(dictionary)

'''
字典不允许出现同名键，其值后者覆盖前者
键元素不可变，于此不支持列表元素作为键，支持数字、字符、元祖
'''
dicts = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print(dicts)

# 字典-内置函数 len str type
print(len(dicts))
print(str(dicts))
print(type(dicts))

'''
内置方法 clear copy fromkeys get key in dict items keys setdefault update values default pop popitem
'''
# clear 清除字典all元素 dict.clear()

# copy 引用与拷贝
dict1 = {'name': 'Alice', 'age': 18, 'like': [1, 2, 3]}
copy1 = dict1  # 引用对象, dict1改变，copy1随之改变
copy2 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
# 修改 data 数据
dict1['age'] = 20
dict1['like'].remove(1)
print(dict1)
print(copy1)
print(copy2)

# fromkeys() 函数于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
seq = ('a', 'b', 'c')
dict_fk = dict.fromkeys(seq)
print(dict_fk)
dict_fk = dict.fromkeys(seq, 1)
print(dict_fk)

# get 获取字典key的values,无值返回none
print(dict1.get('name'))
print(dict1.get('names'))

# key in dict 判读键是否存在字典中
if 'name' in dict1:
    print(True)
else:
    print(False)

# items 遍历字典
print(dict1.items())

for i, j in dict1.items():
    print(i, ': ', j)

# keys返回迭代器，可用list()转为列表
print(dict1.keys())
print(list(dict1.keys()))

# setDefault和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
dict_def = {'name': 'Lisa', 'age': 18}
print(dict_def)
print(dict_def.setdefault('sex', 'refale'))
print(dict_def)

# update 把指定字典更新到字典内
dict_update = {'voice': 'nice'}
dict_update.update(dict_def)
print(dict_update)

# vlaues() 和items()类似
print(list(dict_update.values()))

# pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
dict_pop = dict_update.pop("voice")
print(dict_pop)

# popitem() 删除字典末尾键值对 如字典元素为空，则报错

dict_popitem = dict_update.popitem()
print(dict_popitem)
print(dict_update)