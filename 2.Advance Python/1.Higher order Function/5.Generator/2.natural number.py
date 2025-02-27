def naturalno(x):
    i=1
    while i<=x:
        yield i
        i=i+1
n=int(input("enter the number="))
p=naturalno(n)
print(next(p))        
print(next(p))
for i in p:
    print(i)        