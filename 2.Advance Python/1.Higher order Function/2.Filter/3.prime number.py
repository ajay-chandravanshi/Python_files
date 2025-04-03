l1 = [1, 2, 3, 4, 5, 67, 8]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Using filter() to get only prime numbers from the list
prime_numbers = list(filter(is_prime, l1))

print("Prime numbers in the list:", prime_numbers)
