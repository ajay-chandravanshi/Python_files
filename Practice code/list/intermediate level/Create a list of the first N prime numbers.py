# Q. Create a list of the first N prime numbers.
# n=int(input("Enter the number of prime numbers:"))
# prime=[]
# i=2
# prime.append(2)
# while(len(prime)<n):
#     if(i%2==0):
#         prime.append(i)
#     i=i+1
# print(prime) 

L1=[1,3,2,4,5,6,9]
L2=[]
i=1
while(i<len(L1)):
    if(L1[i]%2!=0):
      L2.append(L1[i])
    i=i+1
print(L2)      
