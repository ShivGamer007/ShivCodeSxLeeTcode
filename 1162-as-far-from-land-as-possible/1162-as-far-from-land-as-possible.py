class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = deque((i, j) for i in range(n) for j in range(n) if grid[i][j])
        res = 0
        while dq:
            r0, c0 = dq.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r1, c1 = r0 + dr, c0 + dc
                if 0 <= r1 < n and 0 <= c1 < n and not grid[r1][c1]:
                    dq.append((r1, c1))
                    grid[r1][c1] = grid[r0][c0] + 1
                    res = max(res, grid[r1][c1])
        return res - 1
        
        
        
        
        
#         mxdis=0
#         r=len(grid)
#         c=len(grid[0])
#         water=[]
#         land=[]
#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j]==0:
#                     water.append([i,j])
#                 else:
#                     land.append([i,j])
#         if len(water)==0 or len(land)==0:
#             return -1
#         for i in water:
#             for j in land:
#                 mxdis=max(mxdis,abs(i[0]-j[0])+abs(i[1]-j[1]))
                
#         return mxdis

