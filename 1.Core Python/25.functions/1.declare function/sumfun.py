def add(x,y,z):
    "for addition of 3-variables"
    return x+y+z
p=int(input("Enter 1st no="))
q=int(input("Enter 2nd no="))
r=int(input("Enter 3rd no="))
res=add(p,q,r)
print(res)
print(add.__doc__)

# below code generate error=(TypeError: add() missing 1 required positional argument: 'z')
# def add(x,y,z):
#     "for addition of 3-variables"
#     return x+y+z
# p=int(input("Enter 1st no="))
# q=int(input("Enter 2nd no="))
# r=int(input("Enter 3rd no="))
# res=add(p,q)
# print(res)
# print(add.__doc__)