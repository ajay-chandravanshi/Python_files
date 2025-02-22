#  Python program that accepts a string and calculates the number of digits and letters. 
n=input("Enter the string=")
letter=0
digits=0
for i in n:
    x=ord(i)
    if(x>=48 and x<=57):
        digits=digits+1
    elif(x>=65 and x<=90 or x>=97 and x<=122):
        letter=letter+1  
print("The number of digits=",digits)           
print("The number of letters=",letter)        
       