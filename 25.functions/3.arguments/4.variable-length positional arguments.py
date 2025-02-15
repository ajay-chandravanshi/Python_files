# in this * means all 
# *args only tuple hold karega add(*args)
# def add(*n):
#    print(n)
#    print(type(n))

# one code in 2 ways 

# first type 

# res=add(2,4,6,8,9,12,234,43,3)
# print(res)

# def add(*args):
#   sum=0
#   for i in args:
#       sum=sum+i
#   return sum

# x=eval(input("Enter your values="))
# res=add(*x)
# print(res)

# second type 

def add(*args):
  sum=0
  for i in args:
      for j in i:
       sum=sum+j
  return sum

x=eval(input("Enter your values="))
res=add(x)
print(res)