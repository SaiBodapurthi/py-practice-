def knapsack(n,p,w,cap):
    if cap==0:
        return 0
    if n==0:
        return 0
    if w[n-1]>cap:
        return knapsack(n-1,p,w,cap)
    else:
        pick=p[n-1]+knapsack(n-1,p,w,cap-w[n-1])
        not_pick=0+knapsack(n-1,p,w,cap)
        return max(pick,not_pick)
n=int(input())
profit=list(map(int,input().split()))
weigt=list(map(int,input().split()))
capacity= int(input())
ans=knapsack(n,profit,weigt,capacity)
print(ans)