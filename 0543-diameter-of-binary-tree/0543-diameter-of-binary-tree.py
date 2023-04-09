# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node==None: return 0
            lh=height(node.left)
            rh=height(node.right)
            dia=(lh+rh)
            self.ans=max(self.ans,dia)
            return max(lh,rh)+1
        height(root)
        return self.ans