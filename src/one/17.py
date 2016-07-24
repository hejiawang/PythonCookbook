#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.17    从字典中提取子集
Created on 2016年7月24日
@author: wang
'''

prices = {'ACNE':45.23, 'AAPL':612.78, 'IBM':205.55, 'HPQ':37.20, 'FB':10.75}
p1 = { key:value for key, value in prices.items() if value > 200 }
print p1

tech_names = {'AAPL', 'IBM', 'HPQ'}
p2 = { key:value for key, value in prices.items() if key in tech_names }
print p2

p3 = dict( (key, value) for key, value in prices.items() if value > 200 ) #慢
print p3

tech_names = {'AAPL', 'IBM', 'HPQ'}
p4 = { key:prices[key] for key in prices.keys() if key in tech_names } #慢
print p4
