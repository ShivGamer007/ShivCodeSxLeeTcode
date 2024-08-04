class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum = []
        mod = 10**9+7
        for i in range(n):
            x = (nums[i])%mod
            sum.append(x)
            for j in range(i+1, n):
                x = (x+nums[j])%mod
                sum.append(x)
        sum.sort()
        # print(sum)
        ans = 0
        for i in range(left-1, right):
            ans = (ans + sum[i]) % mod
        return ans % mod