#!/usr/bin/python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/8 下午4:27 
# @Author : Mr.Lu
# @Site :  
# @File : chapter_mutilib.py 
# @Software: PyCharm
"""
python 标准库接口
"""
from datetime import date
import zlib
import urllib
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.request import Request
import itertools

now = date.today()
print(now)

# 压缩 zlip zfile gzip bz2 tarfile
st1 = b"this is uzip string test"
print(len(st1))
zst1 = zlib.compress(st1)
print(len(zst1))
print(zlib.decompress(zst1))
print(zlib.crc32(st1))
print(zlib.adler32(st1))

"""
#get
url='https://www.baidu.com'
data={"username":"admin","password":123456}
req_data=urlencode(data)#将字典类型的请求数据转变为url编码
res=urlopen(url)#通过urlopen方法访问拼接好的url
res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)
#post
url='http://www.xxx.com/login'
data={"username":"admin","password":123456}
data=urlencode(data)#将字典类型的请求数据转变为url编码
data=data.encode('ascii')#将url编码类型的请求数据转变为bytes类型
req_data=Request(url,data)#将url和请求数据处理为一个Request对象，供urlopen调用
with urlopen(req_data) as res:
    res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)
"""
#笛卡尔积
class cartesian(object):
    def __init__(self):
        self._data_list=[]

    def add_data(self,data=[]): #添加生成笛卡尔积的数据列表
        self._data_list.append(data)

    def build(self): #计算笛卡尔积
        for item in itertools.product(*self._data_list):
            print(item)

if __name__=="__main__":
    car=cartesian()
    car.add_data([1,2,3,4])
    car.add_data([5,6,7,8])
    car.add_data([9,10,11,12])
    car.build()


for x, y, z in itertools.product([1,2],[3,4],[5,6]):
    print(x,y,z)

#日历
import calendar

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))

# 显示日历
print(calendar.month(yy, mm))