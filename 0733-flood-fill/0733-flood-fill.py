class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        
        def dfs(r, c, src):#src = source val = image[sr,sc]
            if r<0 or r>=rows or c<0 or c>=cols:
                return 
            elif image[r][c] != src:
                return 
            image[r][c] = color
            
            dfs(r+1, c, src)
            dfs(r-1, c, src)
            dfs(r, c+1, src)
            dfs(r, c-1, src)
            
        if color == image[sr][sc]: return image
        
        src = image[sr][sc]
        dfs(sr, sc, src)
        
        return image