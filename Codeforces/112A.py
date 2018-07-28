
//passed, 372ms - py
// 62ms - c++ 14

a = raw_input()
b = raw_input()

for i in range(len(a)):
    t1 = a[i].upper()
    t2 = b[i].upper()
    if ord(t1) < ord(t2):
        
        print -1
        exit()
    elif ord(t1) > ord(t2):
        print 1
        exit()
    else:
        continue

print 0


        

