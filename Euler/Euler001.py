#!/bin/python
# 60/100 points


import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    
    ls = [i for i in range(n) if i%3==0 or i%5==0 ]
    s=0
    for i in ls:
        s+=i
    print s
    
        
        
    
