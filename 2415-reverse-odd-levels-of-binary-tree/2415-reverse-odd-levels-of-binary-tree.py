# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        
        while q:
            n = len(q)
            if level&1:
                l, r = 0, n-1
                while l<r:
                    q[l].val, q[r].val = q[r].val, q[l].val
                    l += 1
                    r -= 1
            for i in range(len(q)):
                x = q.popleft()
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                    
            level += 1

        return root
                
            
            