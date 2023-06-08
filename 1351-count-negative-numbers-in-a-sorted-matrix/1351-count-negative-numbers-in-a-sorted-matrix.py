class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        i = 0
        j = len(grid[0]) - 1
        
        #row and coloumn wise sorted
        
        while i<len(grid) and j >= 0:
            if grid[i][j] < 0:
                c += len(grid)-i
                j -= 1
            elif grid[i][j] >= 0:
                i += 1
        return c
    