#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
1.3    保存最后N个元素
yield    生成器函数
deque(maxlen=x)    创建一个固定长度的队列
Created on 2016年7月23日
@author: wang
'''
from _collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen = history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print (pline) #print (pline, end='')
            print (line) #print (pline, end='')
            print ('-'*20)
            
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print q
q.append(4)
print q

q = deque()
q.append(1)
q.append(2)
q.append(3)
print q
q.appendleft(4)
print q
q_pop = q.pop()
print q_pop
print q
q_popleft = q.popleft()
print q_popleft
print q

