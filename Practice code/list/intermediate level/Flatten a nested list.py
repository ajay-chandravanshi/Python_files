# Q .Flatten a nested list.

# Input:  [[10, 20], [30, [40, 50]], [60]]  
# Output: [10, 20, 30, 40, 50, 60] 

L1 = [[10, 20], [30, [40, 50]], [60]]
L2 = []

while L1:
    item = L1.pop(0)  # Remove the first element
    if isinstance(item, list):
        L1 = item + L1  # Flatten by adding elements back to the main list
    else:
        L2.append(item)  # Append non-list elements to the result

print(L2)

