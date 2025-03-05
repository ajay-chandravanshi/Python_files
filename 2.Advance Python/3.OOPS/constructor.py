# ak class ke ander kitni constgructor bana sakte hai (n numbers of constructor bana sakte hai per last wala constructor hi call hoga bus )
# __init__(self) isse hamesha constructor banega hamesha
# bina consturctor call ke object nahi bana sakte hai
# class name ke aage () paranthesis responsible hota hai constructor call karne ke liye external wala 

class Student:
    def __init__(self):
        print("Constructor Called")

    def __init__(self):
        print("Constructor x Called")    
        # print(id(self))
    def display(self):
        print("Hello")
# obj=Student 
# ob.display()
obj=Student()
# obj.display()  
# print(id(obj)) 
obj.__init__()    


