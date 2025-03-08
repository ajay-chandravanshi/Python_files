# Q.1. Write a Python program to find the sum of all elements in a list.
# list mai jab input mai denge run karne par toh [] isme denge 
# L1=eval(input("Enter the list element="))   
# sum=0
# i=0
# while (i<len(L1)):
#        sum=sum+L1[i]
#        i=i+1
# print("The sum of all the elements =",sum)         

# Q.4 Write a program to remove all duplicates from a list.

# L1=[10,20,10,1,3,1,4]
# L3=[]
# i=0
# while (i<len(L1)):
        
#         if L1[i] not in L3:
#           L3.append(L1[i])      
#         i=i+1 
        
# print(L3)      

L1=[10,20,1,2,10,20]
L2=[]
i=0
while(i<len(L1)):
     if L1[i] not in L2:
          L2.append(L1[i])
     i=i+1
print(L2)          