# Q.1. Write a Python program to find the sum of all elements in a list.

# L1=eval(input("Enter the list element="))
# L2=list(L1)
# sum=0
# i=0
# while (i<len(L1)):
#        sum=sum+L2[i]
#        i=i+1
# print("The sum of all the elements =",sum)    
    
# Q.2 Write a program to find the maximum and minimum elements in a list.

# L1=[10,2,50,1,70,0,100]
# i=0
# minimun=L1[i]
# # l2=min(L1)
# # l3=max(L1)
# # print(l2,l3) 
# while i<len(L1):
#     if L1[i]>minimun:
#         maxx=L1[i]
#     else:
#         minn=L1[i]    
#     minimun=L1[i]    
#     i=i+1 
# print("The maximum value=",maxx)   
# print("The minimum value=",minn)


# l1=list(input("Enter the list="))
# for i in l1:
#     print(i)

# Q.3 Write a Python program to count the occurrences of a specific element in a list.

L1=eval(input("Enter the list element="))
L2=list(L1)
i=0
count=0
element=int(input("Enter the element to count="))
while (i<len(L1)):
    if(L1[i]==element):
        count=count+1
    i=i+1
print(f"The Element {element} appears {count} times in the list")        
