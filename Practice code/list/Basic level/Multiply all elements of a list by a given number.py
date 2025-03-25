# Q .  Multiply all elements of a list by a given number.
L = [1, 2, 3, 4, 5]  # Example list
num = 3  # Number to multiply each element by
i = 0  
print("List Before Update=",L)
while i < len(L):  
    L[i] = L[i] * num  
    i += 1  

print("Updated list:", L)
