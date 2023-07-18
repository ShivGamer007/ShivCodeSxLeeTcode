class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            lsb = n&1
            revlsb = lsb << (31-i)
            ans = ans | revlsb
            n = n >> 1
        return ans
        
   