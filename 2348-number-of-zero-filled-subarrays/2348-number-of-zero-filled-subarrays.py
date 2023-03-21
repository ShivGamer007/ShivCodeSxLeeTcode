class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total=cur=0
        for n in nums:
            if n==0:
                cur+=1
                total+=cur
            else:
                cur=0
        return total
        
        
        