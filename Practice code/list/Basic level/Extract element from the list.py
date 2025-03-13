# Q. List Slicing: Extract [20, 30, 40] from lst = [10, 20, 30, 40, 50].

# code type=1
# lis=[10,20,30,40,50]
# extract=[]
# i=1
# while(i<len(lis)-1):
#     extract.append(lis[i])
#     i=i+1
# print("the extract lis is =",extract)
# print("the remainig element in the list is=",lis[0],lis[len(lis)-1])    

# code type=2

lst = [10, 20, 30, 40, 50]
extract_lis = lst[1:4]
print("The extract lis is =",extract_lis)