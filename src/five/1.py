#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.1    读写文件数据
Created on 2016年9月11日
@author: wang
'''

with open('somefile.txt','rt') as f:
    data = f.read()
    print(data)

with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)

with open('somefile2.txt', 'wt') as f:
    f.write('text1')
    f.write('text2')
    
f = open('somefile.txt', 'rt')
data = f.read()
f.close()

f = open('somefile2.txt', 'rt')
print(f.read())

f = open('somefile2.txt', 'rt', newline='')
print(f.read())

f = open('somefile.txt', 'rt', encoding='ascii', errors='replace')
print(f.read())

f = open('somefile.txt', 'rt', encoding='utf-8')
print(f.read())
