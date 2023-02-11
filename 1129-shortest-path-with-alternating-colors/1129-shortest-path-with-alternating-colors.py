class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for i,j in redEdges: graph[i].append((j,"r"))
        for i,j in blueEdges: graph[i].append((j,"b"))
        res=[-1]*n
        que=deque([(0, 0, None)])
        visited=set()
        while(que):
            node, dist, prevEdge = que.popleft()
            visited.add((node,prevEdge))
            if res[node]==-1:
                res[node]=dist
            else:
                res[node]=min(res[node],dist)
            for neighbour,edge in graph[node]:
                if (neighbour,edge) not in visited and prevEdge != edge:
                    que.append((neighbour,dist+1,edge))
        return res
        