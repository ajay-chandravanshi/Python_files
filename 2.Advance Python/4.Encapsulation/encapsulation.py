# Wrapping variables as well as methods in a single unit is called Encapsulation

class Book:
    price=100
    def __init__(self,name):
        self.author=name

    def add (self,total_pages):
        self.pages=total_pages

    @classmethod
    def update_price(cls,x):
        p="Hello"
        cls.porice=x

    @staticmethod
    def greet():
        print("Welcome to my web-page")

obj=Book()
obj.greet()            