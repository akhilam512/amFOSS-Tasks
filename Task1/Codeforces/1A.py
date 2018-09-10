n,m,a = map(int, raw_input().split())
d= int((n*m) /  (a**2))

if (((n*m) %  (a**2))==0):
    print d
else:
    print d+1
