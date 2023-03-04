class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lbound = -1
        lastmin=-1
        lastmax=-1
        c=0
        for i in range(len(nums)):
            if nums[i]>=minK and nums[i]<=maxK:
                lastmin=i if nums[i]==minK else lastmin
                lastmax=i if nums[i]==maxK else lastmax
                c+=max(0,min(lastmin,lastmax)-lbound)
            else:
                lbound=i
                lastmin=-1
                lastmax=-1
        return c
        
        
        
        