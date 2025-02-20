# Write a Python function that accepts a string and counts the number of upper and lower case letters.
def findd(value):
    UPPER_CASE=0;
    LOWER_CASE=0;
    for i in value:
      if(i.isupper()):
          UPPER_CASE= UPPER_CASE+1
      elif(i.islower()):
           LOWER_CASE= LOWER_CASE+1
      else:
          pass
    return  UPPER_CASE,LOWER_CASE         

value=eval(input("Enter the string="))
ans=findd(value)
print("Uppercase and Lowercase",ans)