# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def serialize(self, node, subtree, duplicates):
        if not node: return "null"
        l=self.serialize(node.left,subtree,duplicates)
        r=self.serialize(node.right,subtree,duplicates)
        s=l+","+r+","+str(node.val)
        if s in subtree:  
            if subtree[s]==1: duplicates.append(node)
            subtree[s]+=1
        else:
            subtree[s]=1
        return s
        
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree={}
        duplicates=[]
        self.serialize(root,subtree,duplicates)
        return duplicates