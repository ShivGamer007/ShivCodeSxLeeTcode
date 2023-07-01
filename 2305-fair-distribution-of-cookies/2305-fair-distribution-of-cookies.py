class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unf = float('inf')
        distribution = [0] * k
        
        def backTrack(i):
            nonlocal min_unf, distribution
            
            if i == len(cookies):
                min_unf = min(min_unf, max(distribution))
                return
            
            if min_unf <= max(distribution):
                return
            
            for j in range(k):
                distribution[j] += cookies[i]
                backTrack(i+1)
                distribution[j] -= cookies[i]
                
        backTrack(0)
        return min_unf