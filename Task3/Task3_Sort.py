#Insertion Sort 

n = input()

a = map(int,raw_input().split())

for i in range(1,n):
    t = a[i]
    j = i-1

    while( j>=0 and a[j]>t):
        a[j+1] = a[j]
        j-=1

    a[j+1] = t

print a
