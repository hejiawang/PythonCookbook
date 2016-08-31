#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
3.16    处理涉及到时区的日期问题
Created on 2016年8月31日
@author: wang
'''

from datetime import datetime
from pytz import timezone
from _datetime import timedelta
d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

banf_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(banf_d)

d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)

from datetime import timedelta
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

import pytz
print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)#世界统一时间
print(utc_d)

later_utc = utc_d + timedelta(minutes = 30)
print(later_utc.astimezone(central))

print(pytz.country_timezones['IN'])






