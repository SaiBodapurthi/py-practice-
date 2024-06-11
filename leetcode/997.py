n=int(input())
ar=[]
for i in range(0,n):
    temp=list(map(int,input().split()))
    ar.append(temp)
ind=[0 for i in range(n+1)]
outd=[0 for i in range(n+1)]
for i in range(0,2):
    sv=ar[i][0]
    ev=ar[i][i]
    ind[ev]+=1
    outd[sv]+=1
flag=0
for i in range(1,n+1):
    if ind[i]==n-1 and outd[i]==0 :
        flag=i
        break
if flag==0:
    print("-1")
else:
    print(flag)