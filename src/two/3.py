#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.3    利用Shell通配符做字符串匹配
Created on 2016年7月24日
@author: wang
'''

from fnmatch import fnmatch, fnmatchcase
print fnmatch('foo.txt', '*.txt')#fnmatch大小写区分规则同操作系统
print fnmatch('foo.txt', '?**.txt')
print fnmatch('Dat45.csv', 'Dat[0-9]*')
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print [name for name in names if fnmatch(name, 'Dat*.csv')]

print fnmatchcase('foo.txt', '*.TXT')#fnmatchcase区分大小写

addresses = [
                '5412 N CLARK ST',
                '1060 W ADDISON ST',
                '1039 W GRAVNILLE AVE',
                '2122 N CLARK ST',
                '4802 N BROADWAY',
             ]
print [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
