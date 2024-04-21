class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vis=[False]*n
        d={}
        for i in edges:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]]=[i[1]]
            if i[1] in d:
                d[i[1]].append(i[0])
            else:
                d[i[1]]=[i[0]]
        q=[source]
        while q:
            cur=q.pop(0)
            if cur==destination:
                return True
            elif cur in d and not vis[cur]:
                q.extend(d[cur])
            vis[cur]=True
        return False

