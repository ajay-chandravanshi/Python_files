# Q. Write a program to find the second largest element in a list.

L1=[5000,100,150,10,500,1000]
fir_larg=L1[0]
i=1
while(i<len(L1)):
    if(fir_larg<L1[i]):
        fir_larg=L1[i]
    i=i+1

sec_larg=0
j=0

while(j<len(L1)):
    if(sec_larg<L1[j] and L1[j]<fir_larg):
         sec_larg=L1[j]
    j=j+1     
print("The First Largest Value is=",fir_larg)
print("The Second Largest Value is=",sec_larg)