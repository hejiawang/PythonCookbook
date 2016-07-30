#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.16    以固定的列数重新格式化文本
Created on 2016年7月30日
@author: wang
'''

s = "Look into my eyes, Look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."
import textwrap
print(textwrap.fill(s, 70))    
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent=' '))    
print(textwrap.fill(s, 40, subsequent_indent=' '))    

'''
import os
print os.get_terminal_size().columns
'''
