# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head=head

    def getRandom(self) -> int:
        cnt=0
        res=0
        cur=self.head
        while(cur):
            cnt+=1
            if random.randint(1,cnt)==1:
                res=cur.val
            cur=cur.next
        return res
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()