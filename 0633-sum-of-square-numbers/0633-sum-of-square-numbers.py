class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        # c = a^2 + b^2
        # b = sqrt(c-a^2)
        x = int(c**0.5)
        for a in range(x+1):
            b = int((c-(a*a))**0.5)
            if a*a + b*b == c:
                return True
        return False