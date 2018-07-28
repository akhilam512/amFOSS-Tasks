a = raw_input()
t = ''
//incomplete
for i in range(len(a)):
    if a[i].isupper():
        a = a[:i] + lower(a[i]) + a[i+1:]
    

    if a[i] in 'aieouy':
        a = a[:i]+a[i+1:]

    else:
        t = a[:i]+ '.'+ a[i:]
        

print a

    
