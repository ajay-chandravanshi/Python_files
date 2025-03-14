# Q . Split a list into two equal halves.
L1=[1,2,3,4,5,6,7]
L2=[]
L3=[]
x=int(len(L1)/2)
print(x)
i=0
while(i<len(L1)):
    if(i<x):
     L2.append(L1[i])
    elif(i>=x):
      L3.append(L1[i])
    i=i+1    
print(L2,L3)