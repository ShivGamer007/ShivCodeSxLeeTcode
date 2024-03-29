from collections import defaultdict
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        mp = defaultdict(int)
        i, j = 0, 0
        n = len(nums)
        ans = 0
        while j<n:
            mp[nums[j]] += 1
            while mp[mx] >= k:
                ans += (n-j)
                mp[nums[i]] -= 1
                i += 1
            j += 1
        return ans 