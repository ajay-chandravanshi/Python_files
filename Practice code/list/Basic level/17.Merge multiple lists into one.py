# Q . Merge multiple lists into one.
L1 = [1, 2, 3]  
L2 = [4, 5, 6]  
L3 = [7, 8, 9]
print("The Different Lists are=",L1,"\n",L2,"\n",L3)  
merged_list = []  

i = 0  
while i < len(L1):  
    merged_list.append(L1[i])  
    i += 1  

i = 0  
while i < len(L2):  
    merged_list.append(L2[i])  
    i += 1  

i = 0  
while i < len(L3):  
    merged_list.append(L3[i])  
    i += 1  

print(merged_list)  

