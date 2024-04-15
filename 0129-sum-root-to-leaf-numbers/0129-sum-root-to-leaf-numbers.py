# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        def sumNode(root, cur):
            if root == None: return 0
            cur = cur*10+root.val
            if root.left == None and root.right == None: return cur
            left = sumNode(root.left, cur)
            right = sumNode(root.right, cur)
            return left+right
        
        cur = 0
        return sumNode(root, cur)