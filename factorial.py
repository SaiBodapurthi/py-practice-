def cal(n):
    if n==1:
        return 1
    else:
        return n* cal(n-1)
n=int(input());
fact=cal(n)
print(fact)
    