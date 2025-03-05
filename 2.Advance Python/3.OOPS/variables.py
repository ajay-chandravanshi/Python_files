# aise variable jo object badlne ke sath mai apni value badal de aise variable instance variable kehlate hai
# self ke sath jo variable hota hai ussi ko instance variable bolte hai
 
# 1.Instance variable
# code-1(a)

# class Student:
#     def __init__(self,name,marks):
#         self.x=name
#         self.y=marks
# obj=Student('Ajay',80)  
# print(obj.x)      
# print(obj.y) 

# above same code in another way
#  code-1(b)

class Student:
    def __init__(self,name,marks):
        self.x=name
        self.y=marks
    def show(self): 
        print(self.x)   
        print(self.y)   
obj=Student('Ajay',80)  
obj.show()
obj1=Student('Ajay',30)  
obj1.show()

