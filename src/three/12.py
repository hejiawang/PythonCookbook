#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
3.12    时间换算
Created on 2016年8月30日
@author: wang
'''

#利用datetime模块进行不同时间单位的换算
from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds / 3600)

#表示特定的日期和时间
from datetime import datetime
a = datetime(2016, 8, 30)
print(a + timedelta(days=10))
b = datetime(2016, 9, 30)
d = b - a
print(d.days)

now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

#datetime模块可以正确处理闰年
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print((a-b).days)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c-d).days)

#处理更为复杂的日期问题，如处理时区，模糊时间范围，计算节日的日期等可以用dateutil模块
from dateutil.relativedelta import relativedelta
print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))

b = datetime(2012, 12, 21)
d = b - a
print(d)
d = relativedelta(b, a)
print(d)
print( d.months )
print( d.days )
