# Q . Rotate a list to the right by k positions.

L1=[10,20,30,40,50]
L2=[]
k=3
i=len(L1)-k
while(i<len(L1)):
    L2.append(L1[i])
    i=i+1

i=0
x=len(L1)-k
while(i<x):
    L2.append(L1[i])
    i=i+1
print(L2)    