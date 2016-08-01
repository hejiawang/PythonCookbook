#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
3.2    执行精确的小数计算
Created on 2016年8月1日
@author: wang
'''

a = 2.1
b = 4.2
c = a + b
print c
print c == 6.3

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print a + b
print a + b == Decimal('6.3')

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print( a / b )
with localcontext() as ctx :
    ctx.prec = 3
    print( a/b )
with localcontext() as ctx :
    ctx.prec = 5
    print( a/b )
    
num = [ 1.23e+18, 1, -1.23e+18 ]
print sum(num)
import math
print math.fsum(num)
