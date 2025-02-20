x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(id(x))
print(id(y))

#address  of x and y is difference in the above case 

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

e=10
f=10
print(id(e))
print(id(f))

#address  of e and f is same in the above case 