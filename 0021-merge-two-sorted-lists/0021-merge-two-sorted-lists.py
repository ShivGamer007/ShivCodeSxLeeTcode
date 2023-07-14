# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        ret=res
        if list1 is None and list2 is None:
            return res.next
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            res=list1
            list1=list1.next
        else:
            res=list2
            list2=list2.next
        ret=res
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                ret.next=list1
                ret=ret.next
                list1=list1.next
            else:
                ret.next=list2
                ret=ret.next
                list2=list2.next
        if list1 is None:
            ret.next=list2
        else:
            ret.next=list1
        return res
            