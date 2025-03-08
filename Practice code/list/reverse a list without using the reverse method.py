# Q. Write a Python program to reverse a list without using the reverse() method.
# code-1

L1=[10,20,30,40,50]
L2=[]
i=len(L1)-1
print(i)
while(i>=0):
    L2.append(L1[i])
    i=i-1
print(L2)    

# reverse list code -2

# L1=[10,20,30,40,50]
# L2=L1[::-1]
# print(L2)