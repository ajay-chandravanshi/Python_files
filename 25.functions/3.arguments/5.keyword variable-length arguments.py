# dubble ** star hamesha dictionary hi hold karega

# 1st code 

# def add(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# res=add(z=10,y=40,x=42,p=5,q=2)
# print(res)    

# 2nd code 

# def add(**kwargs):
#   print(kwargs)
 
# x=eval(input("Enter your dict="))
# # res=add(x) generate error in this line (unterminated string literal (detected at line 1))
# res=add(**x)
# print(res)

# 3rd code 

# def add(**kwargs):
#    print(kwargs.items())
 
# x=eval(input("Enter your dict="))
# res=add(**x)
# print(res)

# 4th code 
# {'name':'ajay','age':21,'qual':'B.tech'}
def add(**kwargs):
   for k,v in kwargs.items():
     print(f"My {k} is : {v}")
 
x=eval(input("Enter your dict="))
res=add(**x)
print(res)

