# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x = ""
        tmp = head
        while tmp != None:
            x += str(tmp.val)
            tmp = tmp.next
        # print(x)
        if x == x[::-1]:
            return True
        return False
        