x=input()
l=x.split()
l1=[]
for i in l:
    if i not in l1:
     if l.count(i)==1:
        l1.append(i)
print(l1)
