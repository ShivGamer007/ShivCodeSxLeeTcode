#User function Template for python3

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        # code here 
        # left, right, top, bottom = 0, m-1, 0, n-1
        
            
            
        ans = []
        if n == 1:
            return matrix[0]
        if m==1:
            for i in range(n):
                ans.append(matrix[i][0])
            return ans
            
            
        ans.extend(matrix[0])
        
        for i in range(1, n-1):
            ans.append(matrix[i][m-1])
        
        # for j in range(m-2, -1, -1):
        #     ans.append(matrix[n-1][j])
        
        tmp = matrix[n-1]
        tmp.reverse()
        # print(tmp)
        ans.extend(tmp)
        
        for i in range(n-2, 0, -1):
            ans.append(matrix[i][0])
            
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends