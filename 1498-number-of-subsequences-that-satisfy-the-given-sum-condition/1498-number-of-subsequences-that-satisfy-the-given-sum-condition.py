class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod=10**9+7
        ans=0
        for i in range(len(nums)):
            l=i
            r=len(nums)-1
            idx=-1
            while(l<=r):
                mid=(l+(r-l)//2)
                if nums[i]+nums[mid]<=target:
                    idx=mid
                    l=mid+1
                else:
                    r=mid-1
            if idx!=-1:
                ans+=pow(2,(idx-i),mod)
        return ans%mod
            