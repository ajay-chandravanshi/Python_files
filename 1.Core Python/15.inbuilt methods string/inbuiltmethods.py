sr1='I Love Python'
print(sr1.lower())
print(sr1.upper())
print(sr1.swapcase())
print(sr1.title())
print(sr1.capitalize())
print(sr1.count('o'))
# print(sr1.index('p'))
print(sr1.index('P'))
print(sr1.find('P'))
print(sr1.find('p'))

# parameter of split('cahr',how many times)
s="I Love Python"
print(s.split())
print(s.split('o',1))
# below code is output error 
# print(s.split('',1))

# join()
s1='Ajay'
s2='chandravanshi'
s3='from bhopal'
x=[s1,s2,s3]
print(''.join(x))
print(' '.join(x))
print('new '.join(x))
print(type('new'.join(x)))