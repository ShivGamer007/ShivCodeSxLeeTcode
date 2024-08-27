class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = [[] for i in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            adj[u].append((v, p))
            adj[v].append((u, p))
            
        dist = [0.0] * n
        dist[start_node] = 1
        
        q = deque([start_node])
        while q:
            cur = q.popleft()
            for node, prob in adj[cur]:
                new_prob = dist[cur] * prob
                if new_prob > dist[node]:
                    dist[node] = new_prob
                    q.append(node)
        return dist[end_node]
        
        
        
        