class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                x = len(set(nums[i:j+1]))
                ans += x**2
        return ans