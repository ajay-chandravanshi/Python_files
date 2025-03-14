# Q . Write a Python program to find the common elements between two lists.
L1=[12,67,34,10,20,50]
L2=[12,17,34,50,10,40]
L3=[]
i=0
j=0
# if(len(L1)>len(L2)):
while(i<len(L1)):
   
   while(j<len(L2)): 
     if (L1[j]==L2[j]):
      L3.append(L2[j])
     j=j+1
   i=i+1  
print(L3)               