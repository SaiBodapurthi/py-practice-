n=int(input())
x=n
t=0
while x>=2:
    if x%2!=0:
        t=1
        break;
    x=x/2
if t==0 and n>=2:
    print("is in powers of 2")
else:
    print("not in powers of 2")