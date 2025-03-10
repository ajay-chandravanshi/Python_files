

class A:
    x=10
    def home(self):
        print("Home from parent")
class B(A):
    def car(self):
        print("car from child")

obj=B()
obj.home()
obj.car()
print(obj.x)