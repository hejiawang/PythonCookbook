#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.6    在字符串上执行I/O操作
Created on 2016年9月11日
@author: wang
'''
import io

s = io.StringIO()
print( s.write('Hello World\n') )
print( 'This is a test', file=s )
print( s.getvalue() )

s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())

s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
