class Solution:
    def dfs(self, al, visited, fromnode):
        ch=0
        visited[fromnode]=True
        for tonode in al[fromnode]:
            if not visited[abs(tonode)]:
                ch+=self.dfs(al,visited,abs(tonode))+(1 if tonode>0 else 0)
        return ch
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        al=[[] for _ in range(n)]
        for c in connections:
            al[c[0]].append(c[1])
            al[c[1]].append(-c[0])
        visited=[False]*n
        return self.dfs(al,visited,0)
        