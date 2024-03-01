class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zero, one = s.count('0'), s.count('1')
        
        ans = ""
        for i in range(one-1):
            ans += '1'
        for i in range(zero):
            ans += '0'
        return ans+'1'
        