# 1/5 test cases only.

#!/bin/python

import sys
def checkprime(n):
    
    f=1
    for i in range(2,n/2+1):
        if n%i ==0 :
            f=0
            break
            
    if f==1:
        print n
    else:
        checkprime(n/2)  # fails for odd composite numbers (9,21,25,etc) and its multiples.
        
            

t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    
    checkprime(n)
    
    
