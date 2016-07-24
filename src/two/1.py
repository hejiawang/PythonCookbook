#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.1    针对任意多的分隔符拆分字符串
Created on 2016年7月24日
@author: wang
'''

line = 'asdf fjdk; afed, fjek,asdf,     foo'
import re
print re.split(r'[;,\s]\s*', line)
fields = re.split(r'(;|,|\s)\s*', line)
print fields

values = fields[::2]
print values

delimiters = fields[1::2] + ['']
print delimiters

print ''.join(v+d for v, d in zip(values, delimiters))

print re.split(r'(?:,|;|\s)\s*', line)
