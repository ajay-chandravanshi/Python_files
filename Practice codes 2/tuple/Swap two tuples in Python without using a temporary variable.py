# Q . Swap two tuples in Python without using a temporary variable.

T1 = (1, 2, 3)
T2 = (4, 5, 6)

print("Before Swapping:")
print("T1 =", T1)
print("T2 =", T2)

# Swapping without temp variable
T1, T2 = T2, T1

print("After Swapping:")
print("T1 =", T1)
print("T2 =", T2)
