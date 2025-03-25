# Q . Find the product of all elements in a list.
L = [1, 2, 3, 4, 5]  # Example list
product = 1  
i = 0  

while i < len(L):  
    product = product * L[i]  
    i += 1  

print("Product of all elements:", product)
