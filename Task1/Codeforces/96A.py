s = raw_input()
c=0

for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        c=0


if c<7:
    print "NO"
else:
    print "YES"
    
