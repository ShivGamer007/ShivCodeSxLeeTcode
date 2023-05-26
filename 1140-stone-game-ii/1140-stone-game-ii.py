class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suf_sum = [0]*(n+1)
        suf_sum[n-1] = piles[n-1]
        for i in range(n-2, -1, -1):
            suf_sum[i] = suf_sum[i+1] + piles[i]
        
        dp = [[0]*(n+1) for i in range(n)]
        for i in range(n-1, -1, -1):
            for p in range(1, n+1):
                if i+2*p >= n:
                    dp[i][p] = suf_sum[i]
                else:
                    for x in range(1, 2*p+1):
                        opp_score = dp[i+x][max(x,p)]
                        score = suf_sum[i] - opp_score
                        dp[i][p] = max(dp[i][p], score)
        return dp[0][1]
        