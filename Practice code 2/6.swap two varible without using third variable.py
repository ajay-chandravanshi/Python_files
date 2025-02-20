# Write a program to swap two variables using Addition and Substraction.

x=int(input("Enter the first number="))
y=int(input("Enter the second number="))
print("value of x=",x,"value of y=",y)
x=x+y
y=x-y
x=x-y
print("value of x=",x)
print("value of y=",y)