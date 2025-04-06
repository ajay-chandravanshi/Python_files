# Q . Remove duplicate elements from a tuple.

T1 = (10, 20, 30, 20, 10, 40, 30)
T2 = tuple(set(T1))
print("Tuple after removing duplicates:", T2)
