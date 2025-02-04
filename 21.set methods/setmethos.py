s1={10,20,10,30,60,40,50}
s1.copy()
print(s1)
# s1.clear()
print(s1)
s1.add(90)
print(s1)
# s1.update({2,4,6})
s1.update('ajay')
print(s1)
# when use remove value is not in the array  code will be generate error
s1.remove(10)
print(s1)
# when use discard value is not in the array but code will be run 
s1.discard(100)
print(s1)
s1.pop()
print(s1)