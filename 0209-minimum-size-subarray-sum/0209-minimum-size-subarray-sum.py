class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target: return 0
        
        i, j, sm = 0, 0, 0
        ans = len(nums)
        
        while(j < len(nums)):
            sm += nums[j]
            while(sm >= target):
                ans = min(ans, j-i+1)
                sm -= nums[i]
                i += 1
            j +=1
        return ans
        
        
        
        
#         if sum(nums) < target:
#             return 0
#         s, l = 0, 0
#         ans = len(nums)
#         for i, val in enumerate(nums):
#             s += val
#             while s >= target:
#                 s -= nums[l]
#                 ans = min(ans, i-l+1)
#                 l += 1
#         return ans
        
        