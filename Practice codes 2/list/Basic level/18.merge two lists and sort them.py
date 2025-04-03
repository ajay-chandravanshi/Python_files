# Q.Write a Python program to merge two lists and sort them.

# code -1 using bubble sort 

L1=[2,20,10,1,70]
L2=[70,2,1,90,40]
i=0
while(i<len(L2)):
    L1.append(L2[i])
    i=i+1

n = len(L1)
for i in range(n):
    for j in range(n - i - 1):
        if L1[j] > L1[j + 1]:  # Swap if current element is greater than next
            L1[j], L1[j + 1] = L1[j + 1], L1[j]

print("Sorted List:", L1)

# code -2 using sort method 
L1=[2,20,10,1,70]
L2=[70,2,1,90,40]
i=0
while(i<len(L2)):
    L1.append(L2[i])
    i=i+1

print(L1)
L1.sort()
print(L1)