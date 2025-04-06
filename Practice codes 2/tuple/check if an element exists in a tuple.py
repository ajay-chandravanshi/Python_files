# Q . Write a program to check if an element exists in a tuple.

T1 = (10, 20, 30, 40, 50)
element = int(input("Enter the element to search: "))

if element in T1:
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")
