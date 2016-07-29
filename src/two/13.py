#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.13    对其文本字符串
Created on 2016年7月29日
@author: wang
'''

text = 'Hello World'
print text.ljust(20)
print text.rjust(20)
print text.center(20)

print text.rjust(20,'=')
print text.center(20, '*')

print format(text, '>20')
print format(text, '<20')
print format(text, '^20')

print format(text, '=>20s')
print format(text, '*^20s')

print '{:>10s} {:>10s}'.format('Hello', 'World')

x = 1.2345
print format(x, '>10')
print format(x, '^10.2f') 

print '%-20s' % text
print '%20s' % text
