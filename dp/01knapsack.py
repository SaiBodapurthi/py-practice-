n = int(input())
p = list(map(int, input().split()))
w = list(map(int, input().split()))
cap = int(input())
dp = [[-1 for i in range(cap + 1)] for j in range(n + 1)]

def knapsack(n, p, w, cap):
    if cap == 0:
        return 0
    if n == 0:
        return 0
    if dp[n][cap] != -1:
        return dp[n][cap]
    if w[n - 1] > cap:
        dp[n][cap] = knapsack(n - 1, p, w, cap)
        return dp[n][cap]
    else:
        pick = p[n - 1] + knapsack(n - 1, p, w, cap - w[n - 1])
        not_pick = knapsack(n - 1, p, w, cap)
        dp[n][cap] = max(pick, not_pick)
        return dp[n][cap]

ans = knapsack(n, p, w, cap)
print(ans)