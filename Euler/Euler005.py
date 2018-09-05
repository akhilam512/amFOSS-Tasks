#!/bin/python

#passed all test cases
import sys
import fractions

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    
    ans = 1
    
    for i in range (1, n+1):
        ans = (ans*i) / (fractions.gcd(ans,i))  # gcd * lcm = a * b
        
    print ans
    
    
    
    
