# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBst(node,mn,mx):
            if node==None:
                return True
            if (mn!=None and node.val<=mn.val): return False
            if (mx!=None and node.val>=mx.val): return False
            return isBst(node.left,mn,node) and isBst(node.right,node,mx)
        return isBst(root,None,None)