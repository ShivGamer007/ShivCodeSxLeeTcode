# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = []
        tmp = head
        p = []
        while tmp != None:
            if tmp.val != 0:
                p.append(tmp.val)
            else:
                x.append(sum(p))
                p = []
            tmp = tmp.next
        x = x[1:]
        print(x)
        if len(x) == 0:
            return None
        h1 = ListNode(x[0])
        x.pop(0)
        t1 = h1
        while len(x):
            t2 = ListNode(x[0])
            x.pop(0)
            t1.next = t2
            t1 = t1.next
        
        
        return h1
            
                