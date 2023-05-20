
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) # map a -> [b, a/b]
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q, visited = deque(), set()
            q.append([src, 1]) # src and mul(weight)
            visited.add(src)
            while q:
                node, wt = q.popleft()
                if node == target:
                    return wt
                for nbr, weight in adj[node]:
                    if nbr not in visited:
                        q.append([nbr, wt * weight])
                        visited.add(nbr)
            return -1
        
        ans = [bfs(q[0], q[1]) for q in queries]
        return ans