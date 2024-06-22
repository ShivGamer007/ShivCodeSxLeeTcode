from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        cnt = ans = 0
        # Sliding window
        while j < len(nums):
            if nums[j] % 2:
                k -= 1
                cnt = 0
            while k == 0:
                if nums[i] % 2:
                    k += 1
                cnt += 1
                i += 1
            ans += cnt
            j += 1
        return ans