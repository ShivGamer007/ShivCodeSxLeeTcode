class Solution:
    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
        dp = [[0]*n for i in range(n)]
        dp[row][col] = 1
        move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        
        for i in range(1, k+1):
            Newdp = [[0]*n for i in range(n)]
            for r in range(n):
                for c in range(n):
                    for m in move:
                        newr = r + m[0]
                        newc = c + m[1]
                        if 0<=newr<n and 0<=newc<n:
                            Newdp[r][c] += dp[newr][newc]/8.0
            dp = Newdp
        prob = 0.0
        for r in range(n):
            for c in range(n):
                prob += dp[r][c]
        return prob
            
        