class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        s, l = 0, 0
        ans = len(nums)
        for i, val in enumerate(nums):
            s += val
            while s >= target:
                s -= nums[l]
                ans = min(ans, i-l+1)
                l += 1
        return ans
        