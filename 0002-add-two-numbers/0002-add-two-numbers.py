# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        c = 0
        
        while l1 != None or l2 != None or c != 0:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            t = a+b+c
            cur.next = ListNode(t%10)
            c = t//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        return head.next