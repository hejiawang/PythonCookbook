#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.4    找到最大或最小的N个元素
Created on 2016年7月23日
@author: wang
'''

import heapq

nums = [1,30,6,2,36,33,46,3,23,43]
print (heapq.nlargest(3, nums))
print (heapq.nsmallest(3, nums))

portfolio = [
                 {'name':'IBM', 'shares':100, 'price':2.4},
                 {'name':'A', 'shares':1040, 'price':12.4},
                 {'name':'S', 'shares':40, 'price':23.4},
                 {'name':'D', 'shares':1, 'price':2.49},
                 {'name':'F', 'shares':9, 'price':24}
             ]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print cheap
print expensive

nums = [1,8,2,23,7,-4,18,23,42,37,2]
heap = list(nums)
print heap
heapq.heapify(heap)
print heap
print heapq.heappop(heap)
print heapq.heappop(heap)
print heapq.heappop(heap)
