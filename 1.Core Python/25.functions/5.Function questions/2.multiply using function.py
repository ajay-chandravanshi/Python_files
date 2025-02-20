# multiply all the numbers in a list.
def multi(x):
    multi=1
    for i in x:
        multi=multi*i
    return multi   

x=eval(input("Enter the value in list="))
ans=multi(x)
print(ans)