# Q . Sort a list in ascending order without using sort()
L1=[166,1,7,2,5,4,3,256]
i=0
n=len(L1)
while(i<n):
    j=0
    while(j<n-1):
        if(L1[j]>L1[j+1]): 
            L1[j],L1[j+1]=L1[j+1],L1[j]
        j=j+1
    i=i+1       
print(L1)
