#  Python program to get the Fibonacci series. (0,1,1,2,3,5,8,13,21……………..) 
n=int(input("Enter the number="))
a=0
b=1
while(a<=n):
    print(a)
    a,b=b,a+b   