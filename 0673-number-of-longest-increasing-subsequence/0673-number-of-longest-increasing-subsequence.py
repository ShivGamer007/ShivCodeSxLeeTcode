class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        cnt = [1]*n
        mxlen = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        cnt[i] = cnt[j]
                    elif dp[j]+1 == dp[i]:
                        cnt[i] += cnt[j]
                mxlen = max(mxlen, dp[i])
        ans = 0
        for i in range(n):
            if dp[i] == mxlen:
                ans += cnt[i]
        return ans
        
      