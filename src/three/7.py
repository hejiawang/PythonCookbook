#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
3.7    处理无穷大和NaN
Created on 2016年8月29日
@author: wang
'''

a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)
import math
print(math.isinf(a))
print(math.isnan(c))

a = float('inf')
print( a + 45 )
print( a * 10 )
print( 10 / a )

a = float('inf')
b = float('-inf')
print(a/a)
print(a+b)

c = float('nan')
print(c+23)
print(c/3)
print(c*3)
print(math.sqrt(c))

c = float('nan')
d = float('nan')
print(c==d)
print(c is d)
