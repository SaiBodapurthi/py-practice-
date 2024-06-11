ar=list(map(int,input().split()))
t=-1
even=0
odd=0
for i in range(len(ar)-1):
    if ar[i]==ar[i+1]:
        t=1
        break;
if t==-1:
    for i in range(len(ar)):
        if ar[i]%2==0:
            even+=1
    print(even)
else:
    for i in range(len(ar)):
        if ar[i]%2!=0:
            odd+=1
    print(odd)