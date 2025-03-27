# Q . Find the index of the last occurrence of an element in a list.
L = [10, 20, 30, 40, 50, 20, 60, 20]  # Example list
target = 20  # Element to find
i = len(L) - 1  # Start from the last index

while i >= 0:
    if L[i] == target:
        print("Last occurrence of", target, "is at index:", i)
        break
    i -= 1
