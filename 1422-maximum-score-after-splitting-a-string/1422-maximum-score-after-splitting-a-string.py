class Solution:
    def maxScore(self, s: str) -> int:
        ans = 1 if s[0]=='0' else 0
        for i in range(1, len(s)):
            zleft = s[:i].count('0')
            oright = s[i:].count('1')
            ans = max(ans, zleft+oright)
        return ans