#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.12    找出序列中出现次数最多的元素
Created on 2016年7月24日
@author: wang
'''

words = [
            'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
            'the', 'look'
         ]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print top_three

print word_counts['look']
print word_counts['the']

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print word_counts['eyes']
print word_counts['why']

word_counts.update(morewords)
print word_counts['eyes']
print word_counts['why']

a = Counter(words)
b = Counter(morewords)
print a
print b
c = a + b
print c
d = a - b
print b



