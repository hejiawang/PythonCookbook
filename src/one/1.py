#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.1    将序列分解为单独的变量

Created on 2016年7月23日
@author: wang
'''

p = (4, 5)
x, y = p
print x 
print y 

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print name
print shares 
print price 
print date 
name, shares, price, (year, mon, day ) = data
print year 

p = (4, 5)
#x, y, z = p 错误!!!

s = 'hello!'
a, b, c, d, e, f = s
print a
print f
