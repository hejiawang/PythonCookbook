#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.11    从字符串中去掉不需要的字符
Created on 2016年7月26日
@author: wang
'''

s = ' hello word \n'
print s.strip()
print s.lstrip()
print s.rstrip()

t = '-----hello====='
print t.lstrip('-')
print t.strip('-=')

s = ' hello   word   \n'
print s.strip()
print s.replace(' ', '')
import re
print re.sub('\s+', ' ', s)
