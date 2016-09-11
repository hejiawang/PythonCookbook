#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.4    读写二进制数据
Created on 2016年9月11日
@author: wang
'''

with open('somefile4.bin', 'wb') as f:
    f.write(b'hello world')
    
with open('somefile4.bin', 'rb') as f:
    print(f.read())

t = 'Hello World'
print(t[0])
for c in t:
    print(c)

b = b'Hello World'
print(b[0])
for c in b:
    print(c)

with open('somefile4.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
    print(text)

with open('somefile4.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))
    
import array
nums = array.array('i', [1,2,3,4])
with open('data.bin', 'wb') as f:
    f.write(nums)

a = array.array('i', [0,0,0,0,0,0,0,0])
with open('data.bin', 'rb') as f:
    print(f.readinto(a))
print(a)



