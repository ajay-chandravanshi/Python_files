# aise variable jo object badlne ke sath mai apni value badal de aise variable instance variable kehlate hai
# self ke sath jo variable hota hai ussi ko instance variable bolte hai
 
# 1.Instance variable
class Student:
    def __init__(self,name,marks):
        self.x=name
        self.y=marks
obj=Student('Ajay',80)  
print(obj.x)      
print(obj.y)      