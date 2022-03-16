l=input().split()
x=[]
for i in l:
    x.append(int(i))
o=[]    
e=[]
r=[]
for i in x:
    if i%2==1:
        o.append(i)
    else:
        e.append(i)    
print(o+e)
