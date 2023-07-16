class Solution:
    def climbStairs(self, n: int) -> int:
        pre = 1
        pre2 = 0
        for i in range(1, n + 1):
            cur = pre + pre2
            pre2 = pre
            pre = cur
        return pre
    