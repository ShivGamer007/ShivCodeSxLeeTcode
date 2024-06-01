class Solution:
    def checkRecord(self, s: str) -> bool:
        x = 0
        if s.count("A") < 2:
            x += 1
        for i in range(len(s)-2):
            if s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
                x -= 1
        if x == 1:
            return True
        return False