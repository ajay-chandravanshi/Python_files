
num=int(input("Enter the range="))
sum=0
for i in range(num+1):
    if(i%2!=0):
        sum=sum+i
        i=i+1
print(sum)        