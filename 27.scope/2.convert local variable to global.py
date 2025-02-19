x=10;
def update(p):
    global x
    x=p
    print(x)
y=int(input("Enter any number="))
print("Before Update Call=",x) 
update(y)
print("After Update Call=",x) 