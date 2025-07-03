x=str(input('enter the name:'))
y=('a','e','i','o','u','A','E','I','O','U')
i=0
z=[]
vowels=0
consonant=0
while i<len(x):
    if x[i] in y:
        if x[i] not in z:
            z.append(x[i])
            vowels=vowels+1
    else:
        consonant=consonant+1    
    i=i+1
print('Total vowels in str=',vowels)
print('Total consonant in str=',consonant)
