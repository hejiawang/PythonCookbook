#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
3.4    同二进制、八进制和十六进制数打交道
Created on 2016年8月1日
@author: wang
'''

x = 1234
print bin(x)
print oct(x)
print hex(x)

print format(x, 'b')
print format(x, 'o')
print format(x, 'x')

x = -1234
print format(x, 'b')
print format(x, 'o')
print format(x, 'x')

print format(2**32 + x, 'b')
print format(2**32 + x, 'x')

print int('4d2', 16)
print int('10011010010', 2)
