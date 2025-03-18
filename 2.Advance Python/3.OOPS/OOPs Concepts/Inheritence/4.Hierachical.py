class parent:
    def home(self):
        print("this is c class")

class child(parent):
    def home(self):
        print("this is from child") 

class child1(parent):
    def neww(self):
        print("This is second child")            

obj=child()
obj=child1()
obj.home()
obj.neww()