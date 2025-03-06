# In this (school and city) is a static variable because their value is not change 

# declaration(Inside class=outside method)

# class Student:
#     school='SHSS'
#     city='Bhopal'

#     def __init__(self,name,roll):
#         self.x=name
#         self.y=roll

#     def show(self):
#         print(self.x,self.y)    
#         print(Student.school)    
#         print(Student.city)    

# obj1=Student('Ajay',101)
# obj1.show()
# obj2=Student('Animesh',102)
# obj2.show()

class Student:
    school='SHSS'
  

    def __init__(self,name,roll):
        self.x=name
        self.y=roll
        Student.city='Bhopal'

    def show(self):
       Student.s_code=123

    def display(self):
        print(Student.s_code)     
        print(Student.city)     
        print(Student.school)     
        print(Student.principle)

Student.principle='Rahul'        
obj=Student('Ajay',101)
obj.show()
obj.display()