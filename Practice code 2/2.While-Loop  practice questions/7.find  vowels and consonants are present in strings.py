#  Write a program to find how many vowels and consonants are present in strings.
str=input("Enter your name=")
i=0
vowels=consonant=0
while(i<len(str)):
    x=('A','a','E','e','I','i','O','o','U','u')
    y=str[i]
    if y in x:
        consonant=consonant+1
    else:
        vowels=vowels+1 
    i=i+1
           
print("Number of Consonant=",consonant)    
print("Number of Vowels=",vowels)
