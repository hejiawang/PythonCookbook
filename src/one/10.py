#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.10    从序列中移除重复项且保持元素间顺序不变
Created on 2016年7月23日
@author: wang
'''

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
#example
a = [1,5,2,1,9,1,5,10]
print list(dedupe(a))

def dedupe2(items, key = None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val) 
#example
a = [ 
        {'x':1, 'y':2}, 
        {'x':1, 'y':3}, 
        {'x':1, 'y':2}, 
        {'x':2, 'y':4}, 
     ]
print list( dedupe2(a, key=lambda d : (d['x'], d['y']) ) )
print list( dedupe2(a, key=lambda d : (d['x']) ) )

a = [1,5,2,1,9,1,5,10]
print set(a)    
