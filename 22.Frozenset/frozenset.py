s='ajay'
fs=frozenset(s)
print(type(fs))
print(fs)
print(max((fs)))
y=fs.copy()
print(y)
A={2,4,6,8}
x=frozenset(A)
B=[1,2,3,4]
y=frozenset(B)
print(A.difference(B))
print(A.symmetric_difference(B))
print(A.union(B))
print(A.intersection(B))
