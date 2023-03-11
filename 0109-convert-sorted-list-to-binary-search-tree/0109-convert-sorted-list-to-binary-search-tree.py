# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return head
        mid=self.findmid(head)
        root = TreeNode(mid.val)
        if head==mid:
             return root
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)
        return root
        
    def findmid(self,head):
        fast=head
        slow=head
        prev=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev is not None:
            prev.next=None
        return slow