# # # Q . Find all prime numbers in a list.

# # L1=[1,4,3,5,7,2,9,11,21,23]
# # L3=[] 
# # for n in L1:
# #       if(n<2):
# #         continue
      
# #       count=0 
# #       i=1

# #       while(i<=n):
# #           if(n%i==0):
# #               count=count+1
# #               if(count>2):
# #                   break
# #           i=i+1
# #       if(count==2):
# #           L3.append(n)
# # print(L3)                 

# # # n=7
# # # count=0
# # # i=1
# # # while(i<=n):
# # #     print(i)
# # #     if(n%i==0):
# # #         count=count+1
# # #         if(count>2):
# # #             break
# # #     i=i+1
# # # print("the count=",count)    
# # # if(count==2):
# # #     print("this is a prime number")
# # # else:
# # #    print("not a prime")           

# L1=[10,1,3,16,7,21,23,29]
# L3=[]
# for n in L1:
#     if(n<=2):
#         continue
#     count=0
#     i=1
#     while(i<n):
#         if(n%i==0):
#             count=count+1
#             if(count>2):
#               break
#         i=i+1
#     if(count<=2):
#         L3.append(n)    
# print("The prime number is=",L3)         
# 
# 

L1=[10,1,3,16,7,21,23,29]
L2=[]
for n in L1:
    if(n<=2):
        continue
    count=0
    i=1
    while(i<n):
        if(n%i==0):
            count=count+1
            if(count>2):
                break
        i=i+1
    if(count==2):
        L2.append(n)
print(L2)               