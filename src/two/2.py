#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.2    在字符串的开头或结尾处做文本匹配
Created on 2016年7月24日
@author: wang
'''

filename = 'spam.txt'
print filename.endswith('.txt')
print filename.startswith('file:')
url = 'http://www.godaji.com'
print url.startswith('http:')

import os
filenames = os.listdir('.')
print filenames
print [name for name in filenames if name.endswith(('.c', '.py'))]
print any(name.endswith('.py') for name in filenames)

from urllib import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choice = ['http:', 'ftp:']
url = 'http://www.godaji.com'
#print url.startswith(choice)    #error
print url.startswith(tuple(choice))

filename = 'spam.txt'
print filename[-4:] == '.txt'
url = 'http://www.godaji.com'
print url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'

import re
url = 'http://www.godaji.com'
print re.match('http:|https:|ftp:', url)
