class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        obs_sum = sum(rolls)
        total = mean*(m+n)
        miss_sum = total - obs_sum
        
        if miss_sum < n or miss_sum > 6*n:
            return []
        
        avg_val = miss_sum // n
        ans = [avg_val] * n
        
        rem = miss_sum % n
        for i in range(rem):
            ans[i] += 1
        
        return ans