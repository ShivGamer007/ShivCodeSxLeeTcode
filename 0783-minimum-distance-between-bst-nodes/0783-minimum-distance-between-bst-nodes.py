# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.mindif=float('inf')
        self.prev=None
        self.inorder(root)
        return self.mindif
    def inorder(self,root: TreeNode):
        if root is None:
            return
        self.inorder(root.left)
        if self.prev is not None:
            self.mindif=min(self.mindif,root.val-self.prev)
        self.prev=root.val
        self.inorder(root.right)
      