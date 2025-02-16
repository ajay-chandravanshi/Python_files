def add(x):
    sum=0
    for i in x:
        sum=sum+i
    return sum
x=eval(input("Enter the value in list="))
res=add(x)
print(res)