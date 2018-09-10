n,k = map(int,raw_input().split())

a = map(int, raw_input().split())
    
c = 0

t = a[k-1]

for i in range(0,n):

    
    if a[i] >= t and a[i] > 0:
        c+=1

print c
