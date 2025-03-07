# 1.code-1
# Q.1 Reverse a List:

# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# L1=[1,2,3,4,5]
# print(L1)
# L2=L1[::-1]
# print(L2)

# 2.code-2

# Q.2 Find the Maximum and Minimum in a List:

# Input: [10, 20, 5, 8, 90]
# Output: Max = 90, Min = 5

# lst = [10, 20, 5, 8, 90]
# # Initialize max and min with the first element of the list
# max_value = lst[0]
# min_value = lst[0]
# # Loop through the list to find max and min manually
# for num in lst:
#     if num > max_value:
#         max_value = num
#     if num < min_value:
#         min_value = num
# print(f"Max = {max_value}, Min = {min_value}")

# # above same code with another type 

# # Input: [10, 20, 5, 8, 90]
# # Output: Max = 90, Min = 5
# L1=[10,20,5,8,90]
# y=max(L1)
# z=min(L1)
# print("The maximum value=",y)
# print("The minimum value=",z)

# 3.code-3

# Q.3 Remove Duplicates from a List:

# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

L1=[1, 2, 2, 3, 4, 4, 5]
L2=[]
for num in L1:
    if num not in L2:
        L2.append(num)
print(L2)    

# code-4

# Q.4 Check if a List is Palindrome: 

# Input: [1, 2, 3, 2, 1]
# Output: True

L1=list(input("Enter the list="))
L2=L1[::-1]
if(L1==L2):
    print("this is a palindrome")
else:
    print("Not a palindrome") 