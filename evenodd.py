ar=list(map(int,input().split()))
even=0
odd=0
for i in range(len(ar)):
    if ar[i]%2==0:
        even+=1
    else:
        odd+=1
print("even : ",even,"odd : ",odd)