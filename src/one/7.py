#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.7    让字典保持有序
Created on 2016年7月23日
@author: wang
'''

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grol'] = 4
for key in d:
    print (key, d[key])
    
import json

json.dumps(d)

