#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
3.9    处理大型数组的计算
Created on 2016年8月30日
@author: wang
'''

x = [1,2,3,4]
y = [5,6,7,8]
print(x*2)
#print(x+10)    #error
print(x+y)

import numpy as np
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])
print(ax*2)
print(ax+10)
print(ax+ay)
print(ax*ay)

def f(x):
    return 3*x*2
print(f(ax))

print(np.sqrt(ax))
print(np.cos(ax))

grid = np.zeros(shape=(10000,10000), dtype=float)
print(grid)
print(grid+10)
print(np.sin(grid))

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
print(a[1])
print(a[:,1])
print(a[1:3, 1:3])

a[1:3, 1:3] += 10
print(a)

a + [100, 101, 102, 103]
print(a)

print( np.where(a<10, a, 10) )
