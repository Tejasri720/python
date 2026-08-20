k=7
m=867
l=[]
total=0

for i in range(k):
    val=list(map(int,input().split()))
    final=val[1:]
    
    l.append(final)

print(l)

for i in l:
    ele=0
    for j in i:
        if j**2%m>ele:
            ele=j**2%m
    total+=ele

print(total%m)
  
    
    
