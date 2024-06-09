from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        ans = presum = 0
        
        for i in nums:
            presum += i
            r = presum % k
            r += k if r < 0 else 0
            ans += prefix_map[r]
            prefix_map[r] += 1
        
        return ans
