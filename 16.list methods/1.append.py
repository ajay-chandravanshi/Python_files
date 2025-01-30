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