class Solution:
    def solvedptab(self,arr):
        n=len(arr)
        #base
        prev2=0
        prev1=arr[0]
        for i in range(1,n):
            incld=prev2+arr[i]
            excld=prev1
            ans=max(incld,excld)
            prev2=prev1
            prev1=ans
        return prev1

        
    def rob(self, nums: List[int]) -> int:
        res=self.solvedptab(nums)
        return res


        