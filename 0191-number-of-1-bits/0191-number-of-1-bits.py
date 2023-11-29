class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)[2:]
        return str(x).count('1')
