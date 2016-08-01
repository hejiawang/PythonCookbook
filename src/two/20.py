#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.20    在字符串上执行文本操作
Created on 2016年8月1日
@author: wang
'''

data = b'Hello World'
print data[0:5]
print data.startswith(b'Hello')
print data.split()
print data.replace(b'Hello', b'Hello Cruel')
print data 

data = bytearray(b'Hello World')
print data[0:5]
print data.startswith(b'Hello')
print data.split()
print data.replace(b'Hello', b'Hello Cruel')
print data 

data = b'FOO:BAR,SPAM'
import re
print re.split('[:,]', data)
print re.split(b'[:,]', data)

a = 'Hello World'
print a[0]
print a[1]
b = b'Hello World'
print b[0]
print b[1]

s = b'Hello World'
print(s)
print(s.decode('ascii'))

print b'%10s %10d %10.2f' % (b'ACME', 100, 490.1)
print b'{} {} {}'.format(b'ACME', 100, 490.1)

print '{:10s} {:10d} {:10.2f}'.format(b'ACME', 100, 490.1).encode('ascii')

with open('somefile.txt', 'w') as f:
    f.write('spicy')

import os
print os.listdir('.')
print os.listdir(b'.')
