#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
3.6    复数运算
Created on 2016年8月29日
@author: wang
'''

a = complex(2,4)
b = 3 - 5j
print( a ) 
print( b )

print( a.real)
print( a.imag)
print( a.conjugate())

print( a + b)
print( a * b) 
print( a / b) 
print( abs(a))

import cmath
print( cmath.sin(a))
print( cmath.cos(a))
print( cmath.exp(a))

'''
import numpy as np
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
'''
