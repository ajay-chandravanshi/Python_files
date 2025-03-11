# L1=eval(input("Enter the natural number upto 10="))
# print(L1)

# L1=eval(input("Enter the list element="))
# # L1=[10,20,30,40,50]
# i=sum=0
# while(i<len(L1)):
#     sum=sum+L1[i]
#     i=i+1
# print(sum)    

L1=[100,1,34,5,1,67,56,45,90,200,0]
i=0
min=max=L1[i]
while(i<len(L1)):
    if(max<L1[i]):
        max=L1[i]
    elif(min>L1[i]):
        min=L1[i] 
    i=i+1
print("Maximum value=",max)           
print("Minimum value=",min)           