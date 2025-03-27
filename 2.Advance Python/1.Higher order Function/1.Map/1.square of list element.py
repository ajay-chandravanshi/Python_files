#length of (input element is equal to(=) length of output element) equal hai toh (map function lagagenge)

#only input and output equal hoga tab hi map function lagega

def square(x):
    return x**2
y=eval(input("Enter the number="))
result=list(map(square,y))
print(result)



