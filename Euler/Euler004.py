#!/bin/python
#incomplete
import sys

def isprime(t):
    for i in range(2,t/2+1):
        if t%i ==0:
            return 0
    return 1
    
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    
    
    i=n
    for i in range(n,0,-1):  # numbers with even number of digits which are divisible by 11 are always pallindromes!
        if i% 11 ==0:
            t=i/11
            if not(isprime(t)): # this check is not valid for all numbers, hence fails
                print i
                break
