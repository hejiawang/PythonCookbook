#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
3.5    从字符串中打包和解包大整数
Created on 2016年8月29日
@author: wang
'''

x = 1234567893456745
print( x.to_bytes(16,'big'))
print( x.to_bytes(16,'little'))

data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04b\xd5<\xbd\x97i'
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))
