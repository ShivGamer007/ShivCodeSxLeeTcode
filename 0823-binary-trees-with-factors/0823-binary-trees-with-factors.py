class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9+7
        arr.sort()
        res = 0
        mpans = {}
        
        for i in range(len(arr)):
            mpans[arr[i]] = 1
        
        for i in range(1, len(arr)):
            x = arr[i]
            t = int(x**0.5)
            ans = 1
            for j in range(2, t+1):
                if x % j == 0:
                    p = x//j
                    if (j in mpans) and (p in mpans):
                        if p == j: 
                            ans += mpans[j] * mpans[j]
                        else:
                            ans += (mpans[j] * mpans[p])*2
            mpans[x] = ans % mod
        for i in mpans:
            res += mpans[i]
        return res % mod
                            