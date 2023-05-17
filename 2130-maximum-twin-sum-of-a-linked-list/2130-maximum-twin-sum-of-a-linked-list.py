# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        def reverselinkedlist(head):
            cur = head
            prev = None
            while(cur is not None):
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            return prev
        def printll(head):
            current = head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            
        slow,fast=head,head
        while(slow and fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        h2=slow
        slow=None
        head2 = reverselinkedlist(h2)
        t1, t2 = head, head2
        ans=0
        
        while(t1 and t2):
            sm = t1.val + t2.val
            ans=max(ans,sm)
            t1 = t1.next
            t2 = t2.next
        return ans