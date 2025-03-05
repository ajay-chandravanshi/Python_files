class Student:
    def __init__(self):
        print("Constructor Called")
        # print(id(self))
    def display(self):
        print("Hello")
# obj=Student 
# ob.display()
obj=Student()
# obj.display()  
# print(id(obj)) 
obj.__init__()        