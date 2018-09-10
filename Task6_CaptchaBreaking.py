#for image containing two numbers and one operation 

from pytesseract import image_to_string 
from PIL import Image


c=0 # count variable for elif IsOperator case which is to make sure there are always two operands
def IsDigit(i):   # works
    for k in range(10):
        try:
            if int(i) == k:
                return 1

        except ValueError:   # if i == '+', we need to return 0 
            return 0



def IsOperator(i):    # works
    
    if i == '+':
        return 1
    elif i == '-':
        return 1
    elif i == '/':
        return 1
    elif i == '*':
        return 1

def WhichOperator(i , a):

    
    if i == '+':
        return a[0] + a[1]
    elif i == '-':
        return a[0] - a[1]
    elif i == '/':
        return a[0]/a[1]
    elif i == '*':
        return a[0]*a[1]
    

a= [0.0, 0.0]  # stores digits 


dir = raw_input("Enter file directory ")

s = image_to_string(Image.open(dir))   


for i in s:
    
    if IsDigit(i):   # works
        a[c] = float(i)
        c+=1

for i in s:
    
    if IsOperator(i):
       
        if c == 2 :
            res = WhichOperator(i, a) # where a is the list of two operands and i is the operatio

            print res

