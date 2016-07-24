#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.18    将名称映射到序列的元素中
Created on 2016年7月24日
@author: wang
'''

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('wang@qq.com', '2020-10-10')
print sub
print sub.joined
print sub.addr

print len(sub)
addr, joined = sub
print addr
print joined

def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1]*rec[2]
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

s = Stock('ACME', 100, 123.45)
print s
#s.shares = 75    #error
s = s._replace(shares=75)
print s

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('',0, 0.0, None, None)
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name':'ACME', 'shares':100, 'price':123.45}
print dict_to_stock(a)
b = {'name':'ACME', 'shares':100, 'price':123.45, 'date':'12/12/2012'}
print dict_to_stock(b)
