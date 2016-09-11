#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.13    获取目录内容的列表
Created on 2016年9月11日
@author: wang
'''

import os
names = os.listdir('F://Study/WorkSpace/Python/PythonCookbook/src/five')
print(names)

import os.path
names = [name for name in os.listdir('F://Study/WorkSpace/Python/PythonCookbook/src/five')
         if os.path.isfile(os.path.join('F://Study/WorkSpace/Python/PythonCookbook/src/five', name))]
print(names)

names = [name for name in os.listdir('F://Study/WorkSpace/Python/PythonCookbook/src/five')
         if os.path.isdir(os.path.join('F://Study/WorkSpace/Python/PythonCookbook/src/five', name))]
print(names)

pyfiles = [name for name in os.listdir('F://Study/WorkSpace/Python/PythonCookbook/src/five')
         if name.endswith('.py')]
print(pyfiles)

import glob
pyfiles = glob.glob('F://Study/WorkSpace/Python/PythonCookbook/src/five/*.py')
print(pyfiles)

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('F://Study/WorkSpace/Python/PythonCookbook/src/five')
         if fnmatch(name, '*.py')]
print(pyfiles)

#import os
#import os.path
#import glob
pyfiles = glob.glob('*.py')
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]
for name, size, mtime in name_sz_date:
    print(name, size, mtime)
for name,meta in name_sz_date:
    print(name, meta.st_size, meta.st_mtime)
