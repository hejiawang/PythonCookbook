#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.11    对切片命名
Created on 2016年7月23日
@author: wang
'''

items = [0,1,2,3,4,5,6]
a = slice(2,4)
print items[2:4]
print items[a]
items[a] = [10,11]
print items

print a.start
print a.stop
print a.step
