#  Write a program to find how many vowels and consonants are present in strings.
str=input("Enter your name=")
i=0
consonant=0
vowels=0
while(i<len(str)):
    if(str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u"):
        consonant=consonant+1
    else:
        vowels=vowels+1 
    i=i+1
           
print("Number of Consonant=",consonant)    
print("Number of Vowels=",vowels)
