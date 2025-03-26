def operants(x,y,operation):
    return operation(x,y)
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b

result1=operants(5,3,add)
result2=operants(5,3,multiply)

print(result1)
print(result2)