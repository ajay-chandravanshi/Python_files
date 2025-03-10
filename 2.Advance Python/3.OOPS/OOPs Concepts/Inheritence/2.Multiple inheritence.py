# isme A and C Parent hai and B jo hai wo child hai
# ak child ke ander 2 parent hai 
# isme left wale ki priority jyad rahegi child ke ander jo prent hai usme se
# MRO apply hota hai parent par jo child ke ander hai (B(A,C)) , yaha per deft FIRST algorithm lagti hai 
# MRO(method resolution Order)
# MRO sb pai apply hoga 5 pancho par 

# class C:
#     def bank(self):
#         print("this is c class")

# class A:
#     x=10
#     def home(self):
#         print("Home from parent")
# class B(A,C):                        # isme B child hai or A parent hai ( B(A) )
#     def car(self):
#         print("car from child")

# obj=B()
# obj.home()
# obj.bank()
# obj.car()

# method overiding

# class parent:
#     def home(self):
#         print("this is c class")

# class child(parent):
#     def home(self):
#         print("this is from child")        

# obj=child()
# obj.home()

# Super method

class parent:
    def home(self):
        print("this is c class")

class child(parent):
    def home(self):
        print("this is from child") 
        super().home()       

obj=child()
obj.home()