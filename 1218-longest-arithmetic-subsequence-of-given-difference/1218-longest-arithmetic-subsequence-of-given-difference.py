class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 0
        for i in range(len(arr)):
            x = arr[i] - difference
            prev = dp[x] if x in dp else 0
            
            dp[arr[i]] = 1 + prev

            ans = max(ans, dp[arr[i]])

        return ans