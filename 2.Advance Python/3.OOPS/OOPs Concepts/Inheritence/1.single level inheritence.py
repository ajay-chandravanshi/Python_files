

class A:
    x=10
    def home(self):
        print("Home from parent")
class B(A):                        # isme B child hai or A parent hai ( B(A) )
    def car(self):
        print("car from child")

obj=B()
obj.home()
obj.car()
print(obj.x)