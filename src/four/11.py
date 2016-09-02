#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.11    同时迭代多个序列
Created on 2016年9月2日
@author: wang
'''

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

a = [1, 2, 3]
b = ['w', 'y', 'z', 'x']
for x, y in zip(a, b):
    print(x, y)

from itertools import zip_longest
for i in zip_longest(a, b):
    print(i)
for i in zip_longest(a, b, fillvalue=0):
    print(i)

a = [1, 2, 3]
b = ['w', 'y', 'z']
c = [7, 8, 9]
for i in zip(a, b, c):
    print(i)
