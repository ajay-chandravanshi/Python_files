# Q . Replace every element in a list with the product of all other elements (without using division).\

L1=[2,4,5,3,6,7,1,10]
L2=[]
i=0
n=len(L1)
while(i<n):
    j=0
    output=1
    while(j<n):
        if (i!=j):
           output=output*L1[j]
        j=j+1  
    L2.append(output)
    i=i+1 
print(L2)

 