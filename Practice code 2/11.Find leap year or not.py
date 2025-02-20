# Write a program to find given year is leep year or not.

year=int(input("Enter the year="))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("This is a leap year")
else:
    print("Not a Leap year")     