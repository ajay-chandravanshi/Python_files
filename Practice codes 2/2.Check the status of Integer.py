a=int(input("Enter the First number="))
b=int(input("Enter the Second number="))
boolvalue= int(input("Enter a number (0 for False, any other number for True): "))
flag = bool(boolvalue)
if(a>0 or b>0) and (flag==False):
    print("True")
elif(a<0 and b<0) and (flag==True):
    print("True")  
else:
    print("False")     