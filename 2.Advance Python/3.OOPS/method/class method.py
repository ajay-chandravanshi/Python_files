# static variable or class variable  ko modify karne ke liye hum class method ka use karte hai
# class method banane ke liye (@classmethod) ka use karte hai
# class method ka first parameter cls hota hai


class Book:
    price=100
    total_pages=500
    def __init__(self,stu_name):
        self.x=stu_name
        print(self.x,Book.price,Book.total_pages)

    @classmethod                #this is a classmethod
    def update(cls,p,q):
        cls.price=p
        cls.total_pages=q
obj1=Book('Ajay')
obj2=Book('Ayush')
obj3=Book('Animesh')
Book.update(150,600)
obj4=Book('Arvind')
