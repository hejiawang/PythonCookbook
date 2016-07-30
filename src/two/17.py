#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.17    在文本中处理HTML和XML实体
Created on 2016年7月30日
@author: wang
'''

'''
s = 'Elements are written as "<tag>text</tag>".'
import html
print(s) 
print(html.escape(s))
print(html.escape(s, quote = False))

s = 'Spicy Jalapeno'
print s.encode('ascii', errors = 'xmlcharrefreplace')

s = 'Spicy &quote; Jalape&#241;0&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print p.unescape(s)
t = 'The prompt is &qt;&qt;&qt;'
from xml.sax.saxutils import unescape
print unescape(t)
'''
