# Q .Find the difference between two lists.

L1 = [1, 2, 3, 4, 5, 6]
L2 = [4, 5, 6, 7, 8, 9]

L3 = []  # List to store the difference
i = 0

while i < len(L1):  
    j = 0
    found = False
    while j < len(L2):  
        if L1[i] == L2[j]:  
            found = True
            break  
        j += 1
    if not found:
        L3.append(L1[i])
    i += 1

print(L3)
