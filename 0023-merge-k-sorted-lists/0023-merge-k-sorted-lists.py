# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        s=[]
        for i in lists:
            x=i
            while x:
                s+=[x.val]
                x=x.next
        s=sorted(s,reverse=True)
        res=None
        for i in s:
            res=ListNode(i,res)
        return res
        