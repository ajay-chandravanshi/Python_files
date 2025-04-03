# Q . Find all even numbers in a list.

L1=[19,2,12,3,23,3,14,16]
L2=[]
i=0
while(i<len(L1)):
    if(L1[i]%2==0):
        L2.append(L1[i])
    i=i+1
print("The Even number is=",L2)