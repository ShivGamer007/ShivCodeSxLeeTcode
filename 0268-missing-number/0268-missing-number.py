class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mx = max(nums)
       
        if mx == len(nums)-1:
            return mx+1
        for i in range(mx):
            if i not in nums:
                return i
                