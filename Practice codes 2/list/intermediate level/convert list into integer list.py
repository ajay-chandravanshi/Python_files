# Q .Convert a list of strings into a list of integers.
L1=["1","2","3","4","5"]
L2=[]
i=0
while(i<len(L1)):
    x=int(L1[i])
    L2.append(x)
    i=i+1
print(L2)
print(type(L2))