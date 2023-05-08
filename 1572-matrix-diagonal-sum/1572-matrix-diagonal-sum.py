class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        n=len(mat)
        for i in range(len(mat)):
            s+=mat[i][i]
            s+=mat[i][len(mat)-1-i]
            
        return s-(mat[n//2][n//2] if n%2 else 0)