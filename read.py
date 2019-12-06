#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'提取文件中的数字（浮点数）统一保存在list中'

__author__ = 'EoralMilk'


def isnum(c):
    if ((c == '0')or (c == '1')or(c == '2')or
        (c == '3')or(c == '4')or(c == '5')or
            (c == '6')or(c == '7')or(c == '8')or(c == '9')):
        return True
    else:
        return False


fileToOpen = open('mbox-short.txt', 'r')
strFromFile = fileToOpen.read()
s = strFromFile
itr = iter(s)
lis = []
tmp = []
flag = False
while True:
    try:
        c = next(itr)
    except StopIteration:
        break
    else:
        if isnum(c):
            flag = True
            tmp.append(c)
        elif c == '.' and flag:
            tmp.append(c)
            flag = False
        else:
            flag = False
            if len(tmp) > 0 and tmp[-1] != '.':
                stt = ''.join(tmp)
                if stt.find('.') != -1:
                    try:
                        lis.append(float(stt))
                    except ValueError:
                        pass
            tmp = []

print(lis)
# 做个平均值
sum = 0.0
for n in lis:
    sum = sum + n
avg = sum/len(lis)
print(avg)
