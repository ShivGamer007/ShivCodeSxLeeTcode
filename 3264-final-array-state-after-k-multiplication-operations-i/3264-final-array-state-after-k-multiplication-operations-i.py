class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            x = min(nums)
            nums[nums.index(x)] = x*multiplier
        return nums
            