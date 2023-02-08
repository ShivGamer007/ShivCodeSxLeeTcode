class Solution:
    def jump(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=max(nums[i]+i,nums[i-1])
        idx=0
        ans=0
        while(idx<len(nums)-1):
            ans+=1
            idx=nums[idx]
        return ans
        