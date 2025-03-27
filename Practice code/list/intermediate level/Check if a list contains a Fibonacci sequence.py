L = [0, 1, 1, 2, 3, 5, 8, 13]  
i = 2  
fibonacci = True  
print("List is=",L)
while i < len(L):  
    if L[i] != L[i - 1] + L[i - 2]:  
        fibonacci = False  
        break  
    i += 1  

if fibonacci:  
    print("The list follows a Fibonacci sequence.")  
else:  
    print("The list does NOT follow a Fibonacci sequence.")  
