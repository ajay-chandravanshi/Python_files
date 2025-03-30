L1 = [1, 2, 3, 4, 5]
L2 = [4, 5, 6, 7, 8]
L3 = []  # List to store the union
i = 0  

# Add all elements of L1 to L3
while i < len(L1):  
    if L1[i] not in L3:
        L3.append(L1[i])  
    i += 1  

i = 0  
# Add all elements of L2 to L3 (only if not already present)
while i < len(L2):  
    if L2[i] not in L3:  
        L3.append(L2[i])  
    i += 1  

print("Union:", L3)
