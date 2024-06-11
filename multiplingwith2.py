n=int(input())
sum=1
for i in range(1,n):
    sum*=2
print(sum)
dig=0
while sum>=1:
    dig+=1
    sum/=10
print(dig)