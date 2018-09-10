n = input()
C = 0

for i in range(n):
    a,b,c = map(int, raw_input().split())

    if a>0 and b>0:
        C+=1

    elif b>0 and c>0:
        C+=1

    elif c>0 and a>0:
        C+=1

    elif (c>0 and b>0) and a>0:
        C+=1


print C
        
    
