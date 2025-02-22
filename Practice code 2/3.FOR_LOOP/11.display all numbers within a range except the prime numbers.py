#  Python program to display all numbers within a range except the prime numbers. 

num=int(input("Enter the number="))
count=0
for i in range(2,num):
    if(num%i==0):
        count=count+1
        break 

if(count!=0):
    print("Not a Prime Number")
else:
    print("This is Prime Number")    