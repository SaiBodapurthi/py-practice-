ar=list(map(int,input().split()))
s=0
n=len(ar)
i=0
j=n-1
while(i<=j):
    if ar[i]==ar[j]:
        i=i+1
        j=j-1
    else:
        s=-1
        break;
if(s==0):
    print("array is palindrom")
else:
    print("array is not a palindrom")