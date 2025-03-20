# Q . Sort a list in ascending order without using sort()
L1=[166,1,10,12,7,8,3]
L2=[]
element=L1[0]
i=1
while(i<len(L1)):
     if(element>L1[i]):
          element=L1[i]
     i=i+1
     
L2.append(element)
print(element)          
print(L2)          
    

