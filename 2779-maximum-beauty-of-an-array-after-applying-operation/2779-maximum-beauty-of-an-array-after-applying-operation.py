from collections import defaultdict
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)
        
        for i in range(n):
            mp[nums[i]-k] += 1
            mp[nums[i]+k+1] -= 1
        
        x, ans = 0, 0
        
        for p in sorted(mp):
            x += mp[p]
            ans = max(ans, x)
        
        return ans
    
    
    