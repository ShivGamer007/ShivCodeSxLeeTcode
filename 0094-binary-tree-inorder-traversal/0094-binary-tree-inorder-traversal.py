# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.inorder_Traversal(root,ans)
        return ans
    def inorder_Traversal(self,root,ans):
        if root!=None:
            self.inorder_Traversal(root.left,ans)
            ans.append(root.val)
            self.inorder_Traversal(root.right,ans)
        return ans
    