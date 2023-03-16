# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #post lrr
        if not inorder: return None
        rootval=postorder.pop()
        root=TreeNode(rootval)
        inorderidx=inorder.index(rootval)
        root.right=self.buildTree(inorder[inorderidx+1:],postorder)
        root.left=self.buildTree(inorder[:inorderidx],postorder)
        return root
        
        