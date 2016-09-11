#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.8    对固定大小的记录进行迭代
Created on 2016年9月11日
@author: wang
'''

from functools import partial
RECORD_SIZE = 32
with open('somefile.data', 'rb') as f:
    recode = iter(partial(f.read, RECORD_SIZE), b'')
    for r in recode:
        print(r)
