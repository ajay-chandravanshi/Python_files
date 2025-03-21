l1=[1,2,3,4,5,67,8]
count=0
for i in range(2,len(l1)):
     if(i%l1==0):
          count=count+1
if(count!=0):
     print("this is a prime number")
else:
     print("not a prime number")               