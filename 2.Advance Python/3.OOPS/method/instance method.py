# aisi method jinka pehla parameter (self hona chahiye) hota hai
# instance method ko ak dushre ke ander call kane ke liye pehle (class name . function name)

class Student:
    def first(self):
        print("This is form first")
    def second(self):
        Student.first(self)
        obj1=Student()
        obj1.first()
obj=Student()
obj.first()
obj.second()             