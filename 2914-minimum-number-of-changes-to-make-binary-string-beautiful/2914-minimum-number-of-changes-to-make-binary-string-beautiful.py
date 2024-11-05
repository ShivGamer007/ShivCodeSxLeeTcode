class Solution:
    def minChanges(self, s: str) -> int:
        n = 0
        #Greedy pair processing
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                n += 1
                
        return n