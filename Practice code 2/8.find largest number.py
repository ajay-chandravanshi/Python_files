#Write a program to find largest no among the three inputs numbers. 

x=int(input("Enter the first number="))
y=int(input("Enter the second number="))
z=int(input("Enter the third number="))

print(f"Value of x={x} \nValue of y={y} \nValue of z={z}")

if(x>y and x>z):
    print("x is the largest number")
elif(y>x and y>z):
    print("y is the largest number")
else:
    print("z is the largest number")    