n = int(input())
e = int(input())
parent = [-1 for i in range(n+1)]

def find(a):
    if parent[a] == a:
        return a 
    else:
        while parent[a] != a:
            a = parent[a]
    return a
        
def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        parent[y] = x 
    else:
        parent[x] = y

for i in range(0, n+1):
    parent[i] = i 
    
adj = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(0, e):
    sv = int(input())
    ev = int(input())
    wt = int(input())
    union(sv, ev)
    adj[sv][ev] = wt
    adj[ev][sv] = wt
    
a = find(1)
ans = 10000

for i in range(1, n+1):
    for j in range(1, n+1):
        if adj[i][j] != 0:
            x = find(i)
            y = find(j)
            if x == a and y == a:
                ans = min(ans, adj[i][j])
                
print(ans)