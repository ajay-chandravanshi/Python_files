percent=int(input("Enter your percentage="))
if(percent>=60 and percent<100):
    print(f'{percent} is first division')

elif(percent>=45 and percent<60):
         print(f'{percent} is second division')

elif(percent>=33 and percent<45):
         print(f'{percent} is third division')

elif(percent>=0 and percent<33):
         print('you are fail')

else:
    print("Invalid input")    