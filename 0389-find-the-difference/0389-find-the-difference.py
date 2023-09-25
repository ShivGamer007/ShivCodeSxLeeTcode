class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        for i in range(len(s)):
            c ^= ord(s[i])
        for i in range(len(t)):
            c ^= ord(t[i])
            
        return chr(c)
        
        
        
        # cnt = {}
        # for i in s:
        #     cnt[i] = cnt.get(i, 0)+1
        # for i in t:
        #     cnt[i] = cnt.get(i, 0)-1
        # for i in cnt:
        #     if cnt[i] == -1:
        #         return i
        # return ""