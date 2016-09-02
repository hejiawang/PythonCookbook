#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.15    合并多个有序序列，在对整个有序序列进行迭代
Created on 2016年9月2日
@author: wang
'''

import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)
