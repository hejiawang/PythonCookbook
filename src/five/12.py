#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.12    检查文件是否存在
Created on 2016年9月11日
@author: wang
'''

import os
print(os.path.exists('E://'))
print(os.path.exists('G://'))
print(os.path.isfile('E://'))
print(os.path.isdir('E://'))
print(os.path.islink('E://'))
print(os.path.realpath('E://'))
print(os.path.getsize('F://Study/WorkSpace/Python/PythonCookbook/src/five/12.py'))
print(os.path.getmtime('F://Study/WorkSpace/Python/PythonCookbook/src/five/12.py'))

import time
print(time.ctime(os.path.getmtime('F://Study/WorkSpace/Python/PythonCookbook/src/five/12.py')))




