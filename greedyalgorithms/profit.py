d_l=list(map(int,input().split()))
pr=list(map(int,input().split()))
for i in range(0,len(pr)):
    for j in range(0,len(pr)-1):
        if pr[j]<pr[j+1]:
            temp=pr[j]
            pr[j]=pr[j+1]
            pr[j+1]=temp
            temp=d_l[j]
            d_l[j]=d_l[j+1]
            d_l[j+1]=temp
print(pr)
print(d_l)
tp=[pr[0]]
tl=1
v=[]
for i in range(0,max(d_l)):
    v.append(-1)
for i in range(1,len(pr)):
    if d_l[i]<=tl and v[tl]==-1:
        tp.append(pr[i])
        tl+=1
        v[tl]=0
print(tp)