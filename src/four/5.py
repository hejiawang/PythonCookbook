#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.5    反向迭代
Created on 2016年9月1日
@author: wang
'''

a = [1,2,3,4]
for x in reversed(a):
    print(x)
    
f = open('../two/somefile.txt')
for line in reversed(list(f)):
    print(line, end='')

#实现_reversed__()方法即可反向迭代
class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    def __reversed__(self):
        n = 1
        while n < self.start:
            yield n
            n += 1
