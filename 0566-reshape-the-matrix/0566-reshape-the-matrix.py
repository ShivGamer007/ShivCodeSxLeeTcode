class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat
        p=len(mat)
        q=len(mat[0])
        x=[]
        for i in range(p):
            for j in range(q):
                x.append(mat[i][j])
        res=[[0]*c for _ in range(r)]
        ele=p*q
        z=0
        for i in range(r):
            for j in range(c):
                res[i][j]=x[z]
                z+=1
        return res
        
        
#         p=len(mat)
#         q=len(mat[0])
#         res=[[0]*c for _ in range(r)]
#         for i in range(p*q):
#             res[i//c][i%c]=mat[i//q][i%q]
#         return res
       
            