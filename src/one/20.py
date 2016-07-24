#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.20    将多个映射合并为单个映射
Created on 2016年7月24日
@author: wang
'''


a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

#from collections import ChainMap
from pip._vendor.distlib.compat import ChainMap

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z']) #from a    第一个映射中的值

print len(c)
print list(c.values())

c['z'] = 10
c['w'] = 40
del c['x']
print a
#del c['y']    #error    修改映射的操作总是会作用在列表的第一个映射结构上

values = ChainMap()
values['x'] = 1
values = values.new_child()#add a new map
values['x'] = 2
values = values.new_child()
values['x'] = 3
#print values
print values['x']
values = values.parents
print values['x']
values = values.parents
print values['x']

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
merged = dict(b)
merged.update(a)
print merged['x']
print merged['y']
print merged['z']
a['x'] = 13
print merged['x']   #不会反应到合并后的字典中

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
merged = ChainMap(a, b)
print merged['x']
a['x'] = 42
print merged['x']   #会反应到合并后的字典中
