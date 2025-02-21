# Python program to print a multiplication table of a given number 

table=int(input("Enter the number those you want table="))
for i in range(1,table+9):
    print(f"{table} * {i} = {table*i}")
