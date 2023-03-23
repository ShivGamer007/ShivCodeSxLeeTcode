class Solution:
    def makeConnected(self, n: int, conn: List[List[int]]) -> int:
        if len(conn)<n-1:
            return -1
        graph=[set() for i in range(n)]
        for u,v in conn:
            graph[u].add(v)
            graph[v].add(u)
        visited=[0]*n
        
        def dfs(node):
            if visited[node]:
                return 0
            visited[node]=1
            for nbr in graph[node]:
                dfs(nbr)
            return 1
        return sum(dfs(node) for node in range(n))-1
        
        
        