# Write a program find odd no.(1,3,5,7,9,……) 
n=int(input("Enter the Number="))
i=0;
while(i<=n):
    if(i%2!=0):
        # print("The Odd Number is=",i)
        print(i,end=',')
    i=i+1    