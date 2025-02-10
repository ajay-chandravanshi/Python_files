# hcf
x=8
y=12
m=min(x,y)
while m>0:
    if x%m==0 and y%m==0:
        hcf=m
        break
    m=m-1
print("HCF is =",hcf)    