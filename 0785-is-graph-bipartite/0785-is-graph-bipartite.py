class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n
        def validcolor(node,col):
            if color[node] != 0:
                return color[node] == col
            
            color[node] = col
            for nbr in graph[node]:
                if not validcolor(nbr, -col):
                    return False
            return True
        for node in range(n):
            if color[node] == 0 and not validcolor(node, 1):
                return False
        return True
                
        
        
        