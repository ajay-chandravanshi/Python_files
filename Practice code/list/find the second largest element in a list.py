# Q. Write a program to find the second largest element in a list.

# L1=[150,10,20,1,3,40,90,100,120]
# First=L1[0]
# Second=L1[0]
# i=0
# while(i<len(L1)):
#     if(First<L1[i]):
#         Second=First
#         First=L1[i]
#     elif L1[i] > Second and L1[i] != First:
#         Second = L1[i]         
#     i=i+1
# print("The First Largest value=",First)        
# print("The Second Largest value=",Second)        

L1 = [150, 10, 20, 1, 3, 40, 90, 100, 120]

First = L1[0]
Second = None  # Initially set Second as None

i = 1  # Start loop from index 1
while i < len(L1):
    if L1[i] > First:
        Second = First  # Move First to Second
        First = L1[i]  # Update First
    elif Second is None or (L1[i] > Second and L1[i] != First):
        Second = L1[i]  # Update Second if it's smaller than First but greater than previous Second
    i += 1

print("The First Largest value =", First)        
print("The Second Largest value =", Second)
