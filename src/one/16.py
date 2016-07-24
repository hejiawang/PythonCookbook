#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.16    筛选序列中的元素
Created on 2016年7月24日
@author: wang
'''

mylist = [1,4,-5,10,-7,2,3,-1]
print [n for n in mylist if n > 0]#列表推导式
print [n for n in mylist if n < 0]

pos = (n for n in mylist if n > 0)#生成器表达式
print pos
for x in pos:
    print(x)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

mylist = [1,4,-5,10,-7,2,3,-1]
import math
print [math.sqrt(n) for n in mylist if n > 0]

clip_neg = [n if n > 0 else 0 for n in mylist]
print clip_neg

clip_pos = [n if n < 0 else 0 for n in mylist]
print clip_pos

addresses = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
print more5
print list(compress(addresses, more5))


