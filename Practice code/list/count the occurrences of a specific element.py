# Q. Write a Python program to count the occurrences of a specific element in a list.

L1=[10,20,30,1,2,3,10,20,40,1,2,3,5,20,1]
i=0
count=0
element=int(input("Enter the element to count="))
while(i<len(L1)):
    if(L1[i]==element):
        count=count+1
    i=i+1
print(f"The Element {element} appears {count} times in the list")        