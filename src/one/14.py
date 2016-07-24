#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.14    对不原生支持比较操作的对象排序
Created on 2016年7月24日
@author: wang
'''

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print users
print sorted(users, key = lambda u: u.user_id)

from operator import attrgetter
print sorted(users, key=attrgetter('user_id'))

print min(users, key=attrgetter('user_id'))
print max(users, key=attrgetter('user_id'))