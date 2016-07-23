#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.2    从任意长度的可迭代对象中分解元素
*表达式，Python2,7 不支持???
Created on 2016年7月23日
@author: wang
'''
'''
from audioop import avg

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record = ('Dave', 'dave@example.com', '777-333-2323', '234-234-2345')
name, email, *phone_numbers = record
print name 
print email
print phone_numbers

*trailing, current = [10, 8, 7, 2, 5]
print trailing  #[10, 8, 7, 2, ]
print current #5

records = [
           ('foo', 1, 2),
           ('bar', 'hello'),
           ('foo', 5, 3)
           ]
def do_foo(x, y):
    print ('foo', x, y)
def do_bar(s):
    print ('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
        
line = 'asdf:fedfr234://wef:678d:asdf'
uname, *fields, homedir, sh = line.split(':')
print uname 
print homedir

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print name
print year

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print head #1
print tail #[10, 7, 4, 5, 9]

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
sum(items)
'''