#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
5.3    以不同的分割符或行结尾符完成打印
Created on 2016年9月11日
@author: wang
'''

print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')

for i in range(5):
    print(i)

for i in range(5):
    print(i, end=' ')
    
#print(','.join('ACME', '50', '91.5'))

row = ('ACME', '50', '91.5')
print(','.join(row))
