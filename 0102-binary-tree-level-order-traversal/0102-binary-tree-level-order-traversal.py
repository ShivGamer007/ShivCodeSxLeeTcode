# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root: return ans
        q = []
        q.append(root)
        while len(q) != 0:
            n = len(q)
            level = []
            for i in range(n):
                node = q[0]
                q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level.append(node.val)
            ans.append(level)
        return ans
    