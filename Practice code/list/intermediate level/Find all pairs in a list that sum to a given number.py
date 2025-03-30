# Q . Find all pairs in a list that sum to a given number.

L1 = [2, 4, 3, 7, 5, 8, 1]
target_sum = 9
pairs = []
n = len(L1)

i = 0
while i < n:
    j = i + 1
    while j < n:
        if L1[i] + L1[j] == target_sum:
            pairs.append((L1[i], L1[j]))
        j += 1
    i += 1

print(pairs)
