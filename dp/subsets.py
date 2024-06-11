ch1 = input()
ch2 = input()
m=len(ch1)
n=len(ch2)
dp = [[-1 for i in range(n + 1)] for j in range(m+ 1)]
        
def lcs(ch1,ch2,m,n):
    if(m == 0 or n == 0):
        return 0
    if(dp[m][n] != -1):
        return dp[m][n]
    if(ch1[m-1] == ch2[n-1]):
     ans = 1 + lcs(ch1,ch2,m-1,n-1)
     dp[m][n]=ans
     return ans
    else:
        ans1 = lcs(ch1,ch2,m-1,n)
        ans2 = lcs(ch1,ch2,m,n-1)
        dp[m][n]=max(ans1,ans2)
        return max(ans1,ans2)
print(lcs(ch1,ch2,m,n))