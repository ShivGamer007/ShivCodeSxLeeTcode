class Solution:
    def new21Game(self, n: int, k: int, maxpts: int) -> float:
        if k == 0 or n >= (k + maxpts):
            return 1.0
        windowsm = 1.0
        prob = 0.0
        dp = [0.0] * (n+1)
        dp[0] = 1.0
        for i in range(1, n+1):
            dp[i] = windowsm/maxpts
            if i<k:
                windowsm += dp[i]
            else:
                prob += dp[i]
            
            if i >= maxpts:
                windowsm -= dp[i - maxpts]
                
        return prob
        
        
        