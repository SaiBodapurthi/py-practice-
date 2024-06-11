ar=list(map(int,input().split()))
sum=ar[1]-ar[0]
count=0
for i in range(1,len(ar)):
    if ar[i]-ar[i-1]==sum:
        count+=1
if count==len(ar):
    print("the array follows AP")
else:
    print("the array not follows AP")