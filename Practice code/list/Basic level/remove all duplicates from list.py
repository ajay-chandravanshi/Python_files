# Q. Write a program to remove all duplicates from a list.

L1=[10,20,1,2,10,20]
L2=[]
i=0
while(i<len(L1)):
     if L1[i] not in L2:
          L2.append(L1[i])
     i=i+1
print(L2)          