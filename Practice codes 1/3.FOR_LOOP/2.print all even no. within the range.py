# Python program to print all the even numbers within the given range. 

num=int(input("Enter the range="))

for i in range(1,num+2):
    if(i%2==0):
        print("Even number is=",i)
        i=i+1