#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.9    在两个字典中寻找相同点
python 2.7 不支持???
Created on 2016年7月23日
@author: wang
'''

a = {
        'x':1,
        'y':2,
        'z':3
     }
b = {
        'x':11,
        'y':2,
        'w':10
     }

print a.keys() & b.keys() #{'x','y'}
print a.keys() - b.keys() #{'z'}
print a.items() & b.items() #{('y', 2)}

c = {key: a[key] for key in a.keys() - {'z', 'w'} }
print c #{'x':1, 'y':2}