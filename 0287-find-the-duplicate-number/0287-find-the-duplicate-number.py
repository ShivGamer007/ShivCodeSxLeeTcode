class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
        return 0
        
        
        
#         slow, fast = nums[0], nums[0]
        
#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if slow == fast:
#                 break
#         slow = nums[0]
#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[fast]
#         return slow
        
            
        