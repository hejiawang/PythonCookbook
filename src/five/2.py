#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.2    将输出重定向到文件中
Created on 2016年9月11日
@author: wang
'''

with open('somefile3.txt', 'wt') as f:
    print('Hello world!', file=f)
