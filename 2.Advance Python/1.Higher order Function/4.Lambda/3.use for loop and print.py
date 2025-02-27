
# x=[[1,2,3],[1,2,3],[1,2,3]]
# l1=[]
# for i in range(1,4):
#     l1.append(i)
# print(l1)   
# l2=[]
# for i in range(4):
#     l2.append(l1)
# print(l2)


# above code solve using lambda

# x='neeraj'
# z=lambda x:[i for i in x]
# print(z(x))

# above code for loop in for loop

z=lambda p:[(i for i in range(1,p)) for k in range(p)]
print(z(4))