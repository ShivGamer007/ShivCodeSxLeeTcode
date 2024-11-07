class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        cnt = [0]*24
        
        for n in candidates:
            for i in range(24):
                if n & (1<<i):
                    cnt[i] += 1
        
        return max(cnt)