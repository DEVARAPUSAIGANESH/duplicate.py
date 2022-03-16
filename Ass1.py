l=input().split()
x=[]
for i in l:
    x.append(int(i))
res=[]    
for i in x:
    if i not in res:
        res.append(i)
        
print(res)
