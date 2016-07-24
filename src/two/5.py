#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
查找和替换文本
Created on 2016年7月24日
@author: wang
'''

text = 'yeah, but no, but yeah, but no, but yeah'
print text.replace('yeah','yep')
print text

text = 'Today id 11/27/2012. PyCon starts 3/13/2013'
import re
print re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print datepat.sub(r'\3-\1-\2', text)

from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print datepat.sub(change_date, text)

newtext, n = datepat.subn(r'\3-\1-\2', text)
print newtext
print n
