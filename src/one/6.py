#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.6    在字典中将建映射到多个值上
Created on 2016年7月23日
@author: wang
'''

d = {
        'a' : [1, 2, 3],
        'b' : [4, 5]
     }
e = {
        'a' : {1, 2, 3},
        'b' : {4, 5}
     }

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
print d

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(3)
print d

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(3)
print d 

d = {}
for key, value in d:#pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

d = defaultdict(list)
for key, value in d:#pairs:
    d[key].append(value)
