#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.15    给字符串中的变量名做插值处理
Created on 2016年7月29日
@author: wang
'''

s = '{name} has {n} messages.'
print s.format(name='Guido', n=37)

name = 'Guido'
n = 37
'''
print s.format_map(vars())
'''

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('Guido', 37)
'''
print s.format_map(vars(a))
'''

'''
print s.format(name='Guido')
'''

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'
del n # make sure n is undefined
'''
print s.format_map(safesub(vars(a)))
'''

import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
name = 'Guido'
n = 37
'''
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))
'''

name = 'Guido'
n = 37
'''
print '%{name} has {n} messages.' % vars()
'''
import string
s = string.Template('$name has $n messages.')
print s.substitute(vars())
