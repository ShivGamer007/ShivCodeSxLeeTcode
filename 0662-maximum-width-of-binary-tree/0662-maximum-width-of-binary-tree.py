# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([(root,0)])
        mx_width=0
        while q:
            level=len(q)
            _, level_st=q[0]
            for i in range(level):
                node, idx=q.popleft()
                if node.left:
                    q.append((node.left,2*idx))
                if node.right:
                    q.append((node.right,2*idx+1))
            mx_width=max(mx_width, idx-level_st+1)
        return mx_width
    
            