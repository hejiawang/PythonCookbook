#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.18    文本分词
Created on 2016年7月30日
@author: wang
'''

text = 'foo = 23 + 42 * 10'
tokens = [
          ('NAME', 'foo'),
          ('EQ', '='),
          ('NUM', '23'),
          ('PLUS', '+'),
          ('NUM', '42'),
          ('TIMES', '*'),
          ('NUM', '10'),
          ]
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile( '|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]) )
scanner = master_pat.scanner('foo = 42')
print scanner.match()
print _.lastgroup, _.group()
print scanner.match()
print _.lastgroup, _.group()
print scanner.match()
print _.lastgroup, _.group()
print scanner.match()
print _.lastgroup, _.group()
print scanner.match()
print _.lastgroup, _.group()
print scanner.match()

from collections import namedtuple
Token = namedtuple('Token', ['type', 'value'])
def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup(), m.group())
#Example
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

tokens = (tok for tok in generate_tokens(master_pat, text) 
          if tok.type != 'WS')
for tok in tokens:
    print(tok)

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<LEQ>=)'
master_pat = re.match('|'.join([LE, LT, EQ]))
#master_pat = re.match('|'.join([LT, LE, EQ]))

PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
master_pat = re.match('|'.join([PRINT, NAME]))
for tok in generate_tokens(master_pat, 'printer'):
    print(tok)