class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=-999999999
        n=len(nums)
        cursum=0
        for i in range(n):
            cursum+=nums[i]
            mx=max(cursum,mx)
            if cursum<0:
                cursum=0
        return mx