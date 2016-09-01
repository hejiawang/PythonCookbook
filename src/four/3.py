#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.3    用生成器创建新的迭代模式
Created on 2016年9月1日
@author: wang
'''

def frang(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frang(0, 4, 0.8):
    print(n)
print(list(frang(0, 1, 0.125)))

def countdown(n):
    print('Starting to count from ', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')
c = countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
#print(next(c))    #error
