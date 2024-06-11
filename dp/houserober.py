ar=list(map(int,input().split()))
def logic(ar,n,dp):
    if(n<=0):
        return 0
    if(dp[n]!=-1):
        return dp[n]
    pick=ar[n-1]+logic(ar,n-2,dp)
    not_pick=0+logic(ar,n-1,dp)
    
    dp[n]=max(pick,not_pick)
    return dp[n]
dp = [-1 for i in range(len(ar))]
dp2 = [-1 for i in range(len(ar))]

ar1=[]
for i in range(0,len(ar)-1):
    ar1.append(ar[i])
ar2=[]
for i in range(1,len(ar)):
    ar2.append(ar[i])
    
ans1=logic(ar1,len(ar1),dp)
ans2=logic(ar2,len(ar2),dp2)

print(max(ans1,ans2))