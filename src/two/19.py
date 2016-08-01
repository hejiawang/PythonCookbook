#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2.19    编写一个简单的递归下降解析器
Created on 2016年8月1日
@author: wang
'''

'''
expr ::= expr + term
    | expr - term
    | term
term ::= term * factor
    |term / factor
    | factor
factor ::= ( expr )
    | NUM
'''

'''
expr ::= term { (+|-) term }*
term ::= factor { (*|/) factor }*
factor ::= ( expr )
    | NUM
'''    
