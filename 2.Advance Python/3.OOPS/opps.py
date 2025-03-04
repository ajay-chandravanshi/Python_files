# class(Blue print of a object is called class/Dummy Model/Design of an Object)

# object(Instence of an class/Physical existence of class) 

# syntax:- Class Class_Name:
#                   "doc String"
#                    Variables(Static/class variable,instence variable,Local Variable) 
                    #  methods(Constructor (Special method),instance method,static method,class method)

# interview question = kya class bina consturctor ke class ban sakti hai (ans= ha ban sakti hai)

class First:
    "This is a Class"
    x=10
    def new():
        print("Hello")
obj=First
print(obj.x)
obj.new() 
print(First.__doc__)       