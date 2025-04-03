# Python program to check if the given string is a palindrome.
x=input("Enter the string=")
if(x==str(x[::-1])):
    print("This is a palindrome")
else:
    print("Not a palindrome")    