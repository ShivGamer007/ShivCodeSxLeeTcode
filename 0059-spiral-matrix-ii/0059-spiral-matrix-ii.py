class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat=[[0]*n for _ in range(n)]
        left,right,top,bottom=0,n-1,0,n-1
        val=1
        
        while left<=right:
            
            #left to right in top row
            for c in range(left,right+1):
                mat[top][c]=val
                val+=1
            top+=1
            
            #top to bottom in right col
            for r in range(top,bottom+1):
                mat[r][right]=val
                val+=1
            right-=1
            
            #right to left in bottom row (reverse):
            for c in range(right,left-1,-1):
                mat[bottom][c]=val
                val+=1
            bottom -=1
            
            #bottom to top in left col (reverse):
            for r in range(bottom,top-1,-1):
                mat[r][left]=val
                val+=1
            left+=1
            
        return mat 