ar=list(map(int,input().split()))
ans=0
for i in range(0,len(ar)):
    ans = ans ^ ar[i]
pos =0
while(ans>0):
    if(ans % 2!=0):
        break
    pos = pos + 1
    ans = ans//2
temp = 1<<pos
left = 0
right =0
for i in range(0,len(ar)):
    if(ar[i]&temp==0):
        left=left ^ar[i]
    else: 
        right = right ^ ar[i]
print(left)
print(right)