class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(dict)
        for x,y,z in roads:
            graph[x][y]=graph[y][x]=z
        minscr=float('inf')
        visited=set()
        queue=deque([1])
        while queue:
            temp=queue.popleft()
            for adj,scr in graph[temp].items():
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
                minscr=min(minscr,scr)
        return minscr