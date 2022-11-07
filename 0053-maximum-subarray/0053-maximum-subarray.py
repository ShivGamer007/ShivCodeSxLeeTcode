class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's
        if len(nums)==1:
            return nums[0]
        mx=nums[0]
        sm=0
        for i in range(len(nums)):
            sm=max(sm+nums[i],nums[i])
            mx=max(mx,sm)
        return mx