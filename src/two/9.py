#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.9    将Unicode文本统一表示为规范形式
Created on 2016年7月26日
@author: wang
'''
from curses.ascii import ascii

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print s1
print s2
print s1 == s2
print len(s1)
print len(s2)

import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print t1 == t2 
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print t3 == t4
print(ascii(t4))

s = '\ufb01'
print s
print unicodedata.normalize('NFD', s)
print unicodedata.normalize('NFKD', s)
print unicodedata.normalize('NFKC', s)

t = unicodedata.normalize('NFD', s1)
print ''.join(c for c in t if not unicodedata.combining(c))
