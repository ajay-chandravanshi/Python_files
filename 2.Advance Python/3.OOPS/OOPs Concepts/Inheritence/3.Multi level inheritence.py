
class GrandParent:
    def home(self):
        print("from Grandparent")
class parent(GrandParent):
    def car(self):
        print("from parent")   

class child(parent):
    def car(self):
        print("from child")
        super().car()

obj=child()
obj.home()
obj.car()