#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.10    对二进制文件做内存映射
Created on 2016年9月11日
@author: wang
'''

import os
import mmap
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.path(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

m = memory_map('data')
print(len(m))
