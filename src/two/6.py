#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.6    以不区分大小写的方式对文本做查找和替换
Created on 2016年7月24日
@author: wang
'''
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print re.findall('python', text, flags=re.IGNORECASE)
print re.sub('python', 'snake', text, flags=re.IGNORECASE)

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
#example
print re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
