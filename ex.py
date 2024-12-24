x=input("Enter>")
l1=list(x)
print(l1)
l1.sort()
l2=[]
c=0
for i in l1:
    if l1.count(i)>=2:
        c+=1
        print(c)
    else:
        c+=0
print(c)


