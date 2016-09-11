#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.11    处理路径名
Created on 2016年9月11日
@author: wang
'''

import os
path = 'F:\Study\WorkSpace\Python\PythonCookbook\src\five\11.py'
print( os.path.basename(path) )
print( os.path.dirname(path) )
print( os.path.join('tem', 'data', os.path.basename(path)) )

path = '~\PythonCookbook\src\five\11.py'
print( os.path.expanduser(path) )
print( os.path.splitext(path) )
