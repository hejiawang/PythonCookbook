#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.6    定义带有额外状态的生成器函数
Created on 2016年9月1日
@author: wang
'''

from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3 ):
        self.lines = lines
        self.history = deque(maxlen=histlen)
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line
    def clear(self):
        self.history.clear()
#Example
with open('../two/somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' not in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
        
f = open('../two/somefile.txt')
lines = linehistory(f)
#next(lines)    #error
it = iter(lines)
print(next(it))
