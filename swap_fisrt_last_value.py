
x=12345
y=str(x)
z=list(y)
c=z[0]
d = z[len(z)-1]
z[0] = d
z[len(z)-1] = c
print(z)