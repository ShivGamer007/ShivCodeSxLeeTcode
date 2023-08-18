class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        maxdis = rows + cols
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0: continue
                top, left = maxdis, maxdis
                if(i-1 >= 0): top = mat[i-1][j]
                if(j-1 >= 0): left = mat[i][j-1]
                mat[i][j] = min(top, left) + 1
         
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if mat[i][j] == 0: continue
                bottom, right = maxdis, maxdis
                if(i+1 < rows): bottom = mat[i+1][j]
                if(j+1 < cols): right = mat[i][j+1]
                mat[i][j] = min(mat[i][j], min(bottom, right) + 1)
                
        return mat
