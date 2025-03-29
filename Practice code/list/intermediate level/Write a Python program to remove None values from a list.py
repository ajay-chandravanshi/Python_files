# Q . Write a Python program to remove None values from a list

L1 = [None, None, None, 'hello', None,None, 'world']
L2=[]
for i in L1:
    if(i!=None):
        L2.append(i)
L1=L2        
print(L1)       