# Q . Check if all elements in a list are unique.


L = [1, 2, 3, 4, 5, 6]
i = 0
is_unique = True

while i < len(L):
    j = i + 1
    while j < len(L):
        if L[i] == L[j]:  
            is_unique = False
            break
        j += 1
    if not is_unique:
        break
    i += 1

if is_unique:
    print("All elements are unique")
else:
    print("Duplicate elements found")
