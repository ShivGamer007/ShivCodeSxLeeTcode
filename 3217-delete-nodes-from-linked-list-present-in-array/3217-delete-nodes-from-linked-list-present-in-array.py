# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        if not head:
            return None
        while head and head.val in nums:
            head = head.next
        
        prev = head
        cur = head.next
        
        while cur:
            if cur.val in nums:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return head
        
        # tmp = head
        # while tmp.next and tmp.next.next and tmp.next.next:
        #     if tmp.next.val in nums:
        #         tmp.next = tmp.next.next
        #     tmp = tmp.next
        # if tmp.next and tmp.next.val in nums:
        #     tmp.next = None
        # return head