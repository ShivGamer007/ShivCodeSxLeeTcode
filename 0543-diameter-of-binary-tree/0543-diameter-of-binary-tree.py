# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.ans
        
    def height(self,root):
        if root==None:
            return 0
        lh=self.height(root.left)
        rh=self.height(root.right)
        d=lh+rh
        self.ans=max(self.ans,d)
        return max(lh,rh)+1
