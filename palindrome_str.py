x='121'
b=''
i=len(x)-1
while i>=0:
    b=b+x[i]
    i=i-1
if x==b:
    print('this is palindrome')
else:
    print('not a palindrome')        
# print(b)