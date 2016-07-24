#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.19    同时对数据做转换和换算
Created on 2016年7月24日
@author: wang
'''

nums = [1, 2, 3, 4, 5]
s = sum( x*x for x in nums )
print s

import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be Python!')
else:
    print('sorry, no Python!')
    
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

portfolio = [
                {'name':'GOOG', 'shares':50},
                {'name':'YHOO', 'shares':75},
                {'name':'AOL', 'shares':20},
                {'name':'SCOX', 'shares':65}
             ]
min_shares = min(s['shares'] for s in portfolio)
print min_shares    

min_shares = min(portfolio, key=lambda s: s['shares'])
print min_shares
