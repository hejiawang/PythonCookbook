#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
3.1    对数值进行取整
Created on 2016年8月1日
@author: wang
'''

print round(1.23, 1)
print round(1.27, 1)
print round(-1.27, 1)
print round(1.25361, 3)
print round(1.5, 0)
print round(2.5, 0)

a = 1627731
print round(a, -1)
print round(a, -2)
print round(a, -3)

x = 1.23456
print format(x, '0.2f')
print format(x, '0.3f')
print 'value is {:0.3f}'.format(x)

a = 2.1
b = 4.2
c = a + b
print c
print round(c, 2)
