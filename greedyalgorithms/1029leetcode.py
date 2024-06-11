costs=[]
n=int(input())
for i in range(0,n):
    temp=[]
    temp=list(map(int,input().split()))
    costs.append(temp)
dif=[]
sum=0
for i in range(0,len(costs)):
    sum+=costs[i][0]
    dif.append(costs[i][1]-costs[i][0])
dif.sort()
for i in range(0,len(costs)//2):
    sum+=dif[i]
print(sum)