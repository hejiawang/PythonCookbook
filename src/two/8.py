#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.8    编写多行模式的正则表达式
Created on 2016年7月24日
@author: wang
'''

import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
                multiline comment */
        '''
print comment.findall(text1)
print comment.findall(text2)

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print comment.findall(text2)

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print comment.findall(text2)
