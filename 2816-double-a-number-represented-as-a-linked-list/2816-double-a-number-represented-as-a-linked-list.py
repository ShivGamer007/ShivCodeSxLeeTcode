# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = 0
        tmp = head
        while(tmp):
            x = x*10+tmp.val
            tmp = tmp.next
        x = 2*x
        p = []
        if x>0:
            while x>0:
                p.append(x%10)
                x = x//10
            p = p[::-1]
        else:
            p.append(0)
       
        h2 = ListNode(p[0], None)
        p.pop(0)
        
        t = h2
        while p:
            new = ListNode(p[0], None)
            t.next = new
            t = t.next
            p.pop(0)
        
        return h2