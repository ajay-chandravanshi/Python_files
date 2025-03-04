class Student:
    def __init__(self):
        print("This is Constructor")
        print(id(self))
    def display(self):
        print("Hello")
# obj=student 
# ob.display()
obj=Student()
# obj.display()  
print(id(obj))         