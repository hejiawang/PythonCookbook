#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.8    与字典有关的计算问题
Created on 2016年7月23日
@author: wang
'''

price = {
            'ACME':23.45,
            'IBM':25.45,
            'FB':13.45,
            'IO':4.45,
            'JAVA':45.45,
            'AV':38.38,
         }

min_price = min( zip( price.values(), price.keys() ) )
print min_price

max_price = max( zip( price.values(), price.keys() ) )
print max_price

price_sorted = sorted( zip( price.values(), price.keys() ) )
print price_sorted   

price_and_names = zip( price.values(), price.keys() )
print (min(price_and_names))
#print (max(price_and_names))  error  zip()创建了迭代器，内容只能被消费一次

print min(price)
print max(price)

print min(price.values())
print max(price.values())


print min(price, key = lambda k : price[k])
print max(price, key = lambda k : price[k])

min_value = price[ min(price, key = lambda k : price[k]) ]
print min_value

price = {
            'AAA': 23,
            'ZZZ': 23,
         }
print min( zip( price.values(), price.keys() ) )
print max( zip( price.values(), price.keys() ) )
