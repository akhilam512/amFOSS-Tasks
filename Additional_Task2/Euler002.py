#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    
    t1 = 0
    t2 = 1
    s=0
    req=0
    
    while(s<n):
        
        
        if s%2 ==0:
            req+=s
        s = t1 + t2
        t1 = t2
        t2 = s
    print req
        
        
    #print req
        
        
        
    
    
    
