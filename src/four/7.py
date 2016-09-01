#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.7    对迭代器做切片操作
Created on 2016年9月1日
@author: wang
'''

def count(n):
    while True:
        yield n
        n += 1
c = count(0)
#print(c[10, 20])    #error
import itertools
for x in itertools.islice(c, 10, 20):
    print(x)
