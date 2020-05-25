# -*- coding: utf-8 -*-
"""
Created on Fri May 22 02:16:45 2020

@author: asus
"""
###字典序大于后一个的删除
###重点在于删除之后指针要往前移一位


import sys
n = int(sys.stdin.readline().strip())
ans = 0
values = []
strings = []
for i in range(n*2):
    if i%2==0:
        line = sys.stdin.readline().strip()
        values.append((list(map(int, line.split()))))
    else:
        line = sys.stdin.readline().strip()
        strings.append(list(map(str, line.split())))
def remove(string1,n,m):
    m = min(m,n)
    i = 0
    while(i<(n-1) and m != 0):
        #print(i,string1[0])
        if string1[0][i] > string1[0][i+1]:
            string1[0] = string1[0][:i]+string1[0][i+1:]           
            m -= 1
            n -= 1
            if i > 0 :
                i -= 1
        else:
            i += 1

length = len(values)
#print(length)
for i in range(length):
    n,m = values[i]
    #print(n,m)
    string1 = strings[i]
    #print(string1)
    remove(string1,n,m)
    print(string1[0])
    
        
        
