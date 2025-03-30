# Q. Remove all occurrences of a specific element from a list. 

# code type =1
# L1=[2,10,1,45,2,3,1,45,90] 
# L2=[]
# i=0
# print(L1)
# element=int(input("Enter the element you want remove="))
# while(i<len(L1)):
#  if(element!=L1[i]):
#     L2.append(L1[i])
#  i=i+1
# L1=L2    
# print(L1)    

# code type =2 
# L1=[2,10,1,45,2,3,1,45,90] 
# i=0
# print(L1)
# element=int(input("Enter the element you want remove="))
# while(i<len(L1)):
#  if(element==L1[i]):
#     L1.remove(L1[i])
#  i=i+1 
# print(L1)    

# code type =3 

L1=[2,10,1,45,2,3,1,45,90] 
i=0
print(L1)
element=int(input("Enter the element you want remove="))
while(i<len(L1)):
 if(element==L1[i]):
    L1.pop(i)
 i=i+1 
print(L1)    