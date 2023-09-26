class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # s = [i for i in s]
        # s = "".join(sorted(list(set(s))))
        # return s
        
        last_occurance = {}
        stk = []
        visited = set()
        for i in range(len(s)):
            last_occurance[s[i]] = i
        for i in range(len(s)):
            if s[i] not in visited:
                while (stk and stk[-1] > s[i] and last_occurance[stk[-1]] > i):
                    visited.remove(stk.pop())
                stk.append(s[i])
                visited.add(s[i])
        return "".join(stk)        
    
    