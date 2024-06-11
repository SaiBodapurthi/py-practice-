a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
res=0;
if len(a1)%2==0 and len(a2)%2==0:
    res=0
elif len(a1)%2!=0 and len(a2)%2!=0:
    x=0
    y=0
    for i in range(0,len(a1)):
        x=x^a1[i]
    for j in range(0,len(a2)):
        y=y^a2[i]
    res=x^y
else:
    if len(a1)%2!=0:
        for i in range(0,len(a1)):
            res=res^a1[i]
    else:
        for i in range(0,len(a2)):
            res=res^a2[i]
print(res)