#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.5    对已不存在的文件执行写入操作
Created on 2016年9月11日
@author: wang
'''

with open('somefile', 'wt') as f:
    f.write('Hello\n')

'''
with open('somefile', 'xt') as f:
    f.write('Hello\n')
'''
        
import os
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')



