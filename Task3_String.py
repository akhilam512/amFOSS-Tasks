# Problem - Concatenate 3 at a time and check if palindrome

s = ''
for i in range(1,13):
    s+=raw_input()

    if i%3 ==0:
        if s == s[::-1]:
            print "Palindrome"
        else:
            print "Not Palindrome"

        s=''


        


