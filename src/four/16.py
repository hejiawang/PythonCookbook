#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4.16    用迭代器取代while循环
Created on 2016年9月2日
@author: wang
'''

'''
CHUNKSIZE = 8192

def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)

def reader(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
         process_data(data)
'''
