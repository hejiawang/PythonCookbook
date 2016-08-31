#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
3.15    将字符串转换为日期
Created on 2016年8月31日
@author: wang
'''

from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)
z = datetime.now()
diff = z - y
print(diff)

nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)

#datetime.strftime性能很差，下面自己编写一个函数
from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
