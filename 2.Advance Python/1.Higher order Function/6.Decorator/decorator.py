# kis bhi function ke code ko bina change kiye hue internal behaviour ko change karna 
# decorater is a higher order function (special type of function) 
# decorator is a special type of function they take function as argument and return the function 

# def add(x,y):
#     return x+y
# p=add(10,20)
# print(p)

# decorator code 
# code 1
def outer_fun(new):
    def inner_fun():
        print("Hello")
    return inner_fun
@outer_fun
def new():
    pass                #bus aage badane ke liye use karte hai isse error nhi aata hai
new()    

