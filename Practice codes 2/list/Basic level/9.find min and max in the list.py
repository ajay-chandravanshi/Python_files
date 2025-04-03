# Q. Write a program to find the maximum and minimum elements in a list.

L1=[0.5,1,123,1,100,1,10,20,4,3,50,70,90,120]
minn=maxx=L1[0]
i=1
while(i<len(L1)):
    if(L1[i]>maxx):
        maxx=L1[i]
    if(L1[i]<minn):
        minn=L1[i]
    i=i+1
print("The maximum value is=",maxx)            
print("The minimum value is=",minn)    



