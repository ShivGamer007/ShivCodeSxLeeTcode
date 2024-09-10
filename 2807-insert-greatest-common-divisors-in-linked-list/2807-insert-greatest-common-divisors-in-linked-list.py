# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        nxt = head.next
        
        def getGCD(a, b):
            while (b):
                a, b = b, a%b
            return a
        
        while prev.next:
            curval = getGCD(prev.val, nxt.val)
            cur = ListNode(curval, prev.next)
            prev.next = cur
            prev = nxt
            nxt = nxt.next
        return head