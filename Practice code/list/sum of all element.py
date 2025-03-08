# Q.1. Write a Python program to find the sum of all elements in a list.
# list mai jab input mai denge run karne par toh [] isme denge 

L1=eval(input("Enter the list element="))   
sum=0
i=0
while (i<len(L1)):
       sum=sum+L1[i]
       i=i+1
print("The sum of all the elements =",sum)         
