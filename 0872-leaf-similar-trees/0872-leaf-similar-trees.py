# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def DFS(node, arr):
            if node:
                if not node.left and not node.right: arr += [node.val]
                DFS(node.left, arr)
                DFS(node.right, arr)
                return arr
        return DFS(root1, []) == DFS(root2, [])