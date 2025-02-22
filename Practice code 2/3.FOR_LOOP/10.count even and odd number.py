# Python program to count the number of even and odd numbers from a series of numbers.

num=int(input("Enter the number="))
count_even=0
count_odd=0
for i in range(1,num+1):
    if(i%2==0):
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("The Even Number Count=",count_even)        
print("The Odd Number Count=",count_odd)        
