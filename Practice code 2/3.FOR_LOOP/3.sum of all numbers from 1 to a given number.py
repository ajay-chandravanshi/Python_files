#  Python program to calculate the sum of all numbers from 1 to a given number. 

num=int(input("Enter the number="))
sum=0
for i in range(num+1):
     sum=sum+i
     i=i+1
print(sum)    