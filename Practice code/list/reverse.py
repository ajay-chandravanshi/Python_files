# 1.code-1

# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# L1=[1,2,3,4,5]
# print(L1)
# L2=L1[::-1]
# print(L2)

# 2.code-2

# Input: [10, 20, 5, 8, 90]
# Output: Max = 90, Min = 5

lst = [10, 20, 5, 8, 90]

# Initialize max and min with the first element of the list
max_value = lst[0]
min_value = lst[0]

# Loop through the list to find max and min manually
for num in lst:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print(f"Max = {max_value}, Min = {min_value}")
