# # serial  wise parameter 
# # 1.positional(x)/variable length(*args)
# # 2.key-word((y=0)/variable key-word(**args)

# # relation between parameter and arguments
 
# # 1st code 
# def add(x,*n,y=0,**m):
#     print("valueof x=",x)
#     print("valueof y=",y)
#     print("valueof n=",n)
#     print("valueof m=",m)
# res=add(10,20,30,40,y=20,z=10,p=2,q=4)  

# # 2nd code 
# def add(x,y=0):
#     print("valueof x=",x)
#     print("valueof y=",y)
   
# res=add(10,20)  

# # 3rd code 
# # def add(y=0,x):             this line generate error because of position in parameter
# #     print("valueof x=",x)
# #     print("valueof y=",y)
   
# # res=add(10,20)  

# # 4th code 
# def add(y,*n):
#     print("valueof y=",y)
#     print("valueof n=",n)
   
# res=add(10,20,30,40,50)  

# # 5th code 

# def add(*args,**kwargs):
#     print("valueof args=",args)
#     print("valueof kwargs=",kwargs)
   
# res=add(10,20,30,40,x=10,y=20,z=30)  

