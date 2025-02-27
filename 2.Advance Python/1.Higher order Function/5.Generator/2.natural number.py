def naturalno(x):
    i=1
    while i<=x:
        yield i
        i=i+1
n=int(input("enter the number="))
p=naturalno(n)
next(p)             #ise output nhi aayega value aage bada dega bus        
print(next(p))
# for i in p:
#     print(i)        