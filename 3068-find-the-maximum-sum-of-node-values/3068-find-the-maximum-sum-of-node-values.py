class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        res = 0
        c = 0
        d = 1 << 30
        for a in nums:
            b = (a ^ k)
            res += max(a, b)
            c ^= a < b
            d = min(d, abs(a - b))
        return res - d * c