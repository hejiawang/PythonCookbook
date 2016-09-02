#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.12    在不同的容器中进行迭代
Created on 2016年9月2日
@author: wang
'''

from itertools import chain
a = [1, 2, 3]
b = ['w', 'y', 'z']
c = [7, 8, 9]
for x in chain(a, b, c):
    print(x)
