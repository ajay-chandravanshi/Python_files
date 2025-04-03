# Q . Extract every alternate element from a list.
L = [10, 20, 30, 40, 50, 60, 70]  # Example list
L2 = []  # New list to store alternate elements
i = 0  

while i < len(L):  
    L2.append(L[i])  
    i += 2  # Skipping every second element  

print("Alternate elements:", L2)
