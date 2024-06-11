from collections import defaultdict

class Solution(object):
    def getAncestors(self, n, edges):
        ancestors = [[] for _ in range(n)]
        
        adjacency_list = defaultdict(list)
        for source, destination in edges:
            adjacency_list[source].append(destination)
            
        starting_points = [(node, node) for node in reversed(range(n))]
        visited = set()
        while starting_points:
            level = [starting_points.pop()]
            while level:
                new_level = []
                for node, ancestor in level:
                    if (node, ancestor) not in visited:
                        visited.add((node, ancestor))
                        if node != ancestor:
                            ancestors[node].append(ancestor)
                        for destination in adjacency_list[node]:
                            new_level.append((destination, ancestor))
                level = new_level
            
        return ancestors
n=int(input())
edges=[]
for i in range(n):
    temp=list(map(int,input().split()))
    edges.append(temp)
s=Solution()
res=s.getAncestors(n,edges)
print(res)