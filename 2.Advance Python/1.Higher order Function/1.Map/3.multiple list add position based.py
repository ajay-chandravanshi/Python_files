
l1=[1,2,3,4]
l2=[2,3,4,5]
l3=[3,4]

def add(x,y,z):
    return x+y+z
p=tuple(map(add,l1,l2,l3))
print(p)