# Q. Write a program to filter out negative numbers from a list.

L1=[-1,4,6,-6,9,3,-10,-13,45,-6]
L2=[]
i=0
while(i<len(L1)):
    if(L1[i]<0):
        L2.append(L1[i])
    i=i+1
print("Negative numbers from a list=",L2)        