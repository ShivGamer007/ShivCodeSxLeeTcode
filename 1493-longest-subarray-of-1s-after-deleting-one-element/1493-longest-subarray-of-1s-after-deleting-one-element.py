class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        h, t, cnt, ans = 0, 0, 0, 0
        while (h<len(nums)):
            
            if nums[h] == 0:
                cnt += 1
            
            while (cnt > 1):
                if nums[t] == 0:
                    cnt -= 1
                t += 1
            
            ans = max(ans, h-t)
            
            h += 1
        return ans