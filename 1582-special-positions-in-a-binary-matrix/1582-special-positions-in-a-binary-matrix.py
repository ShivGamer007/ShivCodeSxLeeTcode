class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        r_cnt = [0]*m
        c_cnt = [0]*n
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    r_cnt[r] += 1
                    c_cnt[c] += 1
        ans = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    if r_cnt[r] == 1 and c_cnt[c] == 1:
                        ans += 1
        return ans
        
