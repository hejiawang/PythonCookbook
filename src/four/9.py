#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.9    迭代所有可能的组合或排列
Created on 2016年9月2日
@author: wang
'''

items = ['a', 'b', 'c']

#将所有的元素重排列为所有可能的情况
from itertools import permutations, combinations_with_replacement
for p in permutations(items):
    print(p)
for p in permutations(items, 2):
    print(p)  

#输出序列中所有元素的全部组合形式
from itertools import combinations
for c in combinations(items, 3):
    print(c)  
for c in combinations(items, 2):
    print(c)  
for c in combinations(items, 1):
    print(c)

#输出序列中所有元素的全部组合形式——允许相同元素得到多次选择
for c in combinations_with_replacement(items, 3):
    print(c)
