# Q . Find the Missing number in a list of 1 to n 
L1=[1,3,4,6,7,9,10,11,16]
i=1
L2=[]
n=L1[len(L1)-1]
while(i<=n):
    if i not in L1:
        L2.append(i)
    i=i+1
print(L2)        