class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        #memoization - DP
        
        m,n=len(nums1),len(nums2)
        dp={}
        def bfs(i, j):
            if i == m or j == n:
                return 0
            
            if (i, j) in dp: 
                return dp[(i, j)]
            
            if nums1[i] == nums2[j]:
                dp[(i, j)] = 1 + bfs(i + 1, j + 1)
            else:
                dp[(i, j)] = max(bfs(i + 1, j), bfs(i, j + 1))
                
            return dp[(i, j)]
        
        return bfs(0, 0)