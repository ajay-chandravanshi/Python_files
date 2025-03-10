# Q. Write a Python function to check if a given element exists in a list.

L1=eval(input("Enter the list="))
element=int(input("Enter the element you want check="))
if element in L1:
    print("Element is present")    
else:
    print("Element is not present")