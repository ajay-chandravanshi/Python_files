# Q . Find the intersection of two lists without using set().
L1 = [1, 2, 3, 4, 5, 6]
L2 = [4, 5, 6, 7, 8, 9]
L3 = []  # List to store the intersection
i = 0  

while i < len(L1):  
    j = 0  
    while j < len(L2):  
        if L1[i] == L2[j] and L1[i] not in L3:  
            L3.append(L1[i])  
        j += 1  
    i += 1  

print("Intersection:", L3)
