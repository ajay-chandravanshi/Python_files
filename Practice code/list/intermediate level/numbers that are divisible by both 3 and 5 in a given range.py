# Q . Create a list of numbers that are divisible by both 3 and 5 in a given range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

divisible = []  # Empty list to store numbers
i = start

while i <= end:
    if i % 3 == 0 and i % 5 == 0:
        divisible.append(i)
    i += 1

print(divisible)
