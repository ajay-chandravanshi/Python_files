# Q . Count how many times each element appears in a list.

L = [1, 2, 3, 2, 1, 4, 1, 5, 2, 4, 4, 4]
counted = []  # To track counted elements
i = 0

while i < len(L):
    if L[i] not in counted:
        counted.append(L[i])  # Mark as counted
        count = 0
        j = 0
        while j < len(L):
            if L[i] == L[j]:
                count += 1
            j += 1
        print(L[i], "appears", count, "times")
    i += 1
