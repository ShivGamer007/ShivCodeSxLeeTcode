from collections import defaultdict
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = 0
        dc = defaultdict(int)
        
        for r in range(n):
            dc[nums[r]] += 1
            while max(dc.keys())-min(dc.keys()) > 2:
                dc[nums[l]] -= 1
                if dc[nums[l]] == 0:
                    del dc[nums[l]]
                l += 1
            res += (r-l+1)
        
        return res