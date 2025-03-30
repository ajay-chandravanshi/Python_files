L = [10, 20, 30, 40, 50, 20, 60]  # Example list
target = 20  # Element to find
i = 0  

while i < len(L):  
    if L[i] == target:  
        print("First index of", target, "is:", i)  
        break  
    i += 1  
