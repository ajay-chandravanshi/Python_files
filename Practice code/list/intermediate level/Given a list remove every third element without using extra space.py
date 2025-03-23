# Q .  Given a list, remove every third element without using extra space

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  
new_lst = []  
count = 0  

for i in range(len(lst)):  
    count += 1  
    if count % 3 != 0:  # Skip every third element
        new_lst += [lst[i]]  # Manually add elements

print(new_lst)  # Output: [1, 2, 4, 5, 7, 8, 10, 11]
