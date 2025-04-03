# Python program to check if a given number is an Armstrong number.(153=1**3+5**3+3**3)

n=int(input("Enter the number="))
x=y=n
digit=0
while(n>0):
  n=n//10
  digit=digit+1    
# print(digit)
# print(n)

sum=0
while(x>0):
  last_digit=x%10
  sum=sum+last_digit**digit
  x=x//10
# print(sum)
# print(x)

if(sum==y):
  print("This is a Armstrong number") 
else:
  print("Not a Armstrong number")   