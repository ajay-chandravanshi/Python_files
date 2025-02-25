# A function without name
# use lambda keyword
#it takes n number of argument
# but execute only single line of expression

#syntex:- Lambda arguments:expression

# example:-1 write a function to add two number

# first type

x=int(input("Enter the first value="))
y=int(input("Enter the second value="))
res=lambda p,q:p+q
print(res(x,y))

#second type

x=int(input("Enter the first value="))
y=int(input("Enter the second value="))
res=lambda p,q:print(p+q)
res(x,y)