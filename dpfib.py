def fib(n,dp):
    if(n==1):
        dp[1]==0
    if(n==2):
        dp[2]==1
    if(dp[n]!=-1):
        return dp[n]
    ans=fib(n-1,dp)+fib(n-2,dp)
    dp[n]=ans
    return ans
n=int(input())
dp=[]
for i in range (n+1):
    dp.append(-1)
ans=fib(n,dp)
print(ans)
