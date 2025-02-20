x=10;
def update(p):
    x=p
    print("Before Update=",globals()['x']) #this line (method=globals()['x']) access global variable to local variable
    print(x)

y=int(input("Enter any number="))
print("Before Update Call=",x) 
update(y)
print("After Update Call=",x) 