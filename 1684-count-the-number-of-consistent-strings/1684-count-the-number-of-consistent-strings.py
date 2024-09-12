class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for word in words:
            f = 1
            for i in word:
                if i not in allowed:
                    f = 0
            if f == 1:
                c+=1
                
        return c