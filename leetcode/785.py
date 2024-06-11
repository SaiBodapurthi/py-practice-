v=int(input())
e=int(input())
def dfs(adj,v,sv,vis):
    vis[sv]=1 
    print(sv)
    for i in range(0,v):
        if(adj[sv][i]==1 and vis[i]==0):
            dfs(adj,v,i,vis)
adj=[[0 for i in range(v)]for j in range(v)]
for i in range(0,e):
    sv=int(input())
    ev=int(input())
    adj[sv][ev]=1
vis=[0 for i in range(0,v)]
dfs(adj,v,sv,vis)