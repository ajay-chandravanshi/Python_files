# Q.1. Write a Python program to find the sum of all elements in a list.
L1=eval(input("Enter the list element="))
L2=list(L1)
sum=0
i=0
while (i<len(L1)):
       sum=sum+L2[i]
       i=i+1
print("The sum of all the elements =",sum)    
    