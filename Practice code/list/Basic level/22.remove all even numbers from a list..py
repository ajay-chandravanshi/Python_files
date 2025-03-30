# Q. Write a function to remove all even numbers from a list.

def ajay(L1):   
    i=0
    L2=[]
    while(i<len(L1)):
     
     if(L1[i] % 2 !=0):
        L2.append(L1[i])
     i=i+1
     
    return L2

L1=[10,2,3,1,4,6,5,78]
L1=ajay(L1)
print(L1)
      