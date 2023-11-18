class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r,n = 0,0,len(nums)
        ans, sm = 0,0
        for l in range(n):
            sm += nums[l]
            if (l-r+1)*nums[l] - sm > k:
                sm -= nums[r]
                r += 1
            ans = max(ans, l-r+1)
        return ans