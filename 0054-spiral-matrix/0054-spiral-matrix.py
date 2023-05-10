class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        
        if not mat: return []
        
        res=[]
        m=len(mat) #rows
        n=len(mat[0]) #col
        left,right,top,bottom=0,n-1,0,m-1

        
        while len(res) < (m*n):
            
            #left to right in top row
            for c in range(left,right+1):
                res.append(mat[top][c])
            top+=1
            
            #top to bottom in right col
            for r in range(top, bottom + 1):
                res.append(mat[r][right])
            right-=1
            
            #right to left in bottom row (reverse)
            if top<=bottom:
                for c in range(right, left-1,-1):
                    res.append(mat[bottom][c])
                bottom -= 1
            
            #bottom to top in left col (reverse)
            if left<=right:
                for r in range(bottom, top-1, -1):
                    res.append(mat[r][left])
                left += 1
            
        return res