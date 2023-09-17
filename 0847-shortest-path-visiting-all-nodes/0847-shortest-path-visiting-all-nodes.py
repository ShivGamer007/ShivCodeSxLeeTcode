class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque([(i, 1<<i) for i in range(n)])
        visit = set(q)
        ans = 0
        while q:
            for x in range(len(q)):
                a, b = q.popleft()
                if b == (1<<n)-1:
                    return ans
                for v in graph[a]:
                    if (v, b|1<<v) not in visit:
                        q.append((v, b|1<<v))
                        visit.add((v, b|1<<v))
            ans += 1
        return ans
  