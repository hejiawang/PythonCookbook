#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.7    定义实现最短匹配的正则表达式
Created on 2016年7月24日
@author: wang
'''

import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print str_pat.findall(text1)

text2 = 'Computer says "no." Phone says "yes."'
print str_pat.findall(text2)

str_pat = re.compile(r'\"(.*?)\"')
print str_pat.findall(text2)
