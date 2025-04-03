# Q . Move all zeros in a list to the end while maintaining order
L1=[0,10,20,0,3,4,0,5,0,7]
L2=[]
L3=[]
i=0
while(i<len(L1)):
   if(L1[i]!=0):
      L2.append(L1[i])
   else:
      L3.append(L1[i])   
   i=i+1    
L2=L2+L3
print(L2)        