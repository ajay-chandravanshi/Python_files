# Q.   Count the number of digits in a given number.

num = int(input("Enter a number: "))  
count = 0  

while num > 0:  
    num = num // 10  # Remove the last digit  
    count += 1  # Increase count  

print("Number of digits:", count)  
