# cursor ki position move karne ke liye use karte hai 
# seek(where we move,move from) syntax of seek
# positive negative indexing support hoti hai seek mai

f=open('f2.txt','a+')
print(f.tell())
f.write("Hello")
print(f.tell())
f.seek(0)
print(f.tell())
data=f.read(10)
print(data)