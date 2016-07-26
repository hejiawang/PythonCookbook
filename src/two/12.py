#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.12    文本过滤和清理
Created on 2016年7月26日
@author: wang
'''

s = "python\fis\tawesome\r\n"
print s
remap = {
            ord('\t') : ' ',
            ord('\f') : ' ',
            ord('\r') : None
         }
a = s.translate(remap)
print a 

import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) 
                         if unicodedata.combining(chr(c)) )
b = unicodedata.normalize('NFD', a)
print b
print b.translate(cmb_chrs)

digitmap = {
                c : ord('0') + unicodedata.digit(chr(c))
                for c in range(sys.maxunicode)
                if unicodedata.category(chr(c)) == 'ND'
            }
print len(digitmap)
x = '\u0661\u0662\u0663'
x.translate(digitmap)

a = "python is awesome\n"
b = unicodedata.normalize('NFD', a)
print b.encode('ascii', 'ignore').decode('ascii')

def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', '')
    s = s.replace('\f', '')
    return s
