A={2,4,6,8}
B={1,2,3,4}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

A.intersection_update(B)
print(A)

B.difference_update(A)
print(B)

A.symmetric_difference_update(B)
print(A)