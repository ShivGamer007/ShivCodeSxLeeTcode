# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxd=0
        self.calcheight(root)
        return self.maxd
        
        
    def calcheight(self,node):
        if not node:
            return 0
        lefth=self.calcheight(node.left)
        righth=self.calcheight(node.right)
        diameter=lefth+righth
        self.maxd=max(self.maxd,diameter)
        return max(lefth,righth)+1