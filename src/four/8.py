#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.8    跳过可迭代对象中的前一部分元素
Created on 2016年9月1日
@author: wang
'''

#跳过所有#开头的行
from itertools import dropwhile
with open('../two/somefile.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

#跳过指定的多少个元素
from itertools import islice
items = ['a','b','c',1,4,10,15]
for x in islice(items, 3, None):
    print(x)
    
with open('../two/somefile.txt') as f:
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

while line:
    print(line, end='')
    line = next(f, None)

with open('../two/somefile.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')

