# generator is a key word

def first():
    # return 'Hello'
    yield 1
    yield 2
    yield 3
x=first()
# print(x)
# print(list(x))
print(next(x))
print("hi")
print("Hello")
print("Welcome")
print(next(x))

