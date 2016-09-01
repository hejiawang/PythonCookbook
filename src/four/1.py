#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.1    手动访问迭代器中的元素
Created on 2016年9月1日
@author: wang
'''

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

with open('/etc/passwd') as f:
    while True:
        line = next(f)
        if line is None:
            break
        print(line, end='')
            
items = [1, 2, 3]
it = iter(items)
print(next(it))            
print(next(it))            
print(next(it))            
print(next(it))#error
