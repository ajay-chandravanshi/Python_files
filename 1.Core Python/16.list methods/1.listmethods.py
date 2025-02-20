l1=[10,20,'Ajay',30,40]

# append method
l1.append(10.5)
print(l1)
l1.append([10,20,30])
print(len(l1))
print(l1)

#extend method
l2=[10,20,'Ajay',30,40]
l2.extend([10,20,30])
print(len(l2))
print(l2)

# insert method
l3=[10,20,'Ajay',30,40]
l3.insert(0,'Raj')
print(l3)

# pop method
l4=[10,20,'Ajay',30,40]
print(l4.pop())
# l4.pop()
print(l4)
print(l4.pop())

# clear method
l5=[10,20,'Ajay',30,40]
l5.clear()
# del l5
print(l5)

# copy method
p5=[10,20,'Ajay',30,40]
p6=p5.copy()
print(p5)
print(p6)
print(id(p5),id(p6))

# count method
p7=[10,20,'Ajay',30,40,10]
print(p7.count(10))

# index method
p8=[10,20,'Ajay',30,40,10]
print(p8.index(10))
print(p8.index(10,1))

# reverse method
p8=[10,20,'Ajay',30,40,70]
p8.reverse()
print(p8)

# sort method
p9=[10,90,100,20,30,40,70]
p9.sort()
print(p9)
p9.sort(reverse=True)
print(p9)
