# Q .Flatten a nested list.

# Input:  [[10, 20], [30, [40, 50]], [60]]  
# Output: [10, 20, 30, 40, 50, 60] 
L1=[[10, 20], [30, [40, 50]], [60]]
L2=[]
for i in L1:
    for n in i:
         L2.append(n) 
         # print(n) 
print(L1)
for i in L2:
    print(i)   
print(L2)
