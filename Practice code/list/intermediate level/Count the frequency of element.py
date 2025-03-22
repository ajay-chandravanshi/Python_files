# Q. Count the frequency of elements in a list 

L1=[5,7,5,9,7,5,9,9,9,7]
i=0
count=0
L2=[]
while(i<len(L1)):
    j=0
    count=0
    while(j<len(L1)):
        if(L1[i]==L1[j]):
            count=count+1
        j=j+1
    print(count) 
    i=i+1         