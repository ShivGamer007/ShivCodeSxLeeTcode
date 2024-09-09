class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(mat), len(mat[0])
        left, right, top, bottom = 0, n, 0, m
        
        while left<right and top<bottom:
            
            for i in range(left, right):
                ans.append(mat[top][i])
            top += 1
            
            for i in range(top, bottom):
                ans.append(mat[i][right-1])
            right -= 1
            
            if not(top<bottom and left<right):
                break
            
            for i in range(right-1, left-1, -1):
                ans.append(mat[bottom-1][i])
            bottom -= 1
            
            for i in range(bottom-1, top-1, -1):
                ans.append(mat[i][left])
            left += 1
        return ans
            