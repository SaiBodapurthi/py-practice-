ar=list(map(int,input().split()))
ans=0
for i in range(0,len(ar)):
    ans=ans^ar[i]
print(ans)