class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freqs = {}
        x = "abcdefghijklmnopqrstuvwxyz"
        for i in x:
            freqs[i] = 0
        for i in s:
            freqs[i] += 1
        cnt = 0
        for ch in t:
            if freqs[ch] != 0:
                freqs[ch] -= 1
            else:
                cnt +=1
        return cnt