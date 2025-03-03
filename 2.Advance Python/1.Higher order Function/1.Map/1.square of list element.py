#length of (input element is equal to(=) length of output element) equal hai toh (map function lagagenge)

#only input and output equal hoga tab hi map function lagega

def sqr(n):
    return n**2
l1=eval(input("Enter any Collection="))
x=map(sqr,l1)
print(x)
print(list(x))



