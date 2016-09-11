#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.7    读写压缩的数据文件
Created on 2016年9月11日
@author: wang
'''

import gzip
with gzip.open('somefile.gz','rt') as f:
    text = f.read()
    print(text)
    
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()
    print(text)

with gzip.open('somefile.gz', 'wt') as f:
    f.write('hello gzip')
    
with bz2.open('somefile.bz2', 'wt') as f:
    f.write('hello bz2')
    
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write('hello world')

f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
