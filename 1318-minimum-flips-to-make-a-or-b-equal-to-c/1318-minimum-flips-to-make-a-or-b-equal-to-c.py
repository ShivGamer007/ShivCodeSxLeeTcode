class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        
        while a > 0 or b > 0 or c > 0:
            bita = a & 1
            bitb = b & 1
            bitc = c & 1
            
            if bitc == 0:
                cnt += (bita + bitb)
            else:
                if bita == 0 and bitb == 0:
                    cnt += 1
            a >>= 1
            b >>= 1
            c >>= 1
            
        return cnt
        