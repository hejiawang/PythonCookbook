#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.10    以索引-值对的形式迭代序列
Created on 2016年9月2日
@author: wang
'''

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)
for idx, val in enumerate(my_list, 1):
    print(idx, val)

from _collections import defaultdict
word_summary = defaultdict(list)
with open('../two/somefile.txt', 'r') as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].append(idx)







