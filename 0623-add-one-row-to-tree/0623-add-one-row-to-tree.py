# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def dfs(root, val, depth):
            if root == None: return
            if depth > 2:
                dfs(root.left, val, depth-1)
                dfs(root.right, val, depth-1)
            else:
                tmp = root.left
                root.left = TreeNode(val, tmp, None)
                tmp = root.right
                root.right = TreeNode(val, None, tmp)
        if depth == 1:
            tmp = TreeNode(val, root, None)
            return tmp
        dfs(root, val, depth)
        return root
